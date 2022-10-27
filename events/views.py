from django.shortcuts import render

# Create your views here.
def event_main(request):
    return render(request, "main.html", {})