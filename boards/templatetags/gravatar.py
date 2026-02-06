import hashlib
from django import template

register = template.Library()

@register.simple_tag
def gravatar(email, size=40):
    email = email.lower().encode('utf-8')
    hash = hashlib.md5(email).hexdigest()
    return f"https://www.gravatar.com/avatar/{hash}?s={size}&d=identicon"
