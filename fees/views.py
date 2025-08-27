from django.shortcuts import render
from .models import Fee

def fee_list(request):
    fees = Fee.objects.all()
    return render(request, 'fees/fee_list.html', {'fees': fees})