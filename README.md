

---

# Shopping Cart Python Program

This Python program allows users to create a shopping cart with multiple products, each with its own price. The shopping cart calculates the total price, applies the most beneficial discount rule (from a pre-defined set), and calculates gift wrapping and shipping fees based on the quantities of each product.

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/your_username/shopping_cart_python
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

Hope this README provides sufficient information for your GitHub post. Make sure to replace `your_username` with your actual GitHub username in the clone URL.
