'''
from django.db import models

# Create your models here.
class Calendar(models.Model):
	day = models.DateField(u'Day of the Event', help_text = u'Day of the Event')

	class Meta:
	    verbose_name = u'Scheduling'
	    verbose_name_plural = u'Scheduling'
	    '''