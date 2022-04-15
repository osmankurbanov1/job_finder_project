import datetime
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic import ListView, DetailView, CreateView
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView, RetrieveAPIView, \
    CreateAPIView

from vacancy_app.models import Specialty, Vacancy
from company_app.models import Company
from .forms import AddApplication
from .permissions import UserHasCompanyOrReadOnly, IsVacancyOwnerOrReadOnly, IsCompanyOwner
from .serializers import VacancySerializer, SpecialtySerializer, ApplicationSerializer, VacancyRelatedCompanySerializer

# Create your views here.


class ApplicationCreateAPIView(CreateAPIView):
    """
    post new Application to a vacancy
    """

    serializer_class = ApplicationSerializer

    def perform_create(self, serializer):
        if self.request.user:
            serializer.save(user_id=self.request.user.id)


class VacancyRelatedCompanyList(ListAPIView):
    """
    get Vacancies related the Company
    """

    serializer_class = VacancyRelatedCompanySerializer
    permission_classes = (IsCompanyOwner, )

    def get_queryset(self):
        return Vacancy.objects.filter(company=Company.objects.get(name=self.kwargs.get('company')))


class VacancyListCreateAPIView(ListCreateAPIView):
    """
    get all Vacancies
    post new Vacancy
    """
    queryset = Vacancy.objects.all()
    serializer_class = VacancySerializer
    permission_classes = (UserHasCompanyOrReadOnly, )

    def perform_create(self, serializer):
        serializer.save(company_id=self.request.user.companies.pk, posted=datetime.date.today())


class VacancyDetailAPIView(RetrieveUpdateDestroyAPIView):
    """
    read / update / delete Vacancy
    """
    queryset = Vacancy.objects.all()
    serializer_class = VacancySerializer
    permission_classes = (IsVacancyOwnerOrReadOnly, )


class SpecialtyListAPIView(ListAPIView):
    queryset = Specialty.objects.all()
    serializer_class = SpecialtySerializer


class SpecialtyDetailAPIView(RetrieveAPIView):
    queryset = Specialty.objects.all()
    serializer_class = SpecialtySerializer


class VacancySearch(ListView):
    model = Vacancy
    template_name = 'vacancy_app/search_results.html'
    context_object_name = 'vacancies'

    def get_queryset(self):
        return Vacancy.objects.filter(title__icontains=self.request.GET.get("q"))


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
