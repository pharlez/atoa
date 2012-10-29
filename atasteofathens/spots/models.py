from django.db import models
from django.contrib.auth.models import User as AuthUser
from tools import unique_slugify

class Neighbourhood(models.Model):
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        ordering = ['name']

    def __unicode__(self):
        return self.name

class Place(models.Model):
    address = models.CharField(max_length=200)
    neighbourhood = models.ForeignKey(Neighbourhood)

    class Meta:
        abstract = True

class RestaurantCat(models.Model):
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        ordering = ['name']

    def __unicode__(self):
        return self.name

class Restaurant(Place):
    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=20, blank=True)
    category = models.ForeignKey(RestaurantCat)
    PRICE_RANGES = (
            (1, '$'),
            (2, '$$'),
            (3, '$$$'),
            (4, '$$$$'),
            (5, '$$$$$'),
    )
    price = models.PositiveSmallIntegerField(choices=PRICE_RANGES, null=True, blank=True)
    # hours
    # attire
    good_for_groups = models.BooleanField(blank=True)
    takes_reservations =  models.BooleanField(blank=True)
    delivery = models.BooleanField(blank=True)
    take_out = models.BooleanField(blank=True)
    wi_fi = models.BooleanField(blank=True)
    # goodfor
    NOISE_RANGES = (
            (1, 'low'),
            (2, 'average'),
            (3, 'high'),
    )
    noise_level = models.PositiveSmallIntegerField(choices=NOISE_RANGES, blank=True, null=True)
    # ambience
    wheelchair = models.BooleanField(blank=True)
    # create slug for urls
    slug = models.SlugField(blank=True, db_index=True)

    class Meta:
        ordering = ['name']

    def save(self, **kwargs):
        slug_str = "%s" % (self.name)
        unique_slugify(self, slug_str)
        super(Restaurant, self).save()

    def __unicode__(self):
        return self.name

class Rating(models.Model):
    restaurant = models.ForeignKey(Restaurant, related_name='r_ratings')
    user = models.ForeignKey(AuthUser, related_name='u_ratings')
    rating_value = models.PositiveSmallIntegerField('Rating')

    def __unicode__(self):
        return self.user.username + " has rated '" + self.restaurant.name + "'"
