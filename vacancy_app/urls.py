from django.urls import path
from . import views as vacancy_views

urlpatterns = [
    path('', vacancy_views.VacancyList.as_view()),
    path('<int:pk>/', vacancy_views.VacancyDetail.as_view()),
    path('cat/<str:profession>/', vacancy_views.VacancyByCategoryList.as_view()),
]
