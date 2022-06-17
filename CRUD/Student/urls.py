from django.urls import path
from . import views

urlpatterns = [
    path('',views.add_data , name='add_data'),
    path('delete/<int:id>', views.delete_data, name='delete_data'),
    path('edit_data/<int:id>', views.edit_data, name='edit_data'),
]
