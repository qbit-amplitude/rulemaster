from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^v1/health$', views.health, name='health'),
    url(r'^v1/?P<ruleset_name>[_0-9a-ZA-Z\-]+/definition', views.ruleset_definition, name="ruleset_definition")
    url(r'^v1/?P<ruleset_name>[_0-9a-ZA-Z\-]+/facts', views.ruleset_facts, name="ruleset_facts")
    url(r'^v1/?P<ruleset_name>[_0-9a-ZA-Z\-]+/events', views.ruleset_events, name="ruleset_events")
]