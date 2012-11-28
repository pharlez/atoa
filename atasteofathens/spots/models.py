from django.db import models
from django.contrib.auth.models import User as AuthUser
from tools import unique_slugify

from mongoengine import *
from mongoengine_extras.fields import AutoSlugField
"""
class Neighbourhood(models.Model):
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        ordering = ['name']

    def __unicode__(self):
        return self.name
"""
class Spot(Document):
    name = StringField(max_length=200, required=True)
    address = StringField(max_length=200)
    slug = AutoSlugField(populate_from='name')

   # neighbourhood = models.ForeignKey(Neighbourhood)
  #  phone = models.CharField(max_length=20, blank=True)

  #  class Meta:
  #      abstract = True
"""
class EatCategory(models.Model):
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        ordering = ['name']

    def __unicode__(self):
        return self.name

class Restaurant(Place):
    name = models.CharField(max_length=200)
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
    ATTIRE_RANGES = (
            (1, 'casual'),
            (2, 'smart'),
            (3, 'formal'),
    )
    attire = models.PositiveSmallIntegerField(choices=ATTIRE_RANGES, null=True, blank=True)
    group_friendly = models.BooleanField(blank=True)
    date_friendly = models.BooleanField(blank=True)
    reservations =  models.BooleanField(blank=True)
    delivery = models.BooleanField(blank=True)
    waiter_service = models.BooleanField(blank=True)
    take_out = models.BooleanField(blank=True)
    wi_fi = models.BooleanField(blank=True)
    credit_card = models.BooleanField(blank=True)
    tv = models.BooleanField(blank=True)
    smoking = models.BooleanField(blank=True)
    # alcohol
    # music
    NOISE_RANGES = (
            (1, 'low'),
            (2, 'average'),
            (3, 'high'),
    )
    noise_level = models.PositiveSmallIntegerField(choices=NOISE_RANGES, blank=True, null=True)
    wheelchair = models.BooleanField(blank=True)
    website = models.CharField(max_length=100)
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

class DrinkCategory(models.Model):
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        ordering = ['name']

    def __unicode__(self):
        return self.name

class Drink(Place):
    name = models.CharField(max_length=200)
    category = models.ForeignKey(DrinkCategory)
    PRICE_RANGES = (
            (1, '$'),
            (2, '$$'),
            (3, '$$$'),
            (4, '$$$$'),
            (5, '$$$$$'),
    )
    price = models.PositiveSmallIntegerField(choices=PRICE_RANGES, null=True, blank=True)
    # hours
    ATTIRE_RANGES = (
            (1, 'casual'),
            (2, 'smart'),
            (3, 'formal'),
    )
    attire = models.PositiveSmallIntegerField(choices=ATTIRE_RANGES, null=True, blank=True)
    group_friendly = models.BooleanField(blank=True)
    date_friendly = models.BooleanField(blank=True)
    reservations =  models.BooleanField(blank=True)
    delivery = models.BooleanField(blank=True)
    waiter_service = models.BooleanField(blank=True)
    take_out = models.BooleanField(blank=True)
    wi_fi = models.BooleanField(blank=True)
    credit_card = models.BooleanField(blank=True)
    tv = models.BooleanField(blank=True)
    smoking = models.BooleanField(blank=True)
    # alcohol
    # music
    NOISE_RANGES = (
            (1, 'low'),
            (2, 'average'),
            (3, 'high'),
    )
    noise_level = models.PositiveSmallIntegerField(choices=NOISE_RANGES, blank=True, null=True)
    wheelchair = models.BooleanField(blank=True)
    website = models.CharField(max_length=100)
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
    RATING_RANGES = (
            (0, 'bad'),
            (1, 'OK'),
            (2, 'good'),
    )
    rating_value = models.PositiveSmallIntegerField('Rating', choices=RATING_RANGES)
    #rating_time = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.user.username + " has rated '" + self.restaurant.name + "'"
"""
