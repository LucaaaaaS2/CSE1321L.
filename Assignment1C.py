print("[Weight Conversion- Kilograms to Stones and Pounds]")
kg = float(input("Enter weight in kilograms: "))
#kg to lbs
lbs = kg * 2.20462
#remaining lbs
remaining = (lbs % 14)
#lbs to stone
stone = lbs // 14
print(f"{kg} kilograms is approximately {stone} stones and {remaining:.2f} pounds.")
