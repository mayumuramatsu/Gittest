class company:
    def __init__(self, sales, cost, persons):
        self.sales   = sales
        self.cost    = cost
        self.persons = persons

    def get_profit(self):
        return self.sales - self.cost

company_A = company(100, 80, 10)
company_B = company( 40, 60, 20)

company_A.sales = 80
print (company_A.sales)
print (company_A.get_profit())
