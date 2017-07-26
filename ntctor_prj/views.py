from django.shortcuts import render
from partners.models import Partner


def index(request):
    template = 'pages/index.html'
    partners = Partner.objects.filter(show=True)
    var = {
            "partners":partners,
            }
    return render(request, template, var)
