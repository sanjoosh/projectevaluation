from django.db import models

# Create your models here.
class ProjectEvaluation(models.Model):
    UserName=models.CharField(max_length=20,null=False,blank=False)
    Password=models.CharField(max_length=20,null=False,blank=False)
    
    def __unicode__(self):
        return self.UserName