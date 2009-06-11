from django.shortcuts import render_to_response as render

def welcome(request):
    """This view is only used to render a template to show lightsearch"""
    return render('welcome.html')

def templatetags(request):
    """This view is used to print the output of some templatetags"""
    return render('templatetags.html')
