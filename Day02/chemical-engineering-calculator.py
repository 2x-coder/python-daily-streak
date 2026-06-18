mass= float(input("enter mass in kg: "))
print(mass, "kg")
if mass <= 0:   
    print("mass cannot be zero or negative")
 
volume= float(input("enter volume in kg: "))
print(volume, "kg")
if volume <= 0:   
    print("volume cannot be zero or negative")
 
def calculate_density(mass, volume):
    return mass/volume
print(calculate_density, "kg/m^3")

result = calculate_density(mass, volume)
print(result)
