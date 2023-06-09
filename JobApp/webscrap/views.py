import json

from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Personalize, Tags, jobDetails
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Q


# Create your views here.

def index(request):
    if request.user.is_authenticated:
        personalized_obj = Personalize.objects.filter(user=request.user).all()
        personalized_data = []
        alljobs = []
        for item in personalized_obj:
            personalized_data += list(map(
                lambda x: [x, item.skill],
                jobDetails.objects.filter(tag__skill = item.skill)
            ))
            alljobs += list(map(
                lambda x: [x, item.skill],
                jobDetails.objects.filter(~Q(tag__skill=item.skill))
            ))
    else:
        personalized_data = []
        alljobs = jobDetails.objects.all()
    return render(request, 'webscrap/main.html', {'alljobs': alljobs, "personal": personalized_data,
                                                  "is_no_data": not alljobs and not personalized_data})


def about(request):
    return render(request, 'webscrap/about.html')


def personalize(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            email = request.POST.get("email")
            skill = request.POST.get("skill")
            if Tags.objects.filter(skill=skill).exists():
                request.user.email = request.POST.get("email", "")
                personalize = Personalize(user=request.user, skill=skill)
                personalize.save()
                request.user.save()
                messages.success(request, "Personalize Request saved.")
            else:
                messages.error(request, "we dont have this skill in our database please request this skill")
                return redirect("request_tag")
        else:
            messages.error(request, "Please log in or create account first to personalize")
            return render(request, 'webscrap/main.html')
    return render(request, 'webscrap/personalize.html')


def contact(request):
    return render(request, 'webscrap/contact.html')


def request_tag(request):
    if request.method == 'POST':
        skill = request.POST.get("skill")
        if request.user.is_authenticated:
            tags = Tags(skill=skill, user=request.user)
            tags.save()
            messages.success(request, "we have added this skill we will soon notify you via email")
            return render(request, 'webscrap/main.html')

        else:
            messages.error(request, "you should be logged in or have a acount to request tags!")

    return render(request, 'webscrap/request_tag.html')


def get_skill_list(request):
    tags = Tags.objects.distinct()
    tag_set = tuple(map(lambda tag: [tag.id, tag.skill.lower()], tags))
    return JsonResponse(data={
        "status": True,
        "tags": tag_set
    })


@csrf_exempt
def post_scrapped_jobs(request):
    data = json.loads(request.body)
    if data:
        tag = data["tag"]
        tag = Tags.objects.get(id=tag)
        old_jobs = jobDetails.objects.filter(tag=tag).all()
        for job in old_jobs:
            job.delete()
        for job in data.get("jobs"):
            job_obj = jobDetails(
                company_name=job[0],
                title=job[1],
                link=job[2],
                tag=tag
            )
            job_obj.save()
    return JsonResponse(data={"status": True})
