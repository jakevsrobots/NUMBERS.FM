from django import template
from pages.models import Page


register = template.Library()

@register.inclusion_tag('pages/page_fragment.html')
def display_page(page_name):
    page,created = Page.objects.get_or_create(name=page_name)
    return {'body': page.body}
