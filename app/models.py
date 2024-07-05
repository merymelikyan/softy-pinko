from django.db import models

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

class Reviews(models.Model):
    review  = models.TextField(max_length=400)
    first_name = models.CharField(max_length=45)
    Last_name = models.CharField(max_length=45)
    position = models.CharField(max_length=60)
    image = models.ImageField(upload_to="reviews")
      
    def __str__(self):
        return f"{self.first_name}{self.Last_name}"