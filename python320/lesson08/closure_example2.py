def discount_calculator(discount):
    def todays_discount(price):
        final_price = float(price) * (1 - float(discount))
        return f"After applying today's discount, you will pay {final_price}!"
    return todays_discount

if __name__ == "__main__":
    discount = input("What is today's discount? ")
    final_price = discount_calculator(discount)

    while True:
        price = input("Enter the regular price of the product: ")
        print(final_price(price))

