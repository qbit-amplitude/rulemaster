# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import datetime
import json
import sqlite3
import base64
import requests
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from engine.tasks import health_check
from engine.view_decorators import require_http_methods
from engine.models import Rule, RuleSet

## constants
RESP_CODES = {
    0: "OK",
    1: "Out of memory (uncommon)",
    2: "Unexpected type (uncommon)",
    5: "Unexpected name (uncommon)",
    6: "Rule limit exceeded (uncommon)",
    8: "Rule beta limit exceeded (uncommon)",
    9: "Rule without qualifier (uncommon)",
    10: "Invalid rule attribute (uncommon)",
    101: "Error parsing JSON value (uncommon)",
    102: "Error parsing JSON string (uncommon)",
    103: "Error parsing JSON number (uncommon)",
    104: "Error parsing JSON object (uncommon)",
    301: "Could not establish Redis connection",
    302: "Redis returned an error",
    501: "Could not parse regex",
    502: "Max regex state transitions reached (uncommon)",
    503: "Max regex states reached (uncommon)",
    504: "Regex DFA transform queue full (uncommon)",
    505: "Regex DFA transform list full (uncommon)",
    506: "Regex DFA transform set full (uncommon)",
    507: "Conflict in regex transform (uncommon)",
    201: "The event or fact was not captured because it did not match any rule",
    202: "Too many properties in the event or fact",
    203: "Max rule stack size reached due to complex ruleset (uncommon)",
    209: "Max number of command actions reached (uncommon)",
    210: "Max number of add actions reached (uncommon)",
    211: "Max number of eval actions reached (uncommon)",
    212: "The event or fact has already been observed",
    302: "Redis returned an error"
}


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
    #
    # get_or_update django query
    #
    org, domain, sub_domain = None, None, None
    ruleset_define = json.loads(request.body.decode("utf-8"))
    condition_api = ruleset_define.get('condition_api',{})
    api_name = condition_api.get('name', "")
    api_id = condition_api.get("ID", {})
    parameters = condition_api.get('params', {})
    if parameters.get('domain'):
        domain = parameters['domain']
    if parameters.get('org'):
        org = parameters['org']
    if parameters.get('sub_domain'):
        sub_domain = parameters['sub_domain']
    description = json.dumps(ruleset_define)#.get('ruleset_name'))
    encoded_description = base64.b64encode(bytes(description), 'utf-8')
    rule_name = ruleset_name #ruleset_define.get('ruleset_name').keys()[0]

    if not Rule.objects.filter(rule_description=encoded_description, rule_name=rule_name, org=org, domain=domain, sub_domain=sub_domain):
        rule_obj = Rule.objects.create(
            rule_name=rule_name,
            org=org,
            domain=domain,
            sub_domain=sub_domain,
            rule_description=encoded_description,
            action=rule_name,
            condition=json.dumps(ruleset_define)#.get('ruleset_name').keys()[0].get('start')),
        )
        rule_obj.save()
        RuleSet.objects.create(
            rule_id=rule_obj,
            rule_set_name=ruleset_name,
            rule_set_description=description,
            org=org,
            domain=domain,
            sub_domain=sub_domain,
            ).save()
    ## set/update in RE
    url = '/'.join(['http://127.0.0.1:5000', ruleset_name, 'definition'])
    print description
    rule_engine_response = requests.post(url=url, data=description.encode('utf-8'))
    print rule_engine_response.__dict__

    # create response_body
    try:
        response_data = RESP_CODES.get(int(rule_engine_response.json()['outcome']))
    except:
        response_data = rule_engine_response.__dict__.get('status_code')

    resp = {
        "ruleset_name": ruleset_name,
        "type": "definition",
        "timestamp": datetime.datetime.now().isoformat(),
        "response_data": response_data
    }
    return JsonResponse(resp)


@csrf_exempt
@require_http_methods(["POST"])
def ruleset_facts(request, ruleset_name):
    fact_info = json.loads(request.body.decode("utf-8"))
    query_data = json.dumps(fact_info.get('query_data'))
    url = '/'.join(['http://127.0.0.1:5000', ruleset_name, 'facts'])
    response_data = requests.post(url=url, data=query_data.encode('utf-8'))
    resp = {
        "ruleset_name": ruleset_name,
        "type": "facts",
        "timestamp": datetime.datetime.now().isoformat(),
        "response_data": response_data
    }
    return JsonResponse(resp)


@csrf_exempt
@require_http_methods(["POST"])
def ruleset_events(request, ruleset_name):
    event_info = json.loads(request.body.decode("utf-8"))
    #
    # get_or_update django query
    #
    query_data = json.dumps(event_info.get('query_data'))
    print(query_data)
    url = '/'.join(['http://127.0.0.1:5000', ruleset_name, 'events'])
    response_data = requests.post(url=url, data=query_data.encode('utf-8'))
    print response_data.json()
    resp = {
        "ruleset_name": ruleset_name,
        "type": "events",
        "timestamp": datetime.datetime.now().isoformat(),
        "response_data": response_data.json()
    }
    return JsonResponse(resp)


@require_http_methods(["GET"])
def ruleset_info(request, ruleset_name=None):
    if ruleset_name == "all":
        # get all rulesets
        # fetch from sqlite
        rule_sets = RuleSet.objects.all() 
    else:
        # get ruleset name
        # fetch specific ruleset from sqlite 
        rule_sets = RuleSet.objects.filter(rule_set_name=ruleset_name)
    resp = [{"name": obj.ruleset_name, "id": obj.rule_set_id, "associated_rules": obj.rule_id.rule_name} for obj in rule_sets]
    return JsonResponse(resp)



