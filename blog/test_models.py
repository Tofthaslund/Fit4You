from django.test import TestCase
from .models import Blog

class TestModels(TestCase):

    def test_string_representation(self):
        """ Ensure that a blog entry string
        representation is equal to its title"""
        entry = Blog(title='My entry title')
        self.assertEqual(str(entry), entry.title)
