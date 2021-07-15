from django.shortcuts import render
from django.views.generic import View
from django.http import JsonResponse

from model import prediction
from .forms import NewsForm

class Verify(View) :
    form_class  = NewsForm
   
    def post(self,request,*args,**kwargs) :
        feedback = {}
        form = self.form_class(request.POST)

        if form.is_valid() :
            news = form.cleaned_data['news']
            
            #call predict script
            results = prediction.detect_fake_news(news)
            
            #receive feedback
            feedback['validity'] = results[0]
            feedback['accuracy'] = results[1]
            


        else :
            feedback['error'] = form.news.errors

        return JsonResponse(feedback)    



