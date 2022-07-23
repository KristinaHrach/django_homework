from django.db.models import TextChoices
from django.utils.translation import gettext_lazy as _


class TypeChoices(TextChoices):
    Teacher = 'T', _('Teacher')
    Student = 'S', _('Student')
