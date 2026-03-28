from django import template
from quiz.md_parser import render_markdown as _render_md

register = template.Library()


@register.filter(name='render_md')
def render_md(value):
    """Render Markdown text to HTML."""
    return _render_md(value)
