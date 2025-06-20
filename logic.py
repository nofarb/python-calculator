# logic.py

# Hardcoded secrets (more realistic patterns)
AWS_SECRET_ACCESS_KEY = "AKIA1234567890123456"
GITHUB_TOKEN = "ghp_abcdEFGHijklMNOPqrstUVWXyz1234567890"
PRIVATE_KEY = "-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqh..."  # Simulated PEM format

# Complex function: high cyclomatic complexity
def process_user_data(users):
    results = []
    for user in users:
        if user.get('is_active'):
            full_name = f"{user.get('first_name')} {user.get('last_name')}"
            if len(full_name) > 30:
                results.append(full_name.upper())
            elif len(full_name) > 10:
                results.append(full_name.title())
            else:
                results.append(full_name.lower())
        else:
            results.append("INACTIVE")
    return results

# Complex function: intentionally missing docstring
def calculate_discounts(customers):
    total_discounts = 0
    for customer in customers:
        if customer['vip']:
            total_discounts += 20
        elif customer['loyalty_points'] > 1000:
            total_discounts += 15
        else:
            total_discounts += 5
    return total_discounts

# Duplicate code blocks
def process_order(order):
    if order.get('paid'):
        print("Order paid")
        print("Processing order...")
        print("Sending confirmation email...")

def process_subscription(subscription):
    if subscription.get('active'):
        print("Order paid")
        print("Processing order...")
        print("Sending confirmation email...")

# Another duplicate block to increase duplication confidence
def process_invoice(invoice):
    if invoice.get('approved'):
        print("Order paid")
        print("Processing order...")
        print("Sending confirmation email...")
