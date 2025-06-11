from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('create_task', views.create_task, name='create_task'),
    path('delete/<int:id>', views.delete_task),
    path('update/<int:id>', views.update_task),
    path('task_check_ok/<int:id>', views.task_check_ok),
    path('task_check_no/<int:id>', views.task_check_no),
    path('task_filter/<str:type>', views.task_filter),
    path('category', views.category, name='category'),
    path('create_category', views.create_category, name='create_category'),
    path('deleteCategory/<int:id>', views.delete_category, name='delete_category')
    
   
]