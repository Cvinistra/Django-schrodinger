from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("history/", views.history, name="history"),
    path("plot/", views.plot, name="plot"),
    path("adaptations/", views.adaptations, name="adaptations"),
    path("characters/", views.characters, name="characters"),
    path("characters/<slug:slug>/", views.character, name="character"),
    path("factions/", views.factions, name="factions"),
    path("quotes/", views.quotes, name="quotes"),
    path("gallery/", views.gallery, name="gallery"),
]
