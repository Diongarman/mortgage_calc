from django import forms

class MortgageForm(forms.Form):
    home_price = forms.FloatField(label="home_price")
    deposit_percent = forms.FloatField(label="deposit_percent")
    interest_rate = forms.FloatField(label="interest_rate")
    loan_term = forms.IntegerField(label="loan_term")

