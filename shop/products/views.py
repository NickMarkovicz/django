from django.shortcuts import render
import logging
from django.http import HttpResponse
from django.conf import settings

logger = logging.getLogger(__name__)

# Create your views here.


def index(request):
    return HttpResponse(f"This is the Main Page.")


def products_view(request):
    if request.GET.get("parameter"):
        logger.info(f"Parameter is: {request.GET.get('parameter')}")
        return HttpResponse(f"Parameter is: {request.GET.get('parameter')}")
    return HttpResponse(f"No parameters.")


def variables(request):
    logger.info(f"{settings.FIRST_VAR}")
    if request.method == "GET":
        if int(settings.FIRST_VAR) == 1:
            return HttpResponse(f"{settings.SECOND_VAR}")
        return HttpResponse(f"{settings.THIRD_VAR}")
