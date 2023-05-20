class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class ShoppingCart:
    def __init__(self):
        self.items = {}
        self.total = 0
        self.total_units = 0
        self.gift_wrap_units = 0
        self.shipping_units = 0

    def add_product(self, product, quantity, is_gift_wrapped):
        self.items[product.name] = {'product': product, 'quantity': quantity}
        self.total += product.price * quantity
        self.total_units += quantity
        if is_gift_wrapped:
            self.gift_wrap_units += quantity
        self.shipping_units += -(-quantity // 10)  # Equivalent to ceiling division

    def apply_discount(self):
        discounts = {'flat_10_discount': self.flat_10_discount(),
                     'bulk_5_discount': self.bulk_5_discount(),
                     'bulk_10_discount': self.bulk_10_discount(),
                     'tiered_50_discount': self.tiered_50_discount()}

        best_discount_name = max(discounts, key=discounts.get)
        self.total -= discounts[best_discount_name]
        return best_discount_name, discounts[best_discount_name]

    def flat_10_discount(self):
        return self.total * 0.1 if self.total > 200 else 0

    def bulk_5_discount(self):
        return sum(
            [item['product'].price * item['quantity'] * 0.05 for item in self.items.values() if item['quantity'] > 10])

    def bulk_10_discount(self):
        return self.total * 0.1 if self.total_units > 20 else 0

    def tiered_50_discount(self):
        return sum([item['product'].price * (item['quantity'] - 15) * 0.5 if item['quantity'] > 15 else 0 for item in
                    self.items.values()])

    def calculate_fees(self):
        gift_wrap_fee = self.gift_wrap_units * 1
        shipping_fee = self.shipping_units * 5
        return gift_wrap_fee, shipping_fee

    def checkout(self):
        print("Cart Items:\n")
        for item in self.items.values():
            print(
                f"Product Name: {item['product'].name}, Quantity: {item['quantity']}, Total: ${item['product'].price * item['quantity']}")

        print(f"\nSubtotal: ${self.total}")

        discounts = {'flat_10_discount': self.flat_10_discount(),
                     'bulk_5_discount': self.bulk_5_discount(),
                     'bulk_10_discount': self.bulk_10_discount(),
                     'tiered_50_discount': self.tiered_50_discount()}

        print("\nAvailable Discounts:")
        for discount_name, discount_amount in discounts.items():
            if discount_amount > 0:
                print(f"{discount_name}: ${discount_amount}")

        best_discount_name = max(discounts, key=discounts.get)
        print(f"\nBest Discount Applied: {best_discount_name}, Discount Amount: ${discounts[best_discount_name]}")
        self.total -= discounts[best_discount_name]

        gift_wrap_fee, shipping_fee = self.calculate_fees()
        print(f"\nGift Wrap Fee: ${gift_wrap_fee}, Shipping Fee: ${shipping_fee}")

        self.total += gift_wrap_fee + shipping_fee

        print(f"\nTotal: ${self.total}")


product_A = Product("Product A", 20)
product_B = Product("Product B", 40)
product_C = Product("Product C", 50)

cart = ShoppingCart()

for product in [product_A, product_B, product_C]:
    quantity = int(input(f"Enter the quantity for {product.name}: "))
    is_gift_wrapped = input(f"Do you want {product.name} to be gift wrapped? (yes/no): ") == 'yes'
    cart.add_product(product, quantity, is_gift_wrapped)

cart.checkout()
