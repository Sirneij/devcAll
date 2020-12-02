from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from django.conf import settings
from portfolio.models import Introduction


@receiver(post_save, sender=settings.AUTH_USER_MODEL))
def create_user_portfolio(sender, instance, created, **kwargs):
    if created:
        Introduction.objects.create(user = instance)
    instance.introduction.save()
