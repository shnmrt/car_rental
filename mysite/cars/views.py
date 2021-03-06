from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import ReviewForm
# Create your views here.

def rental_review(request):
    # POST REQUEST ----> FORMS CONTENTS ---> THANK YOU
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            #{'firs_name': ..,}
            form.save()
            print(form.cleaned_data)
            return redirect(reverse('cars:thank_you'))
    else:
        form = ReviewForm()
    #ELSE RENDER FORM
    return render(request, 'cars/rental_review.html', context={'form':form})

def thank_you(request):
    return render(request, 'cars/thank_you.html' )
