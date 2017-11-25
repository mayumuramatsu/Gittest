company_A = {'sales':100,'cost':80,'persons':10}
company_B = {'sales': 40,'cost':60,'persons':20}

def get_profit(sales,cost):
    return sales - cost

profit_A = get_profit(company_A['sales'],company_A['cost'])
profit_B = get_profit(company_B['sales'],company_B['cost'])

print (profit_A)
print (profit_B)
