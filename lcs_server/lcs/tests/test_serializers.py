from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import serializers

from lcs.serializers import SetOfStringSerializer

class SetOfStringSerializerTest(TestCase):
    def setUp(self):
        self.serializer = SetOfStringSerializer()
        
    def test_empty_set_raise_validation_error(self):
        """Test that the serializer raises a validation error if the setOfStrings is empty."""
        payload = {'setOfStrings': []}
        serializer = SetOfStringSerializer(data=payload)
        with self.assertRaises(serializers.ValidationError):
            serializer.is_valid(raise_exception=True)
            
    def test_invalid_type_raise_validation_error(self):
        """Test that the serializer raises a validation error if the setOfStrings is not a list of dictionaries."""
        payload = {'setOfStrings': ['a', 'b']}
        serializer = SetOfStringSerializer(data=payload)
        with self.assertRaises(serializers.ValidationError):
            serializer.is_valid(raise_exception=True)
            
    def test_invalid_key_name_raise_validation_error(self):
        payload = {'setOfStrings': [{'bad_key': 'a'}, {'bad_key': 'ab'}]}
        serializer = SetOfStringSerializer(data=payload)
        with self.assertRaises(serializers.ValidationError):
            serializer.is_valid(raise_exception=True)
            
    def test_non_set_raise_validation_error(self):
        """Test that the serializer raises a validation error if the setOfStrings is not a set."""
        payload = {'setOfStrings': [{'value': 'a'}, {'value': 'a'}]}
        serializer = SetOfStringSerializer(data=payload)
        with self.assertRaises(serializers.ValidationError):
            serializer.is_valid(raise_exception=True)
            
    def test_valid_set_returns_is_valid(self):
        """Test that the serializer is valid for a valid set of strings."""
        payload = {'setOfStrings': [{'value': 'comcast'}, {'value': 'comcastic'}, {'value': 'broadcaster'}]}
        serializer = SetOfStringSerializer(data=payload)
        self.assertTrue(serializer.is_valid())