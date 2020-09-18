def calculate_amortization_amount(principal, interest_rate, period):
    i = interest_rate /(12*100)
    j= (1+i) ** period
    x = (principal * i *j) / (j -1)
    return x

print(calculate_amortization_amount(300000,4.2,30*12))