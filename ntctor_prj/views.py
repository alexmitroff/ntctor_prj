from django.shortcuts import render

def index(request):
    template = 'pages/index.html'
    var = {}
    return render(request, template, var)
