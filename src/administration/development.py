from django.db import models

from src.account.staff import Staff
from utils.helpers import timestamp_id

class BaseResouce(models.Model):
    """ Non-Database abstract class with common fields"""
    
    resouce_id  = models.CharField(max_length=16, default=timestamp_id(12))
    title       = models.CharField(max_length=50)
    tag         = models.SlugField(max_length=20, null=True, blank=True)
    date_added  = models.DateTimeField(auto_now_add=True)
    last_updated    = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        abstract = True
        ordering = ['-date_added', 'title']


class TrainingVideo(BaseResouce):
    """ Database class Inheriting from BaseResouce"""
    
    video     = models.FileField(upload_to="learning/videos")
    audience  = models.CharField(max_length=20)
    
    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = "Training Video"
        verbose_name_plural = "Training Videos"


class TrainingFile(BaseResouce):
    """ Database class Inheriting from BaseResouce"""
    
    file  = models.FileField(upload_to="learning/files")

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = "Training File"
        verbose_name_plural = "Training Files"
        

class TrainingMaterial(models.Model):
    tag     = models.CharField(max_length=30)
    Videos  = models.ManyToManyField(TrainingVideo)
    files   = models.ManyToManyField(TrainingFile)
    date_added  = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ["-date_added"]
        verbose_name = "Training Material"
        verbose_name_plural = "Training Materials"
    
    def __str__(self) -> str:
        return self.tag
    
    class Meta:
        verbose_name = "Training Material"
        verbose_name_plural = "Training Materials"


class TrainingProgram(models.Model):
    program_name = models.CharField(max_length=255)
    description  = models.TextField(null=True, blank=True)
    start_date   = models.DateField()
    end_date     = models.DateField()
    staffs       = models.ManyToManyField(Staff)
    materials    = models.ManyToManyField(TrainingMaterial)

    def __str__(self):
        return self.program_name

    class Meta:
        verbose_name = "Training Program"
        verbose_name_plural = "Training Programs"