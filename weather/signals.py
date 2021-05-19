import json
import channels.layers
from asgiref.sync import async_to_sync

from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import City


def send_message(event):
    message = event['message']
    channel_layer = channels.layers.get_channel_layer()
    # Send message to WebSocket
    async_to_sync(channel_layer.send)(text_data=json.dumps({
        'message': message
    }))


@receiver(post_save, sender=City, dispatch_uid='send_simple_data')
def send_simple_data(sender, instance, **kwargs):
    print('lol')
    group_name = 'weather'

    message = {
        'city_id': instance.city_id,
        'title': instance.title,
    }

    channel_layer = channels.layers.get_channel_layer()

    async_to_sync(channel_layer.group_send)(
        group_name,
        {
            'type': 'send_message',
            'message': message
        }
    )