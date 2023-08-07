from django.db import models


class Employee(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()


class Event(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    event_type = models.CharField(max_length=50)
    event_date = models.DateField()


class EmailTemplate(models.Model):
    event_type = models.CharField(max_length=50)
    template = models.TextField()


class EmailLog(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    status = models.CharField(max_length=20)
    error_message = models.TextField(null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
