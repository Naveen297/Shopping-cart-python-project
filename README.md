

---

# Shopping Cart Python Program

This Python program allows users to create a shopping cart with multiple products, each with its own price. The shopping cart calculates the total price, applies the most beneficial discount rule (from a pre-defined set), and calculates gift wrapping and shipping fees based on the quantities of each product.

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/Naveen297/shopping_cart_python
   ```
2. Navigate into the cloned repository:
   ```
   cd shopping_cart_python
   ```
3. Run the script:
   ```
   python main.py
   ```

## How it Works

### 1. Define the Products

Products are defined as instances of the `Product` class, each with its own name and price. 

```python
product_A = Product("Product A", 20)
product_B = Product("Product B", 40)
product_C = Product("Product C", 50)
```

### 2. Create a Shopping Cart

Create a new shopping cart using the `ShoppingCart` class.

```python
cart = ShoppingCart()
```

### 3. Add Products to the Shopping Cart

You can add products to the shopping cart, specifying the quantity of the product and whether it should be gift wrapped. This will be asked interactively to the user.

```python
for product in [product_A, product_B, product_C]:
    quantity = int(input(f"Enter the quantity for {product.name}: "))
    is_gift_wrapped = input(f"Do you want {product.name} to be gift wrapped? (yes/no): ") == 'yes'
    cart.add_product(product, quantity, is_gift_wrapped)
```

### 4. Checkout

To calculate the total price (including discounts and additional fees), use the `checkout` method.

```python
cart.checkout()
```

## Discount Rules

The program includes four types of discounts:

1. `flat_10_discount`: If the cart total exceeds $200, a $10 discount is applied.
2. `bulk_5_discount`: If the quantity of a single product exceeds 10 units, a 5% discount is applied to that product's total price.
3. `bulk_10_discount`: If the total quantity of products exceeds 20 units, a 10% discount is applied to the cart total.
4. `tiered_50_discount`: If the total quantity exceeds 30 units and the quantity of any single product is greater than 15, a 50% discount is applied to products that exceed the 15 quantity.

## Additional Fees

1. **Gift wrap fee**: $1 per unit.
2. **Shipping fee**: 10 units can be packed in one package, and the shipping fee for each package is $5.

---

## Program Workflow

1. **Product Definition**: The program starts with defining the products available for purchase. Each product is an instance of the `Product` class, which has attributes like name and price.

2. **Shopping Cart Creation**: A shopping cart is created as an instance of the `ShoppingCart` class. The cart keeps track of the added products, their quantities, and if they are gift-wrapped or not.

3. **Adding Products**: The program then asks the user interactively about the quantity of each product they want to purchase and whether they want it to be gift-wrapped.

4. **Checkout**: The `checkout` method in the `ShoppingCart` class calculates the total cost of the products, applies the best discount available, and adds the gift wrapping and shipping fees.

### Discount Calculation

The `ShoppingCart` class has methods to calculate different types of discounts:

- The `flat_10_discount` method calculates a flat 10% discount if the total cost exceeds $200.
- The `bulk_5_discount` method calculates a 5% discount on any product whose quantity exceeds 10.
- The `bulk_10_discount` method calculates a 10% discount on the total if the total number of products exceeds 20.
- The `tiered_50_discount` method calculates a 50% discount on the cost of any product whose quantity exceeds 15, but only for the units exceeding 15.

The `apply_discount` method calculates all these discounts and applies the best one (i.e., the one resulting in the highest discount).

### Fee Calculation

The `calculate_fees` method in the `ShoppingCart` class calculates the gift wrapping and shipping fees. Gift wrapping costs $1 per unit. For shipping, 10 units can be packed into one package, and each package costs $5.

### Final Total Calculation

Finally, the `checkout` method displays the names, quantities, and total costs of the products, the subtotal (i.e., the total cost before discounts and fees), the applied discount and its amount, the gift wrapping and shipping fees, and the final total after applying the discount and adding the fees.
### My Resume
```
https://rxresu.me/r/6gs2_6NY
```
