from django.shortcuts import render, redirect
import logging
from django.http import HttpResponse
from django.conf import settings

from profiles.forms import RegisterForm

logger = logging.getLogger(__name__)

# Create your views here.


def profiles_view(request):
    if request.GET.get("parameter"):
        logger.info(f"Parameter is: {request.GET.get('parameter')}")
        return HttpResponse(f"Parameter is: {request.GET.get('parameter')}")
    return HttpResponse(f"No parameters.")


def sign_up(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            logger.info(f"User Email: {form.cleaned_data['email']}")
            logger.info(f"User password: {form.cleaned_data['password']}")
            return redirect("/thanks/")
    else:
        form = RegisterForm()
    return render(request, "sign_up.html", {"form": form})


def thanks(request):
    return HttpResponse(f"Thank you!")
