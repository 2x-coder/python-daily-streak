'''Problem Statement
Input 
Temperature 
Pressure

Output
Safe
Warning
Danger'''

'''Process Safety Checker'''

#example1
temperature = float(input("Enter temperature(C): "))
pressure = float(input("Enter pressure(bar): "))

if temperature > 100:
    if pressure > 50:
        print("Danger")
    else:
        print("Warning")
else:
    print("Safe")


#example2
temperature = float(input("Enter temperature(C): "))
pressure = float(input("Enter pressure(bar): "))

if temperature > 120:
    if pressure > 80:
        print("Emergency Shutdown")
    else:
        print("High Temperature Warning")
else:
    if pressure > 80:
        print("High Temperature Warning")
    else:
        print("Normal Operation")

#example3
temperature = float(input("Boiler Temperature: "))
water_level = float(input("Water Level(%): "))




