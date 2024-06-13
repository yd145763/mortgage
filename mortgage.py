# -*- coding: utf-8 -*-
"""
Created on Thu Jun 13 16:23:29 2024

@author: limyu
"""

import streamlit as st

def mortgage_calculator(principal, interest_rate, years):
    monthly_interest_rate = interest_rate / 100 / 12
    num_payments = years * 12
    monthly_payment = principal * (
        monthly_interest_rate * (1 + monthly_interest_rate) ** num_payments
    ) / ((1 + monthly_interest_rate) ** num_payments - 1)
    total_payment = monthly_payment * num_payments
    return monthly_payment, total_payment

def main():
    st.title('Mortgage Calculator')
    
    principal = st.number_input('Enter loan amount ($)', min_value=0)
    interest_rate = st.number_input('Enter annual interest rate (%)', min_value=0.0, format="%.2f")
    years = st.number_input('Enter loan term (years)', min_value=1, step=1)
    
    if st.button('Calculate'):
        monthly_payment, total_payment = mortgage_calculator(principal, interest_rate, years)
        st.subheader('Results')
        st.write(f'Monthly Payment: ${monthly_payment:.2f}')
        st.write(f'Total Payment: ${total_payment:.2f}')

if __name__ == '__main__':
    main()
