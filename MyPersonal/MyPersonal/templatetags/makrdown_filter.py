# -*- coding:utf-8 -*-
import markdown

from django import template
from django.template.defaultfilters import stringfilter
from django.utils.safestring import mark_safe


register = template.Library()  # 自定义filter时必须加上


@register.filter
@stringfilter  # 希望字符串作为参数
def markdown_p(value):
    return mark_safe(markdown.markdown(
        value,extensions=['markdown.extensions.fenced_code',
        'markdown.extensions.codehilite'],safe_mode=False,
        enable_attributes=False))