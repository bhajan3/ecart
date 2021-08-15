from django.urls import path
from . import views


urlpatterns = [
    path('product_list/', views.product_list, name = 'product_list'),
    path('<int:id>/', views.product_detail, name = 'product_detail'),

    path('eproduct_list/', views.eproduct_list, name = 'eproduct_list'),
    path('elec/<int:id>', views.electronic_detail, name = 'electronic_detail'),

    path('babycloth/', views.babycloth, name = 'babycloth'),
    path('bab/<int:id>', views.babycloth_detail, name = 'babycloth_detail'),

    path('checkout/', views.checkout, name='checkout'),

    path('reviews/', views.reviews, name='reviews'),



]
