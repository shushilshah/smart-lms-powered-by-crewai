import re
from django import template

register = template.Library()


@register.filter
def youtube_embed(url):
    if not url:
        return ""
    regex = r"(?:youtu\.be/|youtube\.com/(?:watch\?v=|embed/|v/|shorts/))([\w-]+)"
    match = re.search(regex, url)
    if match:
        return f"https://www.youtube.com/embed/{match.group(1)}"
    return url
