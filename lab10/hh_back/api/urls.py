from django.urls import path
from .views import CompanyListView, CompanyDetailView, get_vacancies, get_vacancy_details, get_vacancies_by_company, get_top_ten_vacancies

urlpatterns=[
    path('companies/', CompanyListView.as_view()),
    path('companies/<int:pk>/', CompanyDetailView.as_view()),
    path('companies/<int:pk>/vacancies', get_vacancies_by_company),

    path('vacancies/', get_vacancies),
    path('vacancies/<int:pk>/', get_vacancy_details),
    path('vacancies/top_ten',get_top_ten_vacancies),
]