import re
from pprint import pprint

from django import template
from django.template import TemplateSyntaxError
from django.template.base import FILTER_SEPARATOR
from django.template.defaulttags import ForNode
from django.utils.html import mark_safe

from e_logs.common.all_journals_app.templatetags.for_or_create_node import ForOrCreateNode
from utils.deep_dict import deep_dict

register = template.Library()


class UnfilledCell():
    def __str__(self):
        return ""


# descriptions for admin
@register.simple_tag()
def model_desc(obj):
    if obj.__doc__:
        return mark_safe('<p>{}</p>'.format(obj.__doc__))
    return ''


@register.filter(name='formcontrol')
def addclass(value):
    return value.as_widget(attrs={'class': 'form-control'})


@register.filter(name='formatDate')
def format_date(value):
    return value


@register.filter
def keyval(d, key):
    res = deep_dict(d).clear_empty()[key]
    if isinstance(res, deep_dict):  # this if is only for proper serialization
        return res.get_dict()
    return res


@register.filter
def table_keyval(d, key):
    res = deep_dict(d).clear_empty()[key]
    if isinstance(res, deep_dict):  # this if is only for proper serialization
        return res.get_dict()
    return res


@register.filter
def choose_val(field_info, index):
    return field_info[index] if index in field_info else ""


@register.filter
def stack(a, b):
    return a + b

@register.filter
def index(sequence, position):
    return sequence[position]


@register.filter(name='split')
def split(value, arg):
    return value.split(arg)


@register.filter('default_for_responsible')
def default_for_responsible(responsible):
    if responsible is None or responsible == {}:
        return ""
    else:
        return responsible


@register.simple_tag(takes_context=True)
def set_global_context(context, key, value):
    """
    Sets a value to the global template context, so it can
    be accessible across blocks.

    Note that the block where the global context variable is set must appear
    before the other blocks using the variable IN THE BASE TEMPLATE.  The order
    of the blocks in the extending template is not important.

    Usage::
        {% extends 'base.html' %}

        {% block first %}
            {% set_global_context 'foo' 'bar' %}
        {% endblock %}

        {% block second %}
            {{ foo }}
        {% endblock %}
    """
    context.dicts[0][key] = value
    return ''


@register.simple_tag
def get_table_name(table_link):
    return '.'.join(table_link.split('/')[-1].split('.')[:-1])


@register.filter('formatter')
def formatter(string, obj):
    return string.format(object)


@register.filter(name='times')
def times(number):
    return range(number)


@register.tag('for_or_create')
def do_for_or_create(parser, token):
    bits = token.split_contents()
    if len(bits) < 4:
        raise TemplateSyntaxError("'for' statements should have at least four"
                                  " words: %s" % token.contents)

    is_reversed = bits[-1] == 'reversed'
    in_index = -3 if is_reversed else -2
    if bits[in_index] != 'in':
        raise TemplateSyntaxError("'for' statements should use the format"
                                  " 'for x in y': %s" % token.contents)

    invalid_chars = frozenset((' ', '"', "'", FILTER_SEPARATOR))
    loopvars = re.split(r' *, *', ' '.join(bits[1:in_index]))
    for var in loopvars:
        if not var or not invalid_chars.isdisjoint(var):
            raise TemplateSyntaxError("'for' tag received an invalid argument:"
                                      " %s" % token.contents)

    sequence = parser.compile_filter(bits[in_index + 1])
    nodelist_loop = parser.parse(('empty', 'endfor_or_create',))
    token = parser.next_token()
    if token.contents == 'empty':
        nodelist_empty = parser.parse(('endfor_or_create',))
        parser.delete_first_token()
    else:
        nodelist_empty = None
    return ForOrCreateNode(loopvars, sequence, is_reversed, nodelist_loop, nodelist_empty)