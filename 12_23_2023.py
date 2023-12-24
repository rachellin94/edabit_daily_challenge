# Convert Minutes into Seconds
def convert(minutes):
	mins_to_seconds = minutes * 60
	return mins_to_seconds
  
# Find the Discount
# Create a function that takes two arguments: the original price and the discount percentage as integers and returns the final price after the discount.
# Examples
# dis(1500, 50) ➞ 750

def dis(price, discount):
    price = int(price)
    discount = float(discount / 100)
    final_discount = 1 - discount 
    total_price = price * final_discount
    round_price = round(total_price, 2)
    return round_price 
