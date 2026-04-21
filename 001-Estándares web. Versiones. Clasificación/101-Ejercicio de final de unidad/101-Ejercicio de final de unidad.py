
print("Programa calculador del IRPF v0.1")
print("Por Raúl Ruiz-Cornejo Badia")

base_imponible = input("Introduce la base imponible: ")

base_imponible = float(base_imponible)

irpf = base_imponible * 0.15  

total = base_imponible - irpf 

print("Resultado del cálculo")
print("Tu base imponible:", base_imponible)
print("IRPF 15%:", irpf)
print("Total a recibir:", total)
