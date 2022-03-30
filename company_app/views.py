from django.views.generic import ListView
from .models import Company
from vacancy_app.models import Vacancy

# Create your views here.


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
