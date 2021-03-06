"""job_finder URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LogoutView

from vacancy_app import views as vacancy_views
from company_app import views as company_views
from admin_app import views as admin_views
from .yasg import urlpatterns as doc_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', vacancy_views.SpecialtyHome.as_view(), name='index'),
    path('search/', vacancy_views.VacancySearch.as_view(), name='vacancy_search'),
    path('companies/<int:id>', company_views.CompanyDetail.as_view(), name='company_detail'),
    path('vacancies/', include('vacancy_app.urls')),
    path('mycompany/', include('admin_app.my_company_urls')),
    path('myresume/', include('admin_app.my_resume_urls')),
]

# Authoritation routs

urlpatterns += [
    path('login', admin_views.MyLoginView.as_view(), name='login'),
    path('register', admin_views.MySignupView.as_view(), name='register'),
    path('logout', LogoutView.as_view(), name='logout'),
]

# API

urlpatterns += [
    path('api/v1/', include('api.urls')),
]

urlpatterns += doc_urls

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
