from django.urls import path, include
from myapp import views

urlpatterns = [
    path('', views.homeViews, name='home'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('about/', views.about, name='about'),
    path('administrator/', views.administratorView),
    path('gallery/', views.gallery, name='gallery'),
    path('gallery_edit/', views.gallery_edit, name='gallery_edit'),
    path('delete/<int:id>/', views.delete_gallery_view, name='delete'),
    path('update/<int:id>/', views.update_gallery_view, name='update'),
    path('news/', views.news, name='news'),
    path('events/', views.event_views.as_view(), name='events'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.logout_views, name='logout'),
    path('search/', views.search_views, name='search')
]