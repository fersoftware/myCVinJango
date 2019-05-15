from django.shortcuts import render
from django.utils import timezone
from .models import PersonalData,Objective,ProfessionalExperience,Education,Skill,Language,Certificate

def cv_list(request):
    listPersonalData = PersonalData.objects.all()
    listObjective = Objective.objects.all()
    listProfXP = ProfessionalExperience.objects.all()
    listEducation = Education.objects.all()
    listSkill = Skill.objects.all()
    listLanguage = Language.objects.all()
    listCertificate = Certificate.objects.all()
    return render(request, 'cv/cv_list.html', {'listPerson': listPersonalData, 'listObjective': listObjective,'listProfXP': listProfXP,'listEducation': listEducation,'listSkill': listSkill,'listLanguage': listLanguage, 'listCertificate': listCertificate})
