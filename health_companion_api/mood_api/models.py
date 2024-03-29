from django.db import models
from .utils import validate_word_count


# Create your models here.
class DailyLog(models.Model):
    log = models.TextField(validators=[validate_word_count])

    def __str__(self):
        return self.log
