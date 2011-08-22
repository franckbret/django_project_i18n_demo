from django import template
from django.core.urlresolvers import reverse, resolve

from classytags.core import Tag, Options
from classytags.arguments import Argument

from django.template import (Node, Variable, TemplateSyntaxError,
    TokenParser, Library, TOKEN_TEXT, TOKEN_VAR)
from django.template.base import _render_value_in_context
from django.template.defaulttags import token_kwargs
from django.utils import translation

register = template.Library()

@register.tag
class current_url(Tag):
    """ Return the current url name. This is convenient when we want to redirect
    to the same page in another language
    
    Keyword arguments:
    request  -- Django request object
    """
    name = 'current_url'
    options = Options(
        'as',
        Argument('varname', required=False, resolve=False)
    )

    def render_tag(self, context, varname):
        
        request = context["request"]
        url_path_info = resolve(request.get_full_path())
        output = url_path_info.url_name

        if varname:
            context[varname] = output
            return ''
        else:
            return output

#register.tag(current_url)

class override(object):
    def __init__(self, language, deactivate=False):
        self.language = language
        self.deactivate = deactivate
        self.old_language = translation.get_language()

    def __enter__(self):
        translation.activate(self.language)

    def __exit__(self, exc_type, exc_value, traceback):
        if self.deactivate:
            translation.deactivate()
        else:
            translation.activate(self.old_language)

class LanguageNode(Node):
    def __init__(self, nodelist, language):
        self.nodelist = nodelist
        self.language = language

    def render(self, context):
        with override(self.language.resolve(context)):
            output = self.nodelist.render(context)
        return output

@register.tag
def language(parser, token):
    """
    This will enable the given language just for this block.

    Usage::

        {% language "de" %}
            This is {{ bar }} and {{ boo }}.
        {% endlanguage %}

    """

    bits = token.split_contents()
    if len(bits) < 2:
        raise TemplateSyntaxError("'%s' takes one argument (language)" % bits[0])
    language = parser.compile_filter(bits[1])
    nodelist = parser.parse(('endlanguage',))
    parser.delete_first_token()
    return LanguageNode(nodelist, language)