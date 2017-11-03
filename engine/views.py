# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import datetime
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from engine.tasks import health_check
from engine.view_decorators import require_http_methods


# Create your views here.
def health(request):
    now = datetime.datetime.now().isoformat()
    resp = {
        "alive": True,
        "timestamp": now
    }
    health_check.delay()
    return JsonResponse(resp)


@csrf_exempt
@require_http_methods(["POST"])
def ruleset_definition(request, ruleset_name):
    ruleset_define = json.loads(request.body.decode("utf-8"))
    resp = {
        "ruleset_name": ruleset_name,
        "type": "definition",
        "timestamp": datetime.datetime.now().isoformat()
    }
    return JsonResponse(resp)


@csrf_exempt
@require_http_methods(["POST"])
def ruleset_facts(request, ruleset_name):
    fact_info = json.loads(request.body.decode("utf-8"))
    resp = {
        "ruleset_name": ruleset_name,
        "type": "facts",
        "timestamp": datetime.datetime.now().isoformat()
    }
    return JsonResponse(resp)


@csrf_exempt
@require_http_methods(["POST"])
def ruleset_events(request, ruleset_name):
    event_info = json.loads(request.body.decode("utf-8"))
    resp = {
        "ruleset_name": ruleset_name,
        "type": "events",
        "timestamp": datetime.datetime.now().isoformat()
    }
    return JsonResponse(resp)


@require_http_methods(["GET"])
def ruleset_info(request, ruleset_name):
    if ruleset_name == "all":
        # get all rulesets
        pass
    else:
        # get ruleset name
        pass
    return JsonResponse(resp)