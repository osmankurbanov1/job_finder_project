from django.urls import path
from . import views as admin_views

urlpatterns = [
    path('', admin_views.UpdateCompany.as_view(), name='my_company'),
    path('letsstart/', admin_views.show_company_precreate, name='lets_start_company'),
    path('create/', admin_views.AddCompany.as_view(), name='company_create'),
    path('vacancies/', admin_views.VacancyList.as_view(), name='company_vacancies_list'),
    path('vacancies/create/', admin_views.AddVacancy.as_view(), name='company_vacancy_create'),
    path('vacancies/<int:pk>/', admin_views.UpdateVacancy.as_view(), name='company_vacancy_detail')
]
