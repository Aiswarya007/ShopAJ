from django import template

register = template.Library()

@register.filter
def multiply(value, arg):
    try:
        return value * arg
    except TypeError:
        return 0

@register.filter
def range_filter(value):
    """Returns a range for iteration."""
    return range(1, value + 1)