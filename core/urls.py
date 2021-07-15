from django.urls import path,include
from .pages import Index
from .views import Verify


urlpatterns = [
    path('',Index.as_view(),name='index'),
    path('verify/',Verify.as_view(),name = 'verify')
]