from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def payment(request):
    # print(request.GET.get('next'))
    return render(request, 'payment.html')