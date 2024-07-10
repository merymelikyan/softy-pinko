from django.db import models
from django.utils import timezone

class HeaderText(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=255)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "HeaderText"
        verbose_name_plural = "HeaderText"


class FooterText(models.Model):
    text = models.CharField(max_length=255)
        
    def __str__(self):
        return self.text

    class Meta:
        verbose_name = "Footer Text"
        verbose_name_plural = "Footer Text"



class TreeBlocks(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=255)
    image = models.ImageField(upload_to="tree-blocks")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Tree Block"
        verbose_name_plural = "Tree Blocks"


class LeftBlock(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=255)
    image = models.ImageField(upload_to="left-block")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Left Block"
        verbose_name_plural = "Left Block"


class RightBlock(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=255)
    image = models.ImageField(upload_to="right-block")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Right Block"
        verbose_name_plural = "Right Block"


class WorkProcess(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=255)
    image = models.ImageField(upload_to="work_process")

    def __str__(self):
        return self.title        

    class Meta:
        verbose_name = "Work process"
        verbose_name_plural = "Work process"


class Reviews(models.Model):
    review  = models.TextField(max_length=400)
    first_name = models.CharField(max_length=45)
    Last_name = models.CharField(max_length=45)
    position = models.CharField(max_length=60)
    image = models.ImageField(upload_to="reviews")
      
    def __str__(self):
        return f"{self.first_name}{self.Last_name}"

    class Meta:
        verbose_name = "Review"
        verbose_name_plural = "Reviews"


class PricingPlan(models.Model):
    title = models.CharField(max_length=255)  
    price = models.FloatField() 
    space = models.CharField(max_length=255)
    transfer = models.CharField(max_length=255)
    panel = models.CharField(max_length=255)
    support = models.CharField(max_length=255)
    emails = models.CharField(max_length=255)
    security = models.CharField(max_length=255)
    
    is_space = models.BooleanField(default=True)
    is_transfer = models.BooleanField(default=True)
    is_panel = models.BooleanField(default=True)
    is_support = models.BooleanField(default=True)
    is_emails = models.BooleanField(default=True)
    is_security = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Pricing Plan"
        verbose_name_plural = "Pricing Plans"


class Counter(models.Model):
    projects = models.IntegerField(default=0)
    happy_clients = models.IntegerField(default=0)
    award_wins = models.IntegerField(default=0)
    countries = models.IntegerField(default=0)

    def __str__(self):
        return "Counter"

    class Meta:
        verbose_name = "Counter"
        verbose_name_plural = "Counters"

class Blog(models.Model):
    image = models.ImageField(upload_to="blog")
    title = models.CharField(max_length=60)
    description = models.TextField()
    created_at =models.DateTimeField(default=timezone.now)


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Blog"
        verbose_name_plural = "Blogs"
