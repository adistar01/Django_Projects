from typing import Any, Dict
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView

from .forms import ReviewForm
from .models import Rview

# Create your views here.

class ReviewView(View):
    def get(self, request):
        form = ReviewForm()
        return render(request, "reviews/review.html", {
                "form":form
            })
    
    def post(self, request):
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/thank_you")


#def Review(request):
    #if request.method=='POST':
    #(    entered_username = request.POST['username']
    #    if entered_username=='':
    #        return render(request, "reviews/review.html", {
    #            "has_error": True
    #        })
    #    print(entered_username)
    #    return HttpResponseRedirect("/thank-you")
    #)
    #if request.method=='POST':
        #form = ReviewForm(request.POST)
        #if form.is_valid():
            #(review = Rview(
            #    user_name=form.cleaned_data['user_name'], 
            #    review_text=form.cleaned_data['review_text'], 
            #    rating=form.cleaned_data['rating'])
            #review.save()
            #)

            #form.save()
            #return HttpResponseRedirect("/thank_you")
    #else:
    #    form = ReviewForm()
    #
    #return render(request, "reviews/review.html", {
    #            "form":form
    #        })






#class Thanks(View):
#    def get(self, request):
#        return render(request, "reviews/thank_you.html")
#
#def Thanks(request):
#    return render(request, "reviews/thank_you.html")

class Thanks(TemplateView):
    template_name = "reviews/thank_you.html"

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["message"] = "This works!"
        return context
    



    

#class ReviewsListView(TemplateView):
#    template_name = "reviews/review_list.html"
#
#    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
#        context = super().get_context_data(**kwargs)
#        reviews = Rview.objects.all()
#        context["reviews"] = reviews
#        return context

class ReviewsListView(ListView):
    template_name = "reviews/review_list.html"
    model = Rview
    context_object_name = "reviews"

    #def get_queryset(self) -> QuerySet[Any]:
    #    base_query = super().get_queryset()
    #    data = base_query.filter(rating__gt=3)
    #    return data





    

#class ReviewDetail(TemplateView):
#    template_name = "reviews/review_detail.html"
#
#    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
#        context = super().get_context_data(**kwargs)
#        review_id = kwargs["id"]
#        review = Rview.objects.get(pk = review_id)
#        context["review"] = review
#        return context

class ReviewDetail(DetailView):
    template_name = "reviews/review_detail.html"
    model = Rview

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        loaded_review = self.object
        request = self.request
        fav_id = request.session.get("favorite_review")
        context["is_fav"] = fav_id==(str)(loaded_review.id)
        return context


class AddFavView(View):
    def post(self, request):
        review_id = request.POST["review_id"]
        request.session["favorite_review"] = review_id
        return HttpResponseRedirect("/re/" + review_id)