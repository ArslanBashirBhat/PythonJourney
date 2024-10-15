cost_price = int(input("Enter Cost Price of Product :"))
selling_price = int(input("Enter Selling Price of Product :"))
profit = selling_price - cost_price
loss = cost_price - selling_price
if profit > 0:
    print(f"You are {profit} Rs in Profit")
elif loss > 0:
    print(f"You are {loss} Rs in Loss")
else :
    print("You are Neither in Profit nor Loss")