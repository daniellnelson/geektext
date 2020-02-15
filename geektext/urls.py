from django.contrib import admin
from django.conf import settings # new
from django.urls import path, include # new
from django.conf.urls.static import static # new
from django.conf.urls import url

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
    url(r'^profile/', profile_views.profile_detail, name = 'profile_detail'),
]


# Cart Urls
urlpatterns += [
    path('cart/', cart_views.ListCart, name='list-carts'),
    path('cart/<int:pk>/', cart_views.DetailCart.as_view(), name='detail-cart'),
    path('cart/create/', cart_views.CreateCart.as_view(), name='create-cart'),
    path('cart/<int:pk>/update/', cart_views.Updatecart.as_view(), name='update-cart'),
    path('cart/<int:pk>/delete/', cart_views.DeleteCart.as_view(), name='delete-cart'), 
]

if settings.DEBUG: # new
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
