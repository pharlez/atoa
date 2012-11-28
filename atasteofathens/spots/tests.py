from django.test import TestCase
import mongoengine
from atasteofathens.spots.models import Spot

mongoengine.connect('unit-tests')

class SpotModelTest(TestCase):
    def test_creating_a_new_spot_and_saving_it_to_the_database(self):
        # start by creating a new Spot object with its "name" set
        spot = Spot()
        spot.name = "The Diner"
        spot.address = "25 Curtain Rd."

        # check we can save it to the database
        spot.save()

        # now check we can find in in the database again
        all_spots_in_database = Spot.objects.all()
        self.assertEquals(len(all_spots_in_database), 1)
        only_spot_in_database = all_spots_in_database[0]
        self.assertEquals(only_spot_in_database, spot)

        # and check that it has saved it's two attributes: name and address
        self.assertEquals(only_spot_in_database.name, "The Diner")
        self.assertEquals(only_spot_in_database.address, spot.address)
