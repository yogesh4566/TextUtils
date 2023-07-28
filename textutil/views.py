from django.shortcuts import render, HttpResponse

def index(request):
    return render(request, 'index.html')


def about(request):
    return HttpResponse("<h1>Yogesh</h1>")


def removepunc(request):
    return HttpResponse("remove punc")


def capfirst(request):
    return HttpResponse("capitalize first")


def newlineremove(request):
    return HttpResponse("newlineremove")


def spaceremove(request):
    return HttpResponse("spaceremove")


def charcount(request):
    return HttpResponse("Charcount")

def analyze(request):
    # Get the text
    djtext = request.POST.get('text','default')
    print(djtext)

    # Check checbox values
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    lowercase = request.POST.get('lowercase', 'off')
    newlineremove = request.POST.get('newlineremove', 'off')
    spaceremove = request.POST.get('spaceremove', 'off')
    charcount = request.POST.get('charcount', 'off')
    
      # Check Which Checkbox is on
    if removepunc == "on":
       punctuations = '''!(){};:'"\,<>./?@#$%^&*_~'''
       analyzed = ""
       for char in djtext:
           if char not in punctuations:
              analyzed = analyzed + char
       params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
       djtext = analyzed
    #    return render(request, 'analyze.html', params)
   
    if(fullcaps=="on"):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
            
        params = {'purpose': 'Changed to Uppercase', 'analyzed_text': analyzed}
        djtext = analyzed
        # return render(request, 'analyze.html', params)
    
    if(lowercase=="on"):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.lower()
        params = {'purpose': 'Changed to Lowercase', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)

    if(newlineremove=="on"):
        analyzed = ""
        for char in djtext:
            if char != "\n" and char!="\r":
               analyzed = analyzed + char
        params = {'purpose': 'Removed Newline', 'analyzed_text': analyzed}
        djtext = analyzed
        # return render(request, 'analyze.html', params)

    if(spaceremove=="on"):
        analyzed= ""
        for index, char in enumerate(djtext):
            if djtext[index] ==" " and djtext[index+1]==" ":
               pass
               analyzed = analyzed + char
        
        params = {'purpose': 'Removed Newline', 'analyzed_text': analyzed}
        djtext = analyzed
        # return render(request, 'analyze.html', params)  
      
    # else:
    #   return HttpResponse("Error")
    if(removepunc != "on" and fullcaps!="on" and lowercase!="on" and newlineremove!="on" and spaceremove!="on"):
        return HttpResponse("Please select the operator")
    return render(request, 'analyze.html', params)  
