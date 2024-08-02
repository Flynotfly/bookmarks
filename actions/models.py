from django.conf import settings
from django.db import models


class Action(models.Model):
    user = models.ForeignKey(
        settings.USER_AUTH_MODEL,
        related_name='actions',
        on_delete=models.CASCADE()
    )
    varb = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        indexes = [
            models.Index(fields=['-created'])
        ]
        ordering=['-created']
