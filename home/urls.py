from django.urls import path
from . import views
# defining the url page
urlpatterns = [
    path('', views.home, name='home'),
]