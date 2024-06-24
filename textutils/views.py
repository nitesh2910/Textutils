# I have created this file
from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    return render(request, "index.html")
    
    
def analyze(request):
    djtext = (request.POST.get("text", "default")) 
    #check box value
    removepunc = (request.POST.get("removepunc", "off")) 
    fullcaps = (request.POST.get("fullcaps", "off")) 
    newlineremover = (request.POST.get("newlineremover", "off")) 
    extraspaceremover = (request.POST.get("extraspaceremover", "off")) 
    charcount = (request.POST.get("charcount", "off")) 
    
    #check box is on
    if removepunc == "on":
        punctuations = '''!"#$%&'()*+, -./:;<=>?@[\]^_`{|}~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose':'Removed Punctuations', 'analyzed_text':analyzed}
        djtext = analyzed
    
    if(fullcaps == "on"):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose':'Changed to Uppercase', 'analyzed_text':analyzed}
        djtext = analyzed
    
    if(newlineremover == "on"):
        analyzed = ""
        for char in djtext:
            if char != "\n" and char != "\r":
                analyzed = analyzed + char
        params = {'purpose':'Remove The Newlines', 'analyzed_text':analyzed}
        djtext = analyzed
     
     
    if(extraspaceremover == "on"):
        analyzed = ""
        for index, char  in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index + 1]==" "):
                analyzed = analyzed + char
        params = {'purpose':'Extra Space Remover', 'analyzed_text':analyzed}
        djtext = analyzed
    
    if(charcount == "on"):
        analyzed = ""
        analyzed = djtext.count("e")
        
        params = {'purpose':'charcounts', 'analyzed_text':analyzed}
        djtext = analyzed
    if(removepunc != "on" and fullcaps != "on" and newlineremover != "on" and extraspaceremover != "on" and charcount != "on"):
        return HttpResponse("Please Select any from given Lines, Try Again!")
    
    return render(request, 'analyze.html', params)
    

