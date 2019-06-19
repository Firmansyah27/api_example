from django.shortcuts import render
from languages.models import Paradigm, Language, Programmer


def home (request):
    paradigm = Paradigm.objects
    language = Language.objects
    Programmer = Programmeer.objects
    return render(request, 'home.html',{'paradigm':paradigm,'language':language,'pragrammer':programmer}
)
    