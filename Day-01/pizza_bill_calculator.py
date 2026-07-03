# Pizza Bill Calculator

print("Welcome To Pizza Bill Calculator 🍕")
pizza_price = float(input(("Enter Pizza Price: ")))
gst = float(input("Enter the GST(%): "))
tip = float(input("Enter Tip(%): "))
coupon = input("Do you have a coupon? (Yes/No):").lower()
coupon_amt = 0
if coupon == "yes":
    coupon_amt = float(input("Enter coupon amount:"))
gst_in_price = (gst / 100) * pizza_price
tip_in_price = (tip / 100) * pizza_price
total_bill = pizza_price + gst_in_price + tip_in_price - coupon_amt
line = "-" * 25
print(line)
print(f"Pizza Price : ${pizza_price:.2f}")
print(f"Coupon      : ${coupon_amt:.2f}")
print(f"GST         : ${gst_in_price:.2f}")
print(f"Tip         : ${tip_in_price:.2f}")
print(line)
print(f"Total Bill : ${total_bill:.2f}")
friends = int(input("How many friends are sharing the bill? "))
if friends > 0:
    each_should_pay = total_bill / friends
    print(f"Each friend should pay ${each_should_pay:.2f}")
    print("----Hope you enjoy your pizza🍕!----")
else:
    print("Number of friends must be graeter then 0.")
    print("----Hope you enjoy your pizza🍕!----")
print("---------Thank You, Visit Again!--------")