from django.shortcuts import render
import logging
from django.http import HttpResponse
from django.conf import settings

logger = logging.getLogger(__name__)

# Create your views here.


def profiles_view(request):
    if request.GET.get("parameter"):
        logger.info(f"Parameter is: {request.GET.get('parameter')}")
        return HttpResponse(f"Parameter is: {request.GET.get('parameter')}")
    return HttpResponse(f"No parameters.")
