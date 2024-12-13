# -*- coding: utf-8 -*-
"""PrettyClick Makeup Management System.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1ge2tPFGCBhFjK4xzwsiFc5joiel-Uzez
"""

class MakeupProduct:
  def __init__(self, name, category, price, stock):
    self.name = name
    self.category = category
    self.price = price
    self.stock = stock

  def is_available(self, quantity):
    return self.stock >= quantity

  def reduce_stock(self, quantity):
    if self.is_available(quantity):
      self.stock -= quantity
    else:
      raise ValueError(f'Only {self.stock} units of {self.name} are available.')

  def __str__(self):
    return f"{self.name} ({self.category}) - NPR {self.price} | Stock: {self.stock}"


class PrettyClick:
  def __init__(self):
    self.products = []

  def add_product(self, product):
    self.products.append(product)

  def view_products(self):
    print("Available Products:")
    for product in self.products:
      print(product)
    print()

  def search_by_category(self, category):
    print(f"Products in category '{category}':")
    for product in self.products:
      if product.category.lower() == category.lower():
        print(product)
    print()

  def buy_products(self, product_name, quantity):
    for product in self.products:
      if product.name.lower() == product_name.lower():
        if product.is_available(quantity):
          product.reduce_stock(quantity)
          print(f"Purchased {quantity} * {product.name}")
          return product.price * quantity
        else:
          print(f"Not enough stock for {product.name}.")
          return 0
    print(f"Product '{product_name}' not found")
    return 0


  def generate_bill(self, purchases):
    print("\n----- Preetyclick Store")
    total = 0
    for product_name, quantity in purchases.items():
      cost = self.buy_products(product_name, quantity)
      if cost > 0:
        total += cost
    print(f"Customer your Total Amount: NPR {total}\n")
    print("Thank you for shopping with us!")
    print("----- Preety click Store")

store = PrettyClick()

store.add_product(MakeupProduct("Maybelline SuperStay Lipstick", "Lipstick", 1200, 15))
store.add_product(MakeupProduct("L'Oréal Paris True Match Foundation", "Foundation", 1800, 10))
store.add_product(MakeupProduct("Lakme Absolute Shine Eyeliner", "Eyeliner", 400, 20))
store.add_product(MakeupProduct("Neutrogena Hydro Boost Gel Cream", "Skincare", 2500, 8))
store.add_product(MakeupProduct("The Ordinary Niacinamide Serum", "Skincare", 2300, 12))
store.add_product(MakeupProduct("Revlon Ultra HD Matte Lipcolor", "Lipstick", 1300, 18))
store.add_product(MakeupProduct("MAC Studio Fix Fluid Foundation", "Foundation", 4200, 6))
store.add_product(MakeupProduct("Himalaya Purifying Neem Face Wash", "Skincare", 350, 25))
store.add_product(MakeupProduct("Garnier Bright Complete Vitamin C Serum", "Skincare", 900, 20))
store.add_product(MakeupProduct("Wet n Wild MegaGlow Highlighter", "Highlighter", 600, 14))

store.view_products()

store.search_by_category("Lipstick")

purchases = {"Lakme Absolute Shine Eyeliner":2, "Himalaya Purifying Neem Face Wash": 3, "Wet n Wild MegaGlow Highlighter": 1}
store.generate_bill(purchases)

