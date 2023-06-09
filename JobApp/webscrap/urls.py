from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path("about/", views.about, name='about'),
    path("personalize/", views.personalize, name='personalize'),
    path("contact/", views.contact, name='contact'),
    path("request_tag", views.request_tag, name='request_tag'),
    path("get_skill_list/", views.get_skill_list, name='get_skill_list'),
    path("post_scrapped_jobs/", views.post_scrapped_jobs, name='post_scrapped_jobs'),
]