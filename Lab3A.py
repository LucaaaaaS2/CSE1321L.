#Credit Card
Owed = input("Amount owed:$")
Owed = float(Owed)
APR = input("APR:")
APR = float(APR)
MPR = APR / 12
MPR = float(round(MPR,3))
print(f"Monthly percentage rate: {MPR}")
actMPR = MPR/100
Min = Owed * actMPR
Min = float(round(Min,2))
print(f"Minimum payment: ${Min}")









