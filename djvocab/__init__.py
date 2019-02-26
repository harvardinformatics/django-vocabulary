'''
Choices function.
'''
import django.apps
from django.core.exceptions import AppRegistryNotReady


def getChoices(key):
    """ fetch the choices for a given key
    """
    from djvocab.models import Vocabulary
    try:
        # This prevents issues in other apps using chioces in models.py.
        # as part of django.setup django tried to load all the app models
        # starting with the current app so an app using djvocab would not find the
        # Vocabulary model when choices was executed in it's model
        django.apps.apps.get_model('Vocabulary')
        choices = Vocabulary.objects.filter(key=key)
    except AppRegistryNotReady as e:
        choices = []
    return choices
