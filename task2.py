zahl=10
kommazahl=10.5
text="Hello,World!"
wahrheitswert=True

print(f"Integer (zahl): {zahl}")
print(f"Floating-Point (kommazahl): {kommazahl}")
print(f"String (text): {text}")
print(f"Boolean (wahrheitswert): {wahrheitswert}")

print("\nType of Zahl is "+(type(zahl).__name__))
print("Type of kommazahl is "+(type(kommazahl).__name__))
print("Type of text is "+(type(text).__name__))
print("Type of wahrheitswert is "+(type(wahrheitswert).__name__))