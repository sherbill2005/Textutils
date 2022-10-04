# This file is created by me
from django.http import HttpResponse
from django.shortcuts import render


def about(request):
    return render(request, 'about.html')


def index(request):
    return render(request, 'index.html')
    # return HttpResponse("home")


def analyze(request):
    # get the text

    djtext = request.POST.get("text", "default")
    # Checkbox values
    removepunc = request.POST.get("removepunc", "off")
    fullcaps = request.POST.get("fullcaps", "off")
    newline = request.POST.get("newline", "off")
    extraspaceremover = request.POST.get("extraspaceremover", "off")
    charcounter = request.POST.get("charcounter", "off")

    if removepunc == "on":
        # remove punctuation
        punctuations = '''!()-[]{};:'"\\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {"purpose": "Remove puncuation", "analyzed_text": analyzed}
        djtext = analyzed

    if fullcaps == "on":
        # Capitalize all letters
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {"purpose": "Change to uppercase", "analyzed_text": analyzed}
        djtext = analyzed
    if newline == "on":
        # new Line remover
        analyzed = ""
        for char in djtext:
            if char != "\n" and char != "\r":
                analyzed = analyzed + char
        params = {"purpose": "New Line Removed", "analyzed_text": analyzed}
        djtext = analyzed

    if extraspaceremover == "on":
        analyzed = ""
        for Ande, char in enumerate(djtext, start=0):
            if not (djtext[Ande] == " " and djtext[Ande + 1] == " "):
                analyzed = analyzed + char
        params = {"purpose": "Extra space removed", "analyzed_text": analyzed}
        djtext = analyzed

    if charcounter == 'on':
        analyzed2 = analyzed + ('\nNo. of characters given in the text are : ' + str(len(djtext)))
        params = {'purpose': 'Characters Counted', 'analyzed_text2': analyzed2}
        djtext = analyzed2

    if removepunc != "on" and fullcaps != "on" and newline != "on" and extraspaceremover != "on" and charcounter != "on":
        error = HttpResponse("Please select an operation")
        return error

    return render(request, 'analyze.html', params)
