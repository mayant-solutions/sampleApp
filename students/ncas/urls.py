from django.urls import path, include

from . import views

urlpatterns = [
    path('Students/', views.StdView.as_view(), name='std'),
    path('Course/', views.CoursView.as_view(), name='course'),
    path('<int:pk>/', views.CoursDView.as_view(), name='coursed'),
    path('<int:pk>/', views.StdDView.as_view(), name='stdd'),
    path('accounts/', include('django.contrib.auth.urls'), name='login'),
]