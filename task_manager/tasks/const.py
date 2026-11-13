from django.db import models
from django.utils.translation import gettext_lazy as _

class TaskState(models.TextChoices):
    todo="todo",_("Todo")
    in_progress="in_progress",_("In progress")
    done="done",_("Done")

class PriorityState(models.TextChoices):
    low="low",_("Low")
    medium="medium",_("Medium")
    high="high",_("High")