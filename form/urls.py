
from django.urls import path
from .views import contact_view, contact_list, contact_edit, contact_delete

urlpatterns = [
    path('contact/', contact_view, name='contact'),
    path('contactlist/', contact_list, name='contact_list'),
    path('contacts/edit/<int:pk>/', contact_edit, name='contact_edit'),
    path('contacts/delete/<int:pk>/', contact_delete, name='contact_delete'),  
]
