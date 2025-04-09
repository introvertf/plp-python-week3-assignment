def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price
    return price

def main():
    
    try:
        print("-----Welcome to the Discount Calculator------!")
        original_price = float(input("Enter the original price of the item:"))
        discount_percentage = float(input("Enter the discount percentage: "))

        
        final_price = calculate_discount(original_price,discount_percentage)

        
        if final_price < original_price:
            print(f"\nOriginal Price:{original_price:.2f}")
            print(f"Discount Applied: {discount_percentage}%")
            print(f"Final Price:{final_price:.2f}")
        else:
            print(f"\nNo discount applied. Original price: {original_price:.2f}")
            print("(Minimum 20% discount required to apply discount)")

    except ValueError:
        print("Please enter valid numerical values!")

if __name__ == "__main__":
    main()