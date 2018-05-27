# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import redirect
from django.http import HttpResponse, HttpResponseNotFound



import requests

from urllib.parse import quote

CLASSIFIER_PYTHON = "Programming Language :: Python ::"
CLASSIFIER_DJANGO = "Framework :: Django ::" 
CLASSIFIER_DJANGOCMS = "Framework :: Django CMS ::" 

CLASSIFIER = {
    "python" :CLASSIFIER_PYTHON,
    "django" : CLASSIFIER_DJANGO,
}



def get_classifier_info(pypiproject, classifiers=[]):
    """
    Users the pypi json API and returns information about the classifiers of a project.
    Please cache this function if possible to reduce the load on pypi and also please 
    read the documentation of pypi in regards to using this api.
    """

    ret = {}

    r = requests.get(
        "https://pypi.org//pypi/{}/json".format(pypiproject),
        stream=True,
    )
    if r.status_code == 200:
        r_json = r.json()
        for classifier in classifiers:
            ret[classifier] = []
            for entry in r_json["info"]["classifiers"]:
                if classifier in entry:
                    ret[classifier].append(entry.split("::")[-1].strip("\"' ,"))
    return ret


# Create your views here.
def image_redirect(request, classifier, project_name):
    if classifier in CLASSIFIER:
        versions = dict(get_classifier_info(project_name, [CLASSIFIER[classifier]]))
        version = quote(", ".join(versions[CLASSIFIER[classifier]]))

        if request.GET.get('debug'):
            return HttpResponse("https://img.shields.io/badge/{}-{}-green.svg".format(classifier,version))
        else:        
            return redirect("https://img.shields.io/badge/{}-{}-green.svg".format(classifier,version))
        
    else:
        return HttpResponseNotFound('classifier undefined')  
