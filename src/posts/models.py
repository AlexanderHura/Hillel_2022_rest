from django.db import models

# Create your models here.

from django.conf import settings

class TimeStampMixin(models.Model):
    class Meta:
        abstract = True

    created_at = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now=True)



class Post(TimeStampMixin):
    title = models.CharField(max_length=100)
    content = models.TextField()
    status = models.BooleanField(null=False, blank=False, default=True)

    author = models.ForeignKey(settings.AUTH_USER_MODEL, null=False, blank=False, on_delete=models.CASCADE)



    def __str__(self) -> str:
        return self.title