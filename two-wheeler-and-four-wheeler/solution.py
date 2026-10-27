# V - Total number of vehichles
# W - Total Number of Wheels

# T - Number of two wheeler
# F - Number of four wheeler
V = int(input("Number of Vehichles:"))
W = int(input("Number of Wheels:"))

T = (W - 4*V)//-2

F = V - T 

print(f'TW: {T} FW: {F}')