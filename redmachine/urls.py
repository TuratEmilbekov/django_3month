from django.urls import path
from . import views

urlpatterns = [
    path('cars/', views.CarListView.as_view(), name='car_view'),
    path('cars/<int:id>/', views.CarDetailView.as_view(), name='car_detail_view'),
    path('cars/<int:id>/update/', views.CarUpdateView.as_view(), name='car_update_view'),
    path('cars/<int:id>/delete/', views.CarDeleteView.as_view(), name='car_delete_view'),
    path('add-car/', views.CarCreateView.as_view(), name='add_car_view'),
]