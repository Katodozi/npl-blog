from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('clubs/', views.clubs, name='clubs'),
    path('clubs/<int:club_id>/players/', views.players, name='players'),
    path('blog/', views.blog, name='blog'),
    path('blog/<int:post_id>/', views.post_detail, name='post_detail'),
]

