from django.urls import path
from . import views
urlpatterns=[
 path("",views.home,name="home"),
 path("character/",views.character,name="character"),
 path("abilities/",views.abilities,name="abilities"),
 path("quotes/",views.quotes,name="quotes"),
 path("gallery/",views.gallery,name="gallery"),
]
