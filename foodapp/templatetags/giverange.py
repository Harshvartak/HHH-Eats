from django import template

register = template.Library()

@register.filter(name='val')
def val(count):
    return range(count)