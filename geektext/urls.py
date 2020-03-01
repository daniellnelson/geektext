from django.contrib import admin
from django.conf import settings # new
from django.urls import path, include # new
from django.conf.urls.static import static # new
from django.conf.urls import url

from details import views
from ratings import views as ratings_views
from wishlist import views as wishviews
from geekprofile import views as profile_views
from django.urls import path, include

from Shopping_cart import views as cart_views




urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.home, name ='home'),
    url(r'^details/(\d+)/', views.book_detail, name='book_detail'),
    url(r'^wishlist/', wishviews.wish_list, name='wish_list'),
    url(r'^profile/', profile_views.profile_detail, name = 'profile_detail'),
    url(r'^shopping_cart/', cart_views.item_list, name = 'item-list'),
    url(r'^ratings/display/', ratings_views.display_comment, name='display_comment'),
    url(r'^ratings/write/', ratings_views.write_comment, name='write_comment'),
    url(r'^ratings/rate/(\d+)/', ratings_views.rate_book, name='rate_book'),
    #path('', include('Shopping_cart.urls'), namespace='cart')
]




if settings.DEBUG: # new
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
