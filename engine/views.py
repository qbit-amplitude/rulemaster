# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import datetime
from django.http import JsonResponse

# Create your views here.
def health(request):
    now = datetime.datetime.now().isoformat()
    resp = {
        "alive": True,
        "timestamp": now
    }
    return JsonResponse(resp)