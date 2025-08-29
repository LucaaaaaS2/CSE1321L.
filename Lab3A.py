#Credit Card
Owed = input("Amount owed:$")
Owed = float(Owed)
APR = input("APR:")
APR = float(APR)
MPR = APR / 12
roundedMPR = float(round(MPR,3))
print(f"Monthly percentage rate: {roundedMPR}")
actMPR = MPR/100
Min = Owed * actMPR
Min = float(round(Min,2))
print(f"Minimum payment: ${Min}")









