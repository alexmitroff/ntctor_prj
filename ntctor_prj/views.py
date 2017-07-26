from django.shortcuts import render

def index():
    template = 'pages/index.html'
    var = {}
    return render(request, template, var)
