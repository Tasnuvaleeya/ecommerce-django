from django.shortcuts import render
from .forms import SignUpForm, ContactForm


def home(request):
    title = "Welcome"
    form = SignUpForm(request.POST or None)
    context = {
        "title": title,
        "form": form
    }

    if form.is_valid():
        # form.save()
        instance = form.save(commit=False)
        full_name = form.cleaned_data.get("full_name")
        if not full_name:
            full_name = "New Name"
        instance.full_name = full_name
        #
        instance.save()

        context ={
            "title": "Thank You"
        }

    return render(request, 'home.html', context)


def contact(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        for key,value in form.cleaned_data.iteritems():
            print key,value
            # print form.cleaned_data.get(key)
        # email = form.cleaned_data.get("email")
        # full_name = form.cleaned_data.get("full_name")
        # message = form.cleaned_data.get("message")
        # print email,message,full_name

    context ={
        "form" :form,
    }
    return render(request,"forms.html",context)