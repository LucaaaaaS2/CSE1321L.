print("[Eletrical Energy Consumption Calaculator]")
volts = float(input("Enter the voltage (in volts): "))
ohms = float(input("Enter the resistance (in ohms): "))
hours = float(input("Enter the time the device was used (in hours): "))
temp1 = volts * volts
float(temp1)
temp2 = temp1 * hours
float(temp2)
temp3 = temp2 / ohms
float(temp3)
CONVERSION_FACTOR = temp3 / 1000
print(f"The device consumed {CONVERSION_FACTOR:.2f} kWh of energy.")
