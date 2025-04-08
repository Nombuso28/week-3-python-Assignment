calculate_discount(amount, percentage_discount)

#Another POV

def calculate_discount (price, discount_percentage): #Defining the function and its parameters
  if discount_percentage >= 20: #Checking the condition of the discount percentage
    discount_amount = (price* discount_percentage)/100 #calculating the discount price
    new_price = price - discount_amount #checking the new price without the discount price
    return new_price #showing the new price
  else:
    return price #showing the default price
actual_price = float(input('enter_the_price')) #capturing the product price
percentage = float(input('enter the discount as a percentage:')) #capturing the price percentage
Mutego = calculate_discount(actual_price, percentage ) #calling the price (m)
print(Mutego)