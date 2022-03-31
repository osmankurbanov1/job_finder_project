from django.urls import path
from . import views as admin_views

urlpatterns = [
    path('', admin_views.UpdateResume.as_view(), name='my_resume'),
    path('letsstart/', admin_views.show_resume_precreate, name='resume_lets_start'),
    path('create/', admin_views.CreateResume.as_view(), name='create_resume'),
]
