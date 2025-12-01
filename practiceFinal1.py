comp_time = 15
comp_time_bit = 39
server_time = 19
server_time_bit = 57

total_comp = 0
total_comp_bit = 0
total_server = 0
total_server_bit = 0

department = 1

print("[Post-Crowdstrike Plan]")
while True:
    print(f"department {department}")
    computer = int(input("How many computers need to be fixed? "))
    comp_bit = int(input("How many of those have Bitlocker enabled?"))
    server = int(input("How many servers need to be fixed?"))
    server_bit = int(input("How many of those have Bitlocker enabled?"))

    computer += total_comp
    comp_bit += total_comp_bit
    server += total_server
    server_bit += total_server_bit

    another = input("Is there another department?")
    if another != Y:
        break

    department += 1

total_comp = total_comp - total_comp_bit
total_server = total_server - total_server_bit

total_time_comp = comp_time * total_comp
total_time_compbit = comp_time_bit * total_comp_bit
total_time_server = server_time * total_server
total_time_serverbit = server_time_bit * total_server_bit

total = int(total_time_comp + total_time_compbit + total_time_server + total_time_serverbit)

print(f"Across all departments, there are {total_comp} computers and {total_server} servers. Of those, {total_comp_bit} computers and {total_server_bit} servers had Bitlocker enabled")
print(f"The {total_comp} computers without Bitlocker will take {total_time_comp} to fix")
print(f"The {total_comp_bit} computers with Bitlocker will take {total_time_compbit} to fix")
print(f"The {total_server} servers without Bitlocker will take {total_time_server} to fix")
print(f"The {total_server_bit} servers with Bitlocker will take {total_time_serverbit} to fix")
print(f"Assuming we fix them one at a time, it will take {total} to repair all devices")
