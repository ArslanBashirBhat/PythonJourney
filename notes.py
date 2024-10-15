amount = int(input("Enter the amount: "))

if amount >= 500:
    notes500 = amount // 500
    print(f"{notes500} number of 500 Rs notes required")
    amount -= notes500 * 500

if amount >= 200:
    notes200 = amount // 200
    print(f"{notes200} number of 200 Rs notes required")
    amount -= notes200 * 200

if amount >= 100:
    notes100 = amount // 100
    print(f"{notes100} number of 100 Rs notes required")
    amount -= notes100 * 100

if amount >= 50:
    notes50 = amount // 50
    print(f"{notes50} number of 50 Rs notes required")
    amount -= notes50 * 50

if amount >= 20:
    notes20 = amount // 20
    print(f"{notes20} number of 20 Rs notes required")
    amount -= notes20 * 20

if amount >= 10:
    notes10 = amount // 10
    print(f" {notes10} number of 10 Rs notes required")
    amount -= notes10 * 10
if amount >= 5:
    notes5 = amount // 10
    print(f"{notes5} number of 5 Rs Coins Required")
    amount -= notes5 * 5

if amount >=2:
    notes2 = amount // 2
    print(f"{notes2} number of 2 Rs coins Required")
    amount -= notes2 * 2

if amount >=1 :
    notes1 = amount // 1
    print(f"{notes1} number of 1 Rs coins required")
