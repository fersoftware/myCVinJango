from django.contrib import admin
from .models import Certificate, Education,Language,Objective,PersonalData,Post,ProfessionalExperience,Skill

Models = (Certificate, Education,Language,Objective,PersonalData,Post,ProfessionalExperience,Skill)

admin.site.register(Models)
