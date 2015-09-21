from django.contrib import admin

# Register your models here.
from .models import ProjectEvaluation

class ProjectEvaluationAdmin(admin.ModelAdmin):
    class Meta:
        model=ProjectEvaluation

admin.site.register(ProjectEvaluation, ProjectEvaluationAdmin)        
        