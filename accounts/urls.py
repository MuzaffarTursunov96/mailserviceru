from django.urls import path
from . import views


urlpatterns =[
  path('customers-list/',views.ListCustomers.as_view(),name='list_customer'),
  path('customer-get/<pk>',views.DetailCustomers.as_view(),name='detail_customer'),
  path('customer-create/',views.CreateCustomers.as_view(),name='add_customer'),
  path('customer-update/<pk>',views.UpdateCustomers.as_view(),name='update_customer'),
  path('customer-delete/<pk>',views.DeleteCustomers.as_view(),name='delete_customer'),
  path('my-profile/<int:pk>',views.my_profile,name='my_profile'),

]