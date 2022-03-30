from django.urls import path
from . import views as vacancy_views

urlpatterns = [
    path('', vacancy_views.VacancyList.as_view(), name='vacancies_list'),
    path('<int:pk>/', vacancy_views.VacancyDetail.as_view(), name='vacancy_detail'),
    path('<int:pk>/send/', vacancy_views.sent),
    path('cat/<str:profession>/', vacancy_views.VacancyByCategoryList.as_view(), name='vacancy_category'),
]
