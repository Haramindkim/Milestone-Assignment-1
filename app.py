from datetime import datetime, timedelta

class Product:
    def __init__(self, id, full_name, description, price, status='active'):
        self.id = id
        self.name = full_name
        self.description = description
        self.price = price
        self.status = status
    
    def update(self, name=None, description=None, price=None):
        if name:
            self.name = name
        if description:
            self.description = description
        if price:
            self.price = price

    def suspend(self):
        self.status = 'suspended'
        
    def reactivate(self):
        self.status = 'active'
    
    def __str__(self):
        return f"Product [ID: {self.id}, \nFull Name: {self.name}, \nDescription: {self.description}, \nPrice: {self.price}, \nStatus: {self.status}]\n"

class Policyholder:
    def __init__(self, id, full_name, email, status='active'):
        self.id = id
        self.name = full_name
        self.email = email
        self.status = status
        self.products = []

    def add_product(self, product):
        self.products.append(product)
    
    def suspend(self):
        self.status = 'suspended'
    
    def reactivate(self):
        self.status = 'active'

    def __str__(self):
        products_str = ', '.join([str(product) for product in self.products])
        return f"Policyholder [ID: {self.id}, \nFull Name: {self.name}, \nEmail: {self.email}, \nStatus: {self.status}, \nProducts: {products_str}]\n"

class Payment:
    def __init__(self, id, policyholder_id, product_id, amount, due_date, date=None):
        self.id = id
        self.policyholder_id = policyholder_id
        self.product_id = product_id
        self.amount = amount
        self.due_date = due_date
        self.date = date
        self.paid = False
    
    def process_payment(self):
        self.paid = True
    
    def send_reminder(self):
        if not self.paid and datetime.now() > self.due_date:
            print(f"Reminder: Payment of {self.amount} for Policyholder ID: {self.policyholder_id} is overdue.")
    
    def apply_penalty(self, penalty_amount):
        if not self.paid and datetime.now() > self.due_date:
            self.amount += penalty_amount
            print(f"Penalty applied. New amount: {self.amount}")
    
    def __str__(self):
        return f"Payment [ID: {self.id}, \nPolicyholder ID: {self.policyholder_id}, \nProduct ID: {self.product_id}, \nAmount: {self.amount}, \nDue Date: {self.due_date}, \nPaid: {self.paid}]\n"

def main():
    # Create products
    product1 = Product(1, full_name="Hospital Insurance", description="Comprehensive hospital coverage", price=100.0)
    product2 = Product(2, full_name="Life Insurance", description="Complete life insurance coverage", price=150.0)

    # Create policyholders
    policyholders = [
        Policyholder(id=1, full_name="Divine Peter", email="pttyy@gmail.com"),
        Policyholder(id=2, full_name="Favyy Lakes", email="sephfav@gmail.com"),
        Policyholder(id=3, full_name="Greg Donald", email="Gdonald@rocketmail.com"),
    ]

    # add products to policyholders
    policyholders[0].add_product(product1)
    policyholders[1].add_product(product2)
    policyholders[2].add_product(product1)
    policyholders[3].add_product(product2)
    policyholders[4].add_product(product1)

    # Process payments
    due_date = datetime.now() + timedelta(days=30)  # Due date set to 30 days from now
    payments = [
        Payment(id=1, policyholder_id=1, product_id=1, amount=100.0, due_date=due_date),
        Payment(id=2, policyholder_id=2, product_id=2, amount=150.0, due_date=due_date),
        Payment(id=3, policyholder_id=3, product_id=1, amount=100.0, due_date=due_date)
    ]

    # Process all payments
    for payment in payments:
        payment.process_payment()

    # Display account details
    for policyholder in policyholders:
        print(policyholder)

    # Display payment details
    for payment in payments:
        print(payment)       
        
if __name__ == '__main__':
    main()
