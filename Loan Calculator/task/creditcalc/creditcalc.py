from math import ceil
from math import log
import argparse


parser = argparse.ArgumentParser()
parser.add_argument("--type", choices=["annuity", "diff"])
parser.add_argument("--principal", type=int)
parser.add_argument("--periods", type=int)
parser.add_argument("--interest", type=float)
parser.add_argument("--payment", type=int)

type = parser.parse_args().type
principal = parser.parse_args().principal
periods = parser.parse_args().periods
interest = parser.parse_args().interest
payment = parser.parse_args().payment
accepted_types = ["annuity", "diff"]
arguments = [type, principal, periods, interest, payment]
number_of_args = 0

def annuity_principal(payment, periods, interest):
    i = interest / (12 * 100)
    principal = payment / ((i * pow(1 + i, periods)) / (pow(1 + i, periods) - 1))
    return ceil(principal)

if type not in accepted_types:
    print("Incorrect parameters.")
for arg in arguments:
    if arg is not None:
        number_of_args += 1
if number_of_args < 4:
    print("Incorrect parameters.")

if type == "diff" and principal and periods and interest:
    i = interest / (12 * 100)
    total_payment = 0
    for m in range(1, periods + 1):
        diff = ceil(principal / periods + i * (principal - principal * (m - 1) / periods))
        print("Month {}: payment is {}".format(m, diff))
        total_payment += diff
    print("Overpayment = ", total_payment - principal)
elif type == "diff":
    print("Incorrect parameters.")
if type == "annuity" and payment and periods and interest:
    loan_principal = annuity_principal(payment, periods, interest)
    print("Your loan principal =", loan_principal)
    print("Overpayment =", payment * periods - loan_principal)
elif type =="annuity" and principal and periods and interest:
    i = interest / (12 * 100)
    annuity_payment = ceil(principal * ((i * pow(1 + i, periods)) / (pow(1 + i, periods) - 1)))
    print("Your annuity payment =", annuity_payment)
    print("Overpayment =", annuity_payment * periods - principal)
elif type == "annuity" and principal and payment and interest:
    i = interest / (12 * 100)
    periods = ceil(log(payment / (payment - i * principal), 1 + i))
    years = periods // 12
    months = periods % 12
    if years == 0:
        print("It will take {} months to repay this loan!".format(months))
    elif months == 0:
        print("It will take {} years to repay this loan!".format(years))
    else:
        print("It will take {} years and {} months to repay this loan!".format(years, months))
    print("Overpayment =", payment * periods - principal)