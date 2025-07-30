'''code to illustate a product with its price by normal instance and calculate the product tax rate by 10% in a class method 
and print the total amount to paid
'''

class product:
    tax_rate=0.18
    def __init__(self, name, price):
        self.name = name
        self.price = price
    def finalprice(self):
        total=self.price*(1+product.tax_rate)
        print(f"final price of {self.name} is Rs.{total:.2f}")
    @classmethod
    def settax(cls, rate):
            cls.tax_rate = rate/100
name=str(input("Enter the product name:"))
price=float(input("Enter the product price:"))
rate=int(input("Enter the tax rate in %:"))
product.settax(rate)
item= product(name,price)
item.finalprice()