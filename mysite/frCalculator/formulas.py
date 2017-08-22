
def payment_formula(principal, interest, years):
    """""
    A = periodic payment amount
    principal_balance = amount of principal, net of initial payments, meaning"subtract any down-payments"
    i = periodic(e.g. monthly) interest rate
    n = total number of payments, i.e. loan term
"""

    i = interest/12
    n = years * 12
    A = round((principal * i) / (1 - (1 + i)**-n), 2)
    principal_balance = principal

    return i, n, A, principal_balance

def mortgage_schedule(home_price, deposit_percent, interest_rate, loan_term):

    #how much client wants to borrow
    principal = home_price * (1 - deposit_percent)
    i, n, A, principal_balance = payment_formula(principal, interest_rate, loan_term)
    month_iterator = []
    for month in range(n):
        #the interest_accrued decreases proportionally to  principal_balance as mortgage matures
        interest_accrued = round(i * principal_balance, 2)
        pre_payment_balance = round(interest_accrued + principal_balance,2)
        principal_payment = round(A - interest_accrued, 2)
        loan_balance = round(pre_payment_balance - A, 2)

        month_iterator.append([A, interest_accrued, principal_payment, pre_payment_balance, loan_balance])

        #iteratively diminishing principal
        principal_balance = principal_balance - principal_payment

    total_repayment = A * n
    total_interest = sum([month[1] for month in month_iterator])
    total_principal = sum([month[2] for month in month_iterator])

    print(month_iterator)

    return month_iterator, total_repayment, total_interest, total_principal




#extend into a class
#return a monthly schedule and yearly schedule
#add a interest to principal ratio


#bibliography
#https://en.wikipedia.org/wiki/Amortization_calculator
#http://www.investopedia.com/terms/f/fullyindexedinterestrate.asp
#https://stackoverflow.com/questions/20306981/how-do-i-integrate-ajax-with-django-applications
