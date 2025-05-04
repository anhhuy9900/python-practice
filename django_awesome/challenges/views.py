from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string
from django.shortcuts import render
# Create your views here.

monthly_challenges_constants = {
    "january": "Eat no meat for the entire month!",
    "february": "Walk for at least 20 minutes every day!",
    "march": "Learn Django for at least 20 minutes every day!",
    "april": "Eat no meat for the entire month!",
    "may": "Walk for at least 20 minutes every day!",
    "june": "Learn Django for at least 20 minutes every day!",
    "july": "Eat no meat for the entire month!",
    "august": "Walk for at least 20 minutes every day!",
    "september": "Learn Django for at least 20 minutes every day!",
    "october": "Eat no meat for the entire month!",
    "november": "Walk for at least 20 minutes every day!",
    "december": "Learn Django for at least 20 minutes every day!"
}


def index(request):
    return HttpResponse("Index Page")


def february(request):
    return HttpResponse("Eat no meat for the entire month!")


def march(request):
    return HttpResponse("Learn Django for at least 20 minutes every day!")


def monthly_challenges(request, month):
    try:
        # response_data = f"<h1>{monthly_challenges_constants[month]}</h1>"
        # response_data = render_to_string("challenges/index.html")
        # return HttpResponse(response_data)
        return render(request, "challenges/index.html", {
            "month": month,
            "text": "Go for a walk for at least 20 minutes every day!!!!"
        })
    except:
        return HttpResponseNotFound("<h1>This month is not supported!</h1>")


def monthly_challenges_by_number(request, month):
    monthly = list(monthly_challenges_constants.keys())

    if month > len(monthly):
        return HttpResponseNotFound("Invalid month")

    monthly_redirect = monthly[month - 1]
    monthly_path = reverse("monthly-challenge", args=[monthly_redirect])
    # return HttpResponseRedirect("/challenges/" + monthly_redirect)
    return HttpResponseRedirect(monthly_path)
