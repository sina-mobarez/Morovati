from .views import PermiumAccountListCreateView, PermiumAccountRetrieveUpdateDelete
from django.urls import path





urlpatterns = [
    
    path("permium-account/",PermiumAccountListCreateView.as_view(),name="all-permium-ac"),
    path("permium-account/me/",PermiumAccountRetrieveUpdateDelete.as_view(), name='permium'),


]