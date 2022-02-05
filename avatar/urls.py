from django.urls import path

from avatar import views

urlpatterns = [
    path(r'add/', views.add, name='avatar_add'),
    path(r'change/', views.change, name='avatar_change'),
    path(r'delete/', views.delete, name='avatar_delete'),
    path(r'render_primary/<slug:user>/<int:size>/',
         views.render_primary,
         name='avatar_render_primary'),
]
