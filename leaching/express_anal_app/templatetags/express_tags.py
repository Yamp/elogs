from pprint import pprint

from django import template
from django.utils.html import mark_safe

register = template.Library()


@register.simple_tag()
def model_desc(obj):
    if obj.__doc__:
        return mark_safe('<p>{}</p>'.format(obj.__doc__))
    return ''


@register.filter(name='formcontrol')
def addclass(value):
    return value.as_widget(attrs={'class': 'form-control'})


@register.filter(name='formatDate')
def addclass(value):
    return value


@register.simple_tag()
def value(fid, index=None):
    return '{% include "value.html" with field_name=' + str(fid) + ' index=' + str(index) + ' %}'


@register.filter
def keyval(dict, key):
    # pprint(dict)
    return dict[key]


@register.filter
def choose_val(field_info, index):
    if index is not None:
        return field_info[index]
    else:
        return field_info
