from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from core.views.api_views import vacancy_list_view
from core.views.base import IndexView
from core.views.response import ResumeAddResponseView, ShowResponse, AddMessageToResponse
from core.views.resume import delete_resume, ResumeAddView, ResumeEditView, AddEducation, AddJob, update_resume, \
    ResumeDetailView, download_pdf, hide_resume, DeleteEducationView, EditEducationView, DeleteJobView, EditJobView
from core.views.vacancy import VacancyCreate, VacancyUpdate, VacancyDetail, vacancy_reload

urlpatterns = [
    path('', IndexView.as_view(), name='main'),
    path('vacancy/create', VacancyCreate.as_view(), name='vacancy_create'),
    path('vacancy/update/<int:pk>', VacancyUpdate.as_view(), name='vacancy_update'),
    path('vacancy/<int:pk>', VacancyDetail.as_view(), name='vacancy_detail'),
    path('vacancy/reload/<int:pk>', vacancy_reload, name='reload'),
    path('delete/resume/<int:pk>', delete_resume, name='delete_resume'),
    path('add/resume', ResumeAddView.as_view(), name='add_resume'),
    path('edit/resume/<int:pk>', ResumeEditView.as_view(), name='edit_resume'),
    path('delete/education/<int:pk>', DeleteEducationView.as_view(), name='delete_education'),
    path('edit/education/<int:pk>', EditEducationView.as_view(), name='edit_education'),
    path('delete/job/<int:pk>', DeleteJobView.as_view(), name='delete_job'),
    path('edit/job/<int:pk>', EditJobView.as_view(), name='edit_job'),
    path('resume/<int:pk>/add_education', AddEducation.as_view(), name='add_education'),
    path('resume/<int:pk>/add_job', AddJob.as_view(), name='add_job'),
    path('resume/update/<int:pk>', update_resume, name='update'),
    path('resume/<int:pk>', ResumeDetailView.as_view(), name='resume_detail'),
    path('resume/download/<int:pk>', download_pdf, name='download'),
    path('hide/resume/<int:pk>', hide_resume, name='hide'),
    path('vacancy/add/response/', ResumeAddResponseView.as_view(), name='add_response'),
    path('responses/', ShowResponse.as_view(), name='show_responses'),
    path('send/message/<int:pk>', AddMessageToResponse.as_view(), name='send_message'),
    path('api/vacancy', vacancy_list_view)
]
