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

from Shopping_cart import views as cart_views




urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.home, name ='home'),
    url(r'^details/(\d+)/', views.book_detail, name='book_detail'),
    url(r'^wishlist/', wishviews.wish_list, name='wish_list'),
    url(r'^login/', auth_views.LoginView.as_view(template_name = 'login.html'), name = 'profile_login'),
    url(r'^logout/', auth_views.LogoutView.as_view(template_name = 'logout.html'), name = 'profile_logout'),
    url(r'^signup/', profile_views.profile_signup, name = 'profile_signup'),
    url(r'^profile/', profile_views.profile_detail, name = 'profile_detail'),
    url(r'^edit/', profile_views.profile_edit, name = 'profile_edit'),
    url(r'^creditcards/', profile_views.profile_cards, name = 'profile_cards'),
    url(r'^password/', auth_views.PasswordChangeView.as_view(success_url = '/login/',  template_name='profile_password.html'), name = 'profile_password'),
    url(r'^shopping_cart/', cart_views.item_list, name = 'item-list'),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='login.html')),
    #path('', include('Shopping_cart.urls'), namespace='cart')
]




if settings.DEBUG: # new
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
