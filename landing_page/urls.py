from django.urls import path, include
from . import views as vi 


urlpatterns = [
    path('home',vi.LandingPage.as_view(), name='home')
]

