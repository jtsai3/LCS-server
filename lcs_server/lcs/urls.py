from django.urls import path
from .views import LongestCommonSubstringView
urlpatterns = [
    path('lcs', LongestCommonSubstringView.as_view(), name='lcs'),
]
