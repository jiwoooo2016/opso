from django.contrib import admin
from django.db.models import Avg
from .models import Project, Rating

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'average_score', 'ranking')

    def average_score(self, obj):
        avg = Rating.objects.filter(project=obj).aggregate(Avg('score'))['score__avg']
        return round(avg, 1) if avg else '없음'
    average_score.short_description = '평균 점수'

    def ranking(self, obj):
        all_projects = Project.objects.annotate(avg_score=Avg('ratings__score')).order_by('-avg_score')
        for i, project in enumerate(all_projects, start=1):
            if project.pk == obj.pk:
                return i
        return 'N/A'
    ranking.short_description = '등수'

admin.site.register(Project, ProjectAdmin)
admin.site.register(Rating)
