from django.dispatch import receiver
from .models import Product
from django.db.models.signals import pre_save


@receiver(pre_save, sender=Product)
def calculate_off_price(sender, instance, **kwargs):
    instance.new_price = ((100 - instance.offers) * instance.price) / 100
