from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.template import loader
from rest_framework.response import Response

from rest_framework.views import APIView
from rest_framework.decorators import api_view

import json
#from .forms import MortgageForm
from .formulas import mortgage_schedule, payment_formula

def index(request):
    return render(request, 'frCalculator/index.html')

def get_mortgage_schedule(request):
    if request.method == 'POST':
        #form = MortgageForm(request.POST)
        home_price = int(request.POST.get("home_price"))
        deposit_percent = float(request.POST.get("deposit_percent"))
        interest_rate = float(request.POST.get("interest_rate"))
        loan_term = int(request.POST.get("loan_term"))
        schedule, total_repayment, total_interest, total_principal = \
            mortgage_schedule(home_price, deposit_percent, interest_rate, loan_term)

        return HttpResponse(json.dumps({'monthly_schedule': schedule, 'total_interest': total_interest,
                                       'total_principal': total_principal}), content_type='application/json')

#Bibliography
#https://stackoverflow.com/questions/37341679/django-2-csrf-tokens