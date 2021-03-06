from django.urls import path


from . import views

app_name = 'ncas'
urlpatterns = [
    path('home/', views.home, name='home'),
    path('mark-create/<pk>', views.mark_update, name='markcreate'),
    path('user-create/', views.user_create, name='usercreate'),
    path('student-create/<int:pk>/', views.student_create, name='studentcreate'),
    path('studentlist/', views.studentlist, name='studentlist'),
    path('studentdetail/<int:pk>/', views.StudentDetail.as_view(), name='studentdetail'),
]
