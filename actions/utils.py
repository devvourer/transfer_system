from .models import Actions


def create_action(user, verb, target=None):
    action = Actions(user=user, verb=verb, target=target)
    action.save()