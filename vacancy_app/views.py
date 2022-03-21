from django.views.generic import ListView, DetailView
from vacancy_app.models import Specialty, Vacancy
from company_app.models import Company
# Create your views here.


class VacancyDetail(DetailView):
    model = Vacancy
    template_name = 'vacancy_app/vacancy.html'
    context_object_name = 'vacancy'


class SpecialtyHome(ListView):
    model = Specialty
    template_name = 'vacancy_app/index.html'
    context_object_name = 'specialties'

    def get_context_data(self, **kwargs):
        context = super(SpecialtyHome, self).get_context_data(**kwargs)
        context['companies'] = Company.objects.all()
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
