from django import template
from radio.models import Show


register = template.Library()

@register.inclusion_tag('radio/show_list_fragment.html')
def list_shows():
    return {'shows': Show.objects.active()}
