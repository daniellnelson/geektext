from django.contrib import admin
from django.conf import settings # new
from django.urls import path, include # new
from django.conf.urls.static import static # new
from django.conf.urls import url

from details import views
<<<<<<< HEAD
from wishlist import views as wishviews
=======
from geekprofile import views as profile_views
>>>>>>> a7306b9225fd11c26a900276e6720b2f511d1058

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.home, name ='home'),
    url(r'^details/(\d+)/', views.book_detail, name='book_detail'),
<<<<<<< HEAD
    url(r'^wishlist/', wishviews.wish_list, name='wish_list'),
=======
    url(r'^profile/', profile_views.profile_detail, name = 'profile_detail'),
>>>>>>> a7306b9225fd11c26a900276e6720b2f511d1058
]

if settings.DEBUG: # new
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
