def calculate_discount(price,discount_percent):
    if discount_percent >= 20:
       new_amount= price * discount_percent/100
       final_price = price - new_amount
       return final_price
    else: 
        return price
price=float(input("Enter the price: "))
discount_percent=float(input("Enter the percentage: "))
final_price=calculate_discount(price,discount_percent)

print(f"The final price: {final_price: .2f}")