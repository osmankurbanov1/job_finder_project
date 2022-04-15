from django.views.generic import ListView
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView

from vacancy_app.models import Vacancy
from .permissions import IsAuthenticatedAndHaveNotCompanyOrReadOnly, IsCompanyOwnerOrReadOnly
from .models import Company
from .serializers import CompanySerializer
# Create your views here.


class CompanyListCreateAPIView(ListCreateAPIView):
    """
    get all Companies
    create new Company
    """
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    permission_classes = (IsAuthenticatedAndHaveNotCompanyOrReadOnly, )


class CompanyDetailAPIView(RetrieveUpdateAPIView):
    """
    get the instance of Company
    update the instance of Company
    """
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    permission_classes = (IsCompanyOwnerOrReadOnly, )


class CompanyDetail(ListView):
    model = Vacancy
    template_name = 'company_app/company_card.html'
    context_object_name = 'vacancies'

    def get_context_data(self, **kwargs):
        context = super(CompanyDetail, self).get_context_data(**kwargs)
        company_id = self.kwargs['id']
        current_company = Company.objects.get(id=company_id)
        context['company'] = current_company
        context['vacancy_counter'] = Vacancy.objects.filter(company=current_company).count()
        return context
