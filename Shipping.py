weight = int(input("Please enter the weight of your parcel in lb: "))
premium_ground_shipping = 125.00

#Ground Shipping

if weight <= 2:
  price = (weight * 1.50) + 20
elif weight > 2 and weight <= 6:
  price = (weight * 3.00) + 20
elif weight > 6 and weight <= 10:
  price = (weight * 4.00) + 20
else:
  price = (weight * 4.75) + 20

#Drone Shipping

if weight <= 2:
  price_0 = (weight * 4.50)
elif weight > 2 and weight <= 6:
  price_0 = (weight * 9.00)
elif weight > 6 and weight <= 10:
  price_0 = (weight * 12.00)
else:
  price_0 = (weight * 14.25)

format_price = "{:.2f}".format(price)
print("\n" + "Ground Shipping: " + u"\u0024" + format_price)

format_premium_ground_shipping = "{:.2f}".format(premium_ground_shipping)
print("\n" + "Premium Ground Shipping: " + u"\u0024" + format_premium_ground_shipping)

format_price_0 = "{:.2f}".format(price_0)
print("\n" + "Drone Shipping: "+ u"\u0024" + format_price_0)