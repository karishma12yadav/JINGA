from django.shortcuts import render

# Create your views here.
def placeorder(request):
    return render(request, 'placeorder.html')