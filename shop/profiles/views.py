from django.shortcuts import render
import logging
from django.http import HttpResponse

logger = logging.getLogger(__name__)

# Create your views here.


def profiles_index(request):
    logger.info(request.GET, request.POST)
    return HttpResponse("Profiles app works.")
