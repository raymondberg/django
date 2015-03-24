__author__ = 'rberg'
import unittest
from django.test import TestCase
from partymaker.models import Neighborhood, Animal, AnimalRating


class AnimalTestCase(TestCase):
    def setUp(self):
        self.animal1 = Animal(first_name="Alfred", last_name="Aardvark")
        self.animal2 = Animal(first_name="Laura", last_name="Lion")
        self.animal3 = Animal(first_name="Carla", last_name="Crane")
        self.animal1.save()
        self.animal2.save()
        self.animal3.save()

    def tearDown(self):
        self.animal1.delete()
        self.animal2.delete()
        self.animal3.delete()

class TestRateBrook(AnimalTestCase):
    def test_add_and_deleterating(self):
        self.animal1.rate(self.animal2, 1, 0)
        self.assertEqual(AnimalRating.objects.all().count(), 1)
        self.animal1.clear_rating(self.animal2)
        self.assertEqual(AnimalRating.objects.all().count(), 0)

    @unittest.skip("not supported yet")
    def test_addinvalidlikingrating(self):
        self.animal1.rate(self.animal2, 11, 1)
        self.assertEqual(AnimalRating.objects.all().count(), 0)
    @unittest.skip("not supported yet")
    def test_addinvalidtagalongrating(self):
        self.animal3.rate(self.animal2, 1, 12)
        self.assertEqual(AnimalRating.objects.all().count(), 0)

