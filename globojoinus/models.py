from django.db import models

# Create your models here.
class Profile(models.Model):
    username = models.CharField(max_length=255, null=True, blank=True)
    nome = models.CharField(max_length=255, null=True, blank=True)
    link = models.CharField(max_length=255, null=True, blank=True)
    email = models.CharField(max_length=255, null=True, blank=True)
    company = models.CharField(max_length=255, null=True, blank=True)
    location = models.CharField(max_length=255, null=True, blank=True)
    linguagens = models.CharField(max_length=255, null=True, blank=True)
    projetos = models.IntegerField(null=True, blank=True)
    contactado = models.NullBooleanField(null=True, blank=True)
    iniciado = models.NullBooleanField(null=True, blank=True)
    aprovado = models.NullBooleanField(null=True, blank=True)
    status = models.TextField(null=True, blank=True)
    #projetos = models.ManyToManyField(Projeto, related_name='projetos')
    
    # http://www.linkedin.com/search/fpsearch?companyId=8198&sortCriteria=R&keepFacets=&facet_CC=8198&facet_ED=10512+10582+10696&trk=biz_overview_see_alumni#facets=companyId%3D8198%26searchLocationType%3DY%26keepFacets%3DkeepFacets%26facet_CC%3D8198%26facet_ED%3D10582+10696+10512%26viewCriteria%3D1%26sortCriteria%3DR%26facetsOrder%3DCC%252CED%252CN%252CG%252CI%252CPC%252CL%252CFG%252CTE%252CFA%252CSE%252CP%252CCS%252CF%252CDR%26page_num%3D2%26openFacets%3DN%252CCC%252CED