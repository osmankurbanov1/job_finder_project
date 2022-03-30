from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from vacancy_app.models import Specialty, Vacancy
from company_app.models import Company
from .forms import AddApplication

# Create your views here.


class VacancyDetail(DetailView, CreateView):
    model = Vacancy
    template_name = 'vacancy_app/vacancy.html'
    context_object_name = 'vacancy'

    form_class = AddApplication

    def form_valid(self, form):
        obj = form.save(commit=False)
        if self.request.user.is_authenticated:
            obj.user = self.request.user
        obj.vacancy = Vacancy.objects.get(id=self.kwargs['pk'])
        obj.save()
        return HttpResponseRedirect('send')


class SpecialtyHome(ListView):
    model = Specialty
    template_name = 'vacancy_app/index.html'
    context_object_name = 'specialties'

    def get_context_data(self, **kwargs):
        context = super(SpecialtyHome, self).get_context_data(**kwargs)
        context['companies'] = Company.objects.all()
        if self.request.user.is_authenticated:
            try:
                context['company'] = Company.objects.get(owner=self.request.user)
            except Company.DoesNotExist:
                return context
        return context


class VacancyList(ListView):
    model = Vacancy
    template_name = 'vacancy_app/vacancies.html'
    context_object_name = 'vacancies'


class VacancyByCategoryList(ListView):
    model = Vacancy
    template_name = 'vacancy_app/vacancies_by_cat.html'
    context_object_name = 'vacancies'

    def get_context_data(self, **kwargs):
        context = super(VacancyByCategoryList, self).get_context_data(**kwargs)
        profession_param = self.kwargs['profession']
        context['profession_param'] = profession_param
        context['vacancy_counter'] = Vacancy.objects.filter(specialty__code=profession_param).count()
        return context


def sent(request, pk):
    return render(request, 'vacancy_app/sent.html', context={'pk': pk})
