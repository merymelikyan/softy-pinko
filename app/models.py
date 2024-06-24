from django.core.exceptions import ValidationError
from django.db import models

class HeaderText(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=250)


    def save(self, *args, **kwargs):
        if not self.pk and HeaderText.objects.exists():
            raise ValidationError("Only one header text instance is allowed")
        super().save(*args, *kwargs)

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = "HeaderText"
        verbose_name_plural = "HeaderText"


class SEO(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=500)
    keywords = models.CharField(max_length=255)
    robots = models.CharField(max_length=255)
    content_type = models.CharField(max_length=255)
    language = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = "seo"
        verbose_name_plural = "seo"


class OG(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=500)
    type = models.CharField(max_length=255)
    image = models.ImageField(max_length=255)
    urls = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = "Open Graph"
        verbose_name_plural = "Open Graphs"



