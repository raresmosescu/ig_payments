from django import template

register = template.Library()

@register.filter
def get_at_index(list, index):
    return list[index]

@register.filter
def divide(n1, n2):
    return n1*n2

@register.filter
def multiply(n1, n2):
    return n1*n2

@register.filter
def discount(price, discount):
    return (price - (price*discount))

@register.filter
def round_float(float_number:float, decimals=2):
    return round(float_number, decimals)

@register.filter
def plus(n1, n2):
    return n1+n2

@register.filter
def minus(n1, n2):
    return n1-n2

@register.filter
def to_int(value):
    return int(value)

@register.filter
def modulo(n, val):
    return n%val

@register.filter
def count(queryset_obj):
    counter = 0
    for _ in queryset_obj:
        counter += 1
    print(queryset_obj, counter)
    return counter

    