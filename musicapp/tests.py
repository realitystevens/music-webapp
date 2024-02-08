from django.test import TestCase
from django.urls import reverse
from .models import Artiste, Song, Lyric



class ArtisteTest(TestCase):
    def setUp(self):
        self.artiste = Artiste.objects.create(first_name='Test First Name')

    def test_model_name(self):
        self.assertEqual(self.artiste.first_name, 'Test First Name')

