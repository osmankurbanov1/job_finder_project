from django.urls import path
from . import views

urlpatterns = [
    path('vacancies/', views.VacancyListCreateAPIView.as_view()),
    path('vacancies/<int:pk>/', views.VacancyDetailAPIView.as_view()),
    path('vacancies/<str:company>/', views.VacancyRelatedCompanyList.as_view()),
    path('specialties/', views.SpecialtyListAPIView.as_view()),
    path('specialties/<int:pk>/', views.SpecialtyDetailAPIView.as_view()),
    path('companies/', views.CompanyListCreateAPIView.as_view()),
    path('companies/<int:pk>/', views.CompanyDetailAPIView.as_view()),
    path('applications/', views.ApplicationCreateAPIView.as_view()),
    path('resumes/', views.CreateResumeAPIView.as_view()),
    path('resumes/<int:pk>/', views.UpdateResumeAPIView.as_view()),
]
