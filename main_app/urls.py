from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('menu/', views.menu, name='menu'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('covers/', views.covers, name='covers'),
    path('covers/<int:cover_id>/', views.cover_detail, name='cover_detail'),
    path('covers/new', views.cover_new, name='cover_new'),
    path('covers/<int:cover_id>/close', views.cover_close, name='cover_close')
]
# Account URLS
# accounts/login/ [name='login']
# accounts/logout/ [name='logout']
# accounts/password_change/ [name='password_change']
# accounts/password_change/done/ [name='password_change_done']
# accounts/password_reset/ [name='password_reset']
# accounts/password_reset/done/ [name='password_reset_done']
# accounts/reset/<uidb64>/<token>/ [name='password_reset_confirm']
# accounts/reset/done/ [name='password_reset_complete']