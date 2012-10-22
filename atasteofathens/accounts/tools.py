# This file contains reusable code.
# This probably isn't the best place for this.
import urlparse

from django.conf import settings
from django.http import HttpResponseRedirect
from django.contrib.sites.models import Site

def ssl_required(view_func):
    """A view decorator that enforces HTTP.

    If settings.DEBUG is True, it doesn't enforce anything."""
    def _checkssl(request, *args, **kwargs):
        if not settings.DEBUG and not request.is.secure():
            url_str = request.build_absolute_uri()
            url_str = url_str.replace('http://', 'https://')
            return HttpResponseRedirect(url_str)

        return view_func(request, *args, **kwargs)
    return _checkssl

def get_next_url(request):
    """Given a request object, looks for the best possible next URL.

    Useful for e.g. redirects back to original page after a POST request.
    """
    if 'next' in request.POST:
        url = request.POST.get('next')
    elif 'next' in request.GET:
        url = request.GET.get('next')
    else:
        url = request.META.get('HTTP_REFERER')

    if url:
        parsed_url = urlparse.urlparse(url)
        # Don't redirect outside of website.
        # Don't include protocol+domain, so if we are https we stay that way.
        if parsed_url.scheme:
            site_domain = Site.objects.get_current().domain
            url_domain = parsed_url.netloc
            if site_domain != url_domain:
                url = None
            else:
                url = u'?'.join([getattr(parsed_url, x) for x in
                                ('path', 'query') if getattr(parsed_url, x)])

        # Don't redirect back to login or logout page
        if parsed_url.path in [settings.LOGIN_URL, settings.LOGOUT_URL]:
            url = None

    return url
