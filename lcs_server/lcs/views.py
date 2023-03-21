from django.shortcuts import render
from django.urls import reverse
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.test import APIClient
from rest_framework.views import APIView
from typing import List

from .serializers import SetOfStringSerializer

class LongestCommonSubstringView(APIView):
    serializer_class = SetOfStringSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        setOfStrings = [d['value'] for d in serializer.validated_data['setOfStrings']]

        # compute LCS
        lcs = self.compute_lcs(setOfStrings)
        response = {'lcs': lcs}

        return Response(response, status=status.HTTP_200_OK)
    
    def compute_lcs(self, setOfStrings: List[str]) -> List[dict]:
        """ Returns the longest common substring in the format:
            [
                {'value': 'substring1'},
                {'value': 'substring2'}
            ]
            
            If there is only one string in setOfStrings, the longest common substring is itself.
        """
        def format_substring(substring: str) -> dict:
            return {'value': substring}
        
        longest_substrings = []
        if not setOfStrings:
            return longest_substrings
        
        # Get the shortest string in the list
        shortest_string = min(setOfStrings, key=len)
        
        # Iterate over all possible substrings of the shortest string in the list
        for start in range(len(shortest_string)):
            for end in range(start+1, len(shortest_string)+1):
                substring = shortest_string[start:end]
                
                # Check if the current substring appears in all strings in the list
                is_common_substring = all(substring in s for s in setOfStrings)
                if not is_common_substring:
                    continue
                # If the current substring is longer than the current longest one
                # update the longest substring list
                if not longest_substrings or len(substring) > len(longest_substrings[0]):
                    longest_substrings = [substring]
                elif len(substring) == len(longest_substrings[0]) and substring not in longest_substrings:
                    longest_substrings.append(substring)
        
        # Sort the list of longest substrings in alphabetical order
        longest_substrings = [format_substring(substring) for substring in longest_substrings]
        longest_substrings.sort(key=lambda x: x['value'])
        return longest_substrings
    