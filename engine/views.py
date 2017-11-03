# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import datetime
from django.http import JsonResponse
from engine.tasks import health_check


# Create your views here.
def health(request):
    now = datetime.datetime.now().isoformat()
    resp = {
        "alive": True,
        "timestamp": now
    }
    health_check.delay()
    return JsonResponse(resp)


def ruleset_definition(request, ruleset_name):
    resp = {
        "ruleset_name": ruleset_name,
        "type": "definition",
        "timestamp": datetime.datetime.now().isoformat()
    }
    return JsonResponse(resp)


def ruleset_facts(request, ruleset_name):
    resp = {
        "ruleset_name": ruleset_name,
        "type": "facts",
        "timestamp": datetime.datetime.now().isoformat()
    }
    return JsonResponse(resp)


def ruleset_events(request, ruleset_name):
    resp = {
        "ruleset_name": ruleset_name,
        "type": "events",
        "timestamp": datetime.datetime.now().isoformat()
    }
    return JsonResponse(resp)