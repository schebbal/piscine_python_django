from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^accueil', views.home),
	url(r'^connexion/', views.connexion),
	url(r'^inscription/', views.inscription),
	url(r'^logout/', views.logout),
]