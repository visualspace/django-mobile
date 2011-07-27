from django_mobile import get_flavour
from django_mobile.conf import settings


def flavour(request):
    return {
        'flavour': get_flavour(),
    }

def user_agent_is_mobile(request):
    return {
        'user_agent_is_mobile': request.user_agent_is_mobile,
    }

def is_mobile(request):
    return {
        'is_mobile': get_flavour() == settings.DEFAULT_MOBILE_FLAVOUR,
    }
