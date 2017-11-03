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