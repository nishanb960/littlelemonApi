from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from . import views

router = DefaultRouter()
router.register(
    r'bookings',
    views.BookingViewSet,
    basename='booking'
)

urlpatterns = [
    #homepage
    path('', views.home, name='home'),
    path('home/', views.home, name='home-page'),
    
    #Menu API
    path('api/menu-items/', views.MenuItemsView.as_view(), name='menu-items'),
    
    #single view
    path('api/menu-items/<int:pk>/', views.SingleMenuItemsView.as_view(), name='single-menu-item'),
    
    #Booking Api
    path('api/', include(router.urls)),
    
    #protected Api
    path('api/message/', views.msg , name='message'),
    
    #token
    path('api-token-auth/', obtain_auth_token, name='api-token-auth'),
    
]
