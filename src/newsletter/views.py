from django.shortcuts import render
from .forms import SignUpForm


def home(request):
    title = "Welcome"
    form = SignUpForm(request.POST or None)
    context = {
        "title": title,
        "form": form
    }
    # if request.method == "POST":
    #     print request.POST
    # if request.user.is_authenticated():
    #     title = "My Title %s" %(request.user)
    if form.is_valid():
        # form.save()
        instance = form.save(commit=False)
        full_name = form.cleaned_data.get("full_name")
        if not full_name:
            full_name = "New Name"
        instance.full_name = full_name
        #
        instance.save()
        # print instance
        # print instance.timestamp
        context ={
            "title": "Thank You"
        }

    return render(request, 'home.html', context)