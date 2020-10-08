from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=100)


class Candidate(models.Model):
    name = models.CharField(max_length=255)
    job = models.CharField(max_length=255, default='Student')
    picture = models.ImageField(upload_to='candidate/%Y/%m/%d/', blank=True, max_length=255)
    city = models.CharField(max_length=100, blank=True)
    province = models.CharField(max_length=100, blank=True)
    days_notice = models.IntegerField(default=0)
    description = models.TextField(blank=True)
    company = models.ForeignKey(to=Company, on_delete=models.CASCADE, null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
