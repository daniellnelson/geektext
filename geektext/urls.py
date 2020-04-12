from django.contrib import admin
from django.conf import settings # new
from django.urls import path, include # new
from django.conf.urls.static import static # new
from django.conf.urls import url
from django.contrib.auth import views as auth_views

from details import views
from wishlist import views as wishviews
from geekprofile import views as profile_views

from Shopping_cart import views as cart_views

from ratings import views as ratings_views

from details.views import (
    HomeView,
    BookView
)
from Shopping_cart import views as cart_views
from Shopping_cart.views import (
    #CheckoutView,
    CartView,
    OrderSummaryView,
    add_to_cart,
    remove_from_cart
)



urlpatterns = [

    #url(r'^$', views.home, name ='home'),
    #previous url pattern for book details
    url(r'^details/(\d+)/', views.book_detail, name='book_detail'), 

    url(r'^admin/', admin.site.urls),
    #current url pattern for book detials and home

    path('book_detail/<slug>/', BookView.as_view(template_name = 'book_detail.html'), name='book_detail'),
    #url(r'^details/authors/(\d+)/', views.author_books, name='author_books'),

    url(r'^details/review/(\d+)/', ratings_views.review, name = 'write_review'),
    url(r'^details/review/all/(\d+)/', ratings_views.display_reviews, name = 'display_reviews'),

    path('', HomeView.as_view(), name='home'),
    #url(r'^shopping_cart/', cart_views.item_list, name = 'item-list'),
    path('shopping_cart/', CartView.as_view(), name='item-list'),
    path('order-summary/', OrderSummaryView.as_view(), name='order-summary'),
    path('add-to-cart/<slug>/', add_to_cart, name='add-to-cart'),
    path('remove-from-cart/<slug>/', remove_from_cart, name='remove-from-cart'),


    url(r'^login/', auth_views.LoginView.as_view(template_name = 'login.html'), name = 'profile_login'),
    url(r'^logout/', auth_views.LogoutView.as_view(template_name = 'logout.html'), name = 'profile_logout'),
    url(r'^signup/', profile_views.profile_signup, name = 'profile_signup'),
    
    #FIX THESE
    
    url(r'^profile/', profile_views.profile_detail, name = 'profile_detail'),
    url(r'^edit/', profile_views.profile_edit, name = 'profile_edit'),
    url(r'^creditcards/', profile_views.profile_cards, name = 'profile_cards'),
    url(r'^password/', auth_views.PasswordChangeView.as_view(success_url = '/login/',  template_name='profile_password.html'), name = 'profile_password'),
    
    url(r'wishlist/current/(\d+)/', wishviews.current_wish_list, name='current_wish_list'),
    url(r'^wishlist/all/', wishviews.all_wish_list, name='all_wish_list'),
    url(r'^wishlist/create/', wishviews.create_wish_list, name='create_wish_list'),
    url(r'^wishlist/add/(\d+)/', wishviews.add_to_list, name = 'add_to_list'),
    url(r'^wishlist/delete/(\d+)/(\d+)/', wishviews.delete_book, name = 'delete_book'),
    url(r'^wishlist/move/(\d+)/(\d+)/', wishviews.move_book, name = 'move_book'),
    url(r'^wishlist/deletelist/(\d+)/', wishviews.delete_wish_list, name = 'delete_wish_list'),
    url(r'^wishlist/(\d+)/edit/', wishviews.edit_list, name = 'edit_list'),

    

]



if settings.DEBUG: # new
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
