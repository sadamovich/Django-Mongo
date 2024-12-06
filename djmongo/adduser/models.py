from django.db import models


class Job(models.Model):
    title = models.CharField(max_length=100, help_text="Enter a job title (e.g. car washer, cashier etc.)")

    def __str__(self):
        return self.title

class Staff(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    job = models.ManyToManyField(Job, help_text="Select a job.")

    def __str__(self):
        return '%s, %s' % (self.last_name, self.first_name)