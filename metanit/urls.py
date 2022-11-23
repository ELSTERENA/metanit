from django.urls import path

from URL import views

urlpatterns = [
    path('', views.ListContactView.as_view(), name='Contacts_List'),
    path('home/', views.index, name='home')
]

