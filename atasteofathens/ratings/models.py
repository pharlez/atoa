from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=200, unique=True)

    def __unicode__(self):
        return self.name

class User(models.Model):
    username = models.CharField(max_length=200, unique=True)
    first_name = models.CharField('First name', max_length=200)
    last_name = models.CharField('Last name', max_length=200)
    ratings = models.IntegerField('Number of ratings', default=0)

    def __unicode__(self):
        return self.username

class Rating(models.Model):
    item = models.ForeignKey(Item, related_name='i_ratings')
    user = models.ForeignKey(User, related_name='u_ratings')
    rating_value = models.PositiveSmallIntegerField('Rating')

    def __unicode__(self):
        return self.user.username + " has rated '" + self.item.name + "'"
