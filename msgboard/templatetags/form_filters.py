#!/usr/bin/env python
# coding=utf-8

from django import template

register = template.Library()


@register.filter(is_safe=True, name='add_class')
def add_class(value, arg):
    return value.as_widget(attrs={'class': arg})
