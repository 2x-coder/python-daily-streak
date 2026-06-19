'''Creating a Dictionary'''
elements = {
    "H": 1,
    "He": 4,
    "Li": 6,
    "Be": 9,
    "B": 10,
    "C": 12,
    "N": 14,
    "O": 16,
}

print("Molar Mass Calculator")

h = int(input("number of h atoms:"))
c = int(input("number of c atoms:"))
o = int(input("number of o atoms:"))

molar_mass = (
    h*elements["H"]+
    c*elements["C"]+
    o*elements["O"]
)

print("Molar Mass =", molar_mass, "g/mol")