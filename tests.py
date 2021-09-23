from unittest import signals
from django.http import response
from django.test import TestCase
from django.test.testcases import SimpleTestCase

# Create your tests here.

class TestNotString(SimpleTestCase):
    def test_not_string(self):
        response = self.client.get("/not-string/x")
        self.assertContains(response, "not x")

class TestMakeAbba(SimpleTestCase):
    def test_make_abba(self):
        response = self.client.get("/make-abba/a/b")
        self.assertContains(response, "abba")

class TestCloseFar(SimpleTestCase):
    def test_close_far(self):
        response = self.client.get("/close-far/4/1/3")
        self.assertContains(response, True)
