from django.shortcuts import render
import logging
from django.http import HttpResponse

logger = logging.getLogger(__name__)

# Create your views here.


def index(request):
    logger.info(request.GET, request.POST)
    return HttpResponse("It works.")
