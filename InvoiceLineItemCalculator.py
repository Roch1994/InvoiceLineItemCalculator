# Rochelle Mellette, InvoiceLineItemCalculator, CIS261
def get_price():
  """Prompts the user for a price, validates it as a float, and returns it."""
  while True:
    try:
      price = float(input("Enter price: "))
      return price
    except ValueError:
      print("Invalid decimal number. Please try again.")

def get_quantity():
  """Prompts the user for a quantity, validates it as an integer, and returns it."""
  while True:
    try:
      quantity = int(input("Enter quantity: "))
      return quantity
    except ValueError:
      print("Invalid integer. Please try again.")

def main():
  """Calculates and displays line item totals for an invoice."""

  print("The Invoice Line Item Calculator\n")

  while True:
    price = get_price()
    quantity = get_quantity()

    total = price * quantity

    print(f"PRICE: {price:19.2f}")  # Format price with 2 decimal places
    print(f"QUANTITY:{quantity:10}")
    print(f"TOTAL: {total:22.2f}")  # Format total with 2 decimal places

    another_item = input("Enter another line item? (y/n): ")
    if another_item.lower() != 'y':
      break

  print("\nBye!")

if __name__ == "__main__":
  main()