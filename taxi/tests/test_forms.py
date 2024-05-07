from django.test import TestCase

from taxi.forms import DriverCreationForm, DriverSearchForm


class FormsTest(TestCase):
    def test_driver_creation_form_is_valid(self):
        form_data = {
            "username": "testuser",
            "password1": "testpass",
            "password2": "testpass",
            "first_name": "test",
            "last_name": "test",
            "license_number": "test"
        }
        form = DriverCreationForm(form_data)
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data, form_data)

    def test_driver_search_form_is_valid(self):
        form_data = {"username": "test_model"}
        form = DriverSearchForm(data=form_data)
        self.assertTrue(form.is_valid())
        self.assertTrue("username" in form.fields)
