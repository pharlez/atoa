from django.shortcuts import render, render_to_response, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from atasteofathens.ratings.models import Restaurant

@login_required
def index(request):
    return render(request, 'ratings/index.html')

@login_required
def users(request):
    user_list = User.objects.all()
    return render(request, 'ratings/user_list.html', {'user_list': user_list})

@login_required
def user_profile(request, user_name):
    u = get_object_or_404(User, username=user_name)
    return render(request, 'ratings/user_profile.html', {'user': u})

@login_required
def user_rate(request, user_name):
    u = get_object_or_404(User, username=user_name)

    all_items = Restaurant.objects.all()

    user_ratings = [(i.restaurant, i.rating_value) for i in u.u_ratings.all()]
    rated_items = [x[0] for x in user_ratings]
    no_rating = [(i, None) for i in all_items if i not in rated_items]

    user_ratings = user_ratings + no_rating
    user_ratings.sort(key=lambda item: item[0].name)

    return render(request, 'ratings/user_rate.html', 
                             {'user': u,
                              'user_ratings': user_ratings})
@login_required
def items(request):
    restaurant_list = Restaurant.objects.all()
    return render(request, 'ratings/restaurant_list.html', {'item_list': restaurant_list})