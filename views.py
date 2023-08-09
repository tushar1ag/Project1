from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def analyze(request):
    djtext=request.GET.get('text', 'off')
    charcount = request.GET.get('charcount', 'off')
    extraspace = request.GET.get('extraspace', 'off')
    removepunc=request.GET.get('removepunc', 'off')
    uppercase=request.GET.get('uppercase', 'off')

    if charcount=="on":
        analyzed=""
        counts=0
        for char in djtext:
            counts=counts+1
        params = {'purpose': 'count the characters', 'analyzed_text': analyzed, 'count': counts}

    if removepunc=="on":
       analyzed=""
       punctions='''!"#$%&'()*+, -./:;<=>?@[\]^_`{|}'''
       for char in djtext:
          if char not in punctions:
             analyzed=analyzed+char
       params = {'purpose': 'remove punctuatios', 'analyzed_text': analyzed, 'count':counts}
       djtext = analyzed

    if uppercase=="on":
        analyzed=""
        for char in djtext:
            analyzed=analyzed + char.upper()
        params = {'purpose': 'counvert to upppercase', 'analyzed_text': analyzed, 'count': counts}
        djtext = analyzed

    if extraspace=="on":
        analyzed=""
        for index,char in enumerate(djtext):
            if djtext[index]==" " and djtext[index+1]==" ":
                pass
            else:
                analyzed=analyzed+char
        params = {'purpose': 'remove extra space', 'analyzed_text': analyzed, 'count': counts}
        djtext=analyzed

    if removepunc !="on" and uppercase!="on" and charcount!="on":
        return HttpResponse("please select one option to prroceed")

    return render(request, 'analyze.html', params)