from django import template

register = template.Library()

@register.filter(name='modulo')
def modulo(num, value):
    return num % value