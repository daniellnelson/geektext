from django.contrib import admin
from django.conf import settings # new
from django.urls import path, include # new
from django.conf.urls.static import static # new
from django.conf.urls import url
from django.contrib.auth import views as auth_views

from details import views
from wishlist import views as wishviews
from geekprofile import views as profile_views
from django.urls import path, include

from details.views import (
    HomeView,
    BookView
)
from Shopping_cart import views as cart_views




urlpatterns = [
    url(r'^admin/', admin.site.urls),
    #url(r'^$', views.home, name ='home'),
    path('', HomeView.as_view(), name='home'),
    #previous url pattern for book details
    #url(r'^details/(\d+)/', views.book_detail, name='book_detail'), 

    #current url pattern for book detials
    path('book_details/<slug>/', BookView.as_view(), name='book_detail'),
    
    url(r'^login/', auth_views.LoginView.as_view(template_name = 'login.html'), name = 'profile_login'),
    url(r'^logout/', auth_views.LogoutView.as_view(template_name = 'logout.html'), name = 'profile_logout'),
    url(r'^signup/', profile_views.profile_signup, name = 'profile_signup'),
    url(r'^wishlist/all/', wishviews.all_wish_list, name='all_wish_list'),
    url(r'^wishlist/create/', wishviews.create_wish_list, name='create_wish_list'),
    url(r'wishlist/current/(\d+)/', wishviews.current_wish_list, name='current_wish_list'),
    url(r'^profile/', profile_views.profile_detail, name = 'profile_detail'),
    url(r'^shopping_cart/', cart_views.item_list, name = 'item-list'),
    #path('checkout/', CheckoutView.as_view(), name='checkout'),

    #path('add-to-cart/<slug>/', add_to_cart, name='add-to-cart') use once add_to_cart is implemented
]



if settings.DEBUG: # new
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
