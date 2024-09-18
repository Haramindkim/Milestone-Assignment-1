# Insurance Management System

This Python script implements a basic Insurance Management System with classes for Products, Policyholders, and Payments.

## Features

1. Product Management
   - Create and manage insurance products
   - Update product details
   - Suspend and reactivate products

2. Policyholder Management
   - Create and manage policyholders
   - Add products to policyholders
   - Suspend and reactivate policyholders

3. Payment Processing
   - Create and manage payments
   - Process payments
   - Send reminders for overdue payments
   - Apply penalties for late payments

## Classes

### Product

Represents an insurance product with the following attributes:
- ID
- Full Name
- Description
- Price
- Status (active/suspended)

Methods include:
- `update()`: Update product details
- `suspend()`: Suspend the product
- `reactivate()`: Reactivate the product

### Policyholder

Represents a policyholder with the following attributes:
- ID
- Full Name
- Email
- Status (active/suspended)
- Products (list of associated products)

Methods include:
- `add_product()`: Add a product to the policyholder
- `suspend()`: Suspend the policyholder
- `reactivate()`: Reactivate the policyholder

### Payment

Represents a payment with the following attributes:
- ID
- Policyholder ID
- Product ID
- Amount
- Due Date
- Payment Date
- Paid Status

Methods include:
- `process_payment()`: Mark the payment as paid
- `send_reminder()`: Send a reminder for overdue payments
- `apply_penalty()`: Apply a penalty for late payments

## Usage

The `main()` function demonstrates the usage of these classes:

1. Creates sample products
2. Creates sample policyholders
3. Adds products to policyholders
4. Creates and processes sample payments
5. Displays policyholder and payment details

To run the script, execute:

```
python app.py
```
