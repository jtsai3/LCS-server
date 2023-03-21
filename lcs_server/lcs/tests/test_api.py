from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status

class LongestCommonSubstringTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.lcs_url = reverse('lcs')

    def test_lcs_with_empty_set_should_return_bad_request(self):
        """Test that the API returns a 400 error if the setOfStrings is empty."""
        payload = {'setOfStrings': []}
        response = self.client.post(self.lcs_url, payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_lcs_with_invalid_type_should_return_bad_request(self):
        """Test that the API returns a 400 error if the setOfStrings is not a list of dictionaries."""
        payload = {'setOfStrings': ['a', 'b']}
        response = self.client.post(self.lcs_url, payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_lcs_non_set_should_return_bad_request(self):
        """Test that the API returns a 400 error if the setOfStrings is not a set."""
        payload = {'setOfStrings': [{'value': 'a'}, {'value': 'a'}]}
        response = self.client.post(self.lcs_url, payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_lcs_with_empty_set_should_return_empty_lcs(self):
        """Test that the API returns an empty list if there is no LCS."""
        payload = {'setOfStrings': [{'value': 'a'}, {'value': 'b'}, {'value': 'c'}]}
        expected = {'lcs': []}
        response = self.client.post(self.lcs_url, payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, expected)

    def test_lcs_with_valid_set_should_return_correct_lcs(self):
        """Test that the API returns the correct LCS for a valid set of strings."""
        payload = {'setOfStrings': [{'value': 'comcast'}, {'value': 'comcastic'}, {'value': 'broadcaster'}]}
        expected = {'lcs': [{'value': 'cast'}]}
        response = self.client.post(self.lcs_url, payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, expected)

    def test_lcs_with_multiple_lcs(self):
        """Test that the API returns all LCSs if there are multiple."""
        payload = {'setOfStrings': [{'value': 'cdab'}, {'value': 'abyycd'}, {'value': 'xabxxxcd'}]}
        expected = {'lcs': [{'value': 'ab'}, {'value': 'cd'}]}
        response = self.client.post(self.lcs_url, payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, expected)