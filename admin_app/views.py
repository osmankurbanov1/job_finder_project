import datetime
from django.http import HttpResponseRedirect
from django.shortcuts import render, reverse
from django.views.generic import ListView, UpdateView, CreateView
from django.contrib.auth.views import LoginView

from rest_framework.generics import CreateAPIView, RetrieveUpdateAPIView
from crum import get_current_user

from vacancy_app.models import Vacancy
from company_app.models import Company
from .forms import AddCompanyForm, AddVacancyForm, UpdateCompanyForm, UpdateVacancyForm
from .forms import RegisterUserForm, LoginForm, AddResumeForm
from .models import Resume
from .serializers import ResumeSerializer
from .permissions import IsAuthenticatedAndHasNotResume, IsAuthenticatedAndHasTheResume

# Create your views here.


class CreateResumeAPIView(CreateAPIView):
    """
    post new Resume
    """

    serializer_class = ResumeSerializer
    permission_classes = (IsAuthenticatedAndHasNotResume, )


class UpdateResumeAPIView(RetrieveUpdateAPIView):
    """
    update the Resume
    """

    queryset = Resume.objects.all()
    serializer_class = ResumeSerializer
    permission_classes = (IsAuthenticatedAndHasTheResume, )


class UpdateResume(UpdateView):
    model = Resume
    form_class = AddResumeForm
    template_name = 'admin_app/my_resume.html'
    success_url = '/myresume'

    def get_object(self, queryset=None):
        try:
            obj = Resume.objects.get(user=get_current_user())
        except Resume.DoesNotExist:
            return None
        return obj


class CreateResume(CreateView):
    form_class = AddResumeForm
    template_name = 'admin_app/resume_create.html'

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.user = self.request.user
        obj.save()
        return HttpResponseRedirect('/myresume/')


class UpdateVacancy(UpdateView, ListView):
    model = Vacancy
    form_class = UpdateVacancyForm
    template_name = 'admin_app/vacancy_update.html'

    def get_success_url(self):
        pk = self.kwargs['pk']
        return reverse("update-vacancy", kwargs={"pk": pk})

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(UpdateVacancy, self).get_context_data(**kwargs)
        context['vacancies'] = Vacancy.objects.all()
        return context


class AddVacancy(CreateView):
    form_class = AddVacancyForm
    template_name = 'admin_app/vacancy_create.html'

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.posted = datetime.date.today()
        obj.company = Company.objects.get(owner=self.request.user)
        obj.save()
        return HttpResponseRedirect('/mycompany/vacancies')


class UpdateCompany(UpdateView):
    model = Company
    form_class = UpdateCompanyForm
    template_name = 'admin_app/my_company.html'
    success_url = '/mycompany'

    def get_object(self, queryset=None):
        try:
            obj = Company.objects.get(owner=get_current_user())
        except Company.DoesNotExist:
            return None
        return obj


class AddCompany(CreateView):
    form_class = AddCompanyForm
    template_name = 'admin_app/company_edit.html'

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.owner = self.request.user
        obj.save()
        return HttpResponseRedirect('/mycompany')


def show_company_precreate(request):
    return render(request, 'admin_app/company_create.html')


def show_resume_precreate(request):
    return render(request, 'admin_app/resume_precreate.html')


class VacancyList(ListView):
    model = Vacancy
    template_name = 'admin_app/vacancy_list.html'
    context_object_name = 'vacancies'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(VacancyList, self).get_context_data(**kwargs)
        try:
            context['company'] = Company.objects.get(owner=self.request.user)
        except Company.DoesNotExist:
            return context
        return context

    def get_queryset(self):
        current_user = self.request.user
        try:
            current_company = Company.objects.get(owner=current_user)
        except Company.DoesNotExist:
            return None
        return Vacancy.objects.filter(company=current_company)


class MyLoginView(LoginView):
    form_class = LoginForm
    template_name = 'admin_app/login.html'


class MySignupView(CreateView):
    form_class = RegisterUserForm
    success_url = 'login'
    template_name = 'admin_app/register.html'
