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
            print(results[1])
            feedback['validity'] = str(results[0])
            feedback['score'] = "{}%".format(round(results[1] * 100,2))
            feedback['success'] = True


        else :
            feedback['error'] = "Information entered Failed Validation"

        return JsonResponse(feedback)    



