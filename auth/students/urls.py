from django.urls import path
from . import views, views_api

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:id>', views.view_student, name='view_student'),
    path('add/', views.add, name='add'),
    path('edit/<int:id>/', views.edit, name='edit'),
    path('delete/<int:id>/', views.delete, name='delete'),
    path('student', views_api.getData.as_view(), name='data_get'),
    path('student/push', views_api.inputData.as_view(), name='data_input'),
    path('student/delete/<str:student_number>', views_api.deleteData.as_view(), name='data_delete'),
    path('student/edit/<str:student_number>', views_api.editData.as_view(), name='data_edit'),
]