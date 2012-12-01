from django.db import models
from django.contrib.auth.models import User as AuthUser
from tools import unique_slugify

from mongoengine import *
from mongoengine_extras.fields import AutoSlugField

class Spot(Document):
    name = StringField(max_length=200, required=True)
    address = StringField(max_length=200)
    neighbourhood = StringField(max_length=200)
    phone = StringField(max_length=20)
    website = StringField(max_length=200)
    """
    PRICE_RANGES = (
            (1, '$'),
            (2, '$$'),
            (3, '$$$'),
            (4, '$$$$'),
            (5, '$$$$$'),
    )
    price = IntField(choices=PRICE_RANGES)
    wi_fi = BooleanField()
    credit_card = BooleanField()
    wheelchair = BooleanField()
    tv = BooleanField()
    smoking = BooleanField()
    NOISE_RANGES = (
            (1, 'low'),
            (2, 'average'),
            (3, 'high'),
    )
    noise_level = IntField(choices=NOISE_RANGES)
    ATTIRE_RANGES = (
            (1, 'casual'),
            (2, 'smart'),
            (3, 'formal'),
    )
    attire = IntField(choices=ATTIRE_RANGES)
    waiter_service = BooleanField()
    live_music = BooleanField()
    group_friendly = BooleanField()
    date_friendly = BooleanField()
    reservations = BooleanField()
    slug = AutoSlugField(populate_from='name')
    """
    # music?
    # location?

#class Details(EmbeddedDocument):
    # food details
   # category = StringField(max_length=100)
   # delivery = BooleanField()
    #take_out = BooleanField()
    ## alcohol?
    ## hours?

    # bar details

    # coffee details

    # club details

"""
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
