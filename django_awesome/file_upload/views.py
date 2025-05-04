import os
import time
import json
from django.shortcuts import render
from django.views import View
from django.http import HttpResponseRedirect, HttpResponse

from .forms import ProfileForm
from .models import Profile

# Create your views here.


def create_folder():
    # Directory
    directory = "temp"
    # Parent Directory path
    parent_dir = ""
    # Path
    path = os.path.join(parent_dir, directory)

    # Create the directory
    # '/home / User / Documents'
    if not os.path.isdir('temp'):
        os.mkdir(path)
        print("Directory '% s' created" % directory)
    print("Directory '% s' is existing" % directory)


def store_file(file):
    create_folder()
    file_name = "temp/image-{}.jpg".format(time.time())
    with open(file_name, "wb+") as dest:
        for chunk in file.chunks():
            dest.write(chunk)


class CreateProfile(View):

    def get_all(self):
        all_objects = Profile.objects.all()
        print(repr(all_objects))
        # for key, value in all_objects.__dict__.items():
        #     print(key, value)
        return HttpResponse(all_objects)

    def get(self, request):
        form = ProfileForm()
        return render(request, "./create_profile.html", {
            "form": form
        })

    def post(self, request):
        # print(request.FILES["image"])
        # store_file(request.FILES["image"])
        # return HttpResponseRedirect("/upload/create-profile")

        submitted_form = ProfileForm(request.POST, request.FILES)

        if submitted_form.is_valid():
            profile = Profile(image=request.FILES["user_image"])
            profile.save()
            return HttpResponseRedirect("/upload/create-profile")

        return render(request, "./create_profile.html", {
            "form": submitted_form
        })
