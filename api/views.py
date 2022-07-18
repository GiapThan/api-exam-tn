import imp
from django.shortcuts import render
from django.http import HttpResponse

import cv2

def index(req):
    
    return HttpResponse("hello")