from rest_framework.generics import CreateAPIView, RetrieveUpdateAPIView, ListCreateAPIView, RetrieveAPIView, \
    ListAPIView, RetrieveUpdateDestroyAPIView
from admin_app.models import Resume
from company_app.models import Company
from vacancy_app.models import Vacancy, Specialty
from .serializers import ResumeSerializer, CompanySerializer, ApplicationSerializer, \
    VacancyRelatedCompanySerializer, SpecialtySerializer, VacancySerializer
from .permissions import IsAuthenticatedAndHasNotResume, IsAuthenticatedAndHasTheResume, \
    IsAuthenticatedAndHaveNotCompanyOrReadOnly, IsCompanyOwnerOrReadOnly, IsVacancyOwnerOrReadOnly, IsCompanyOwner, \
    UserHasCompanyOrReadOnly

import datetime

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
