def calculaIRPF(importe):
  irpf = importe * 0.15   
  return irpf

def calculoTotal(base, irpf):
  total = base - irpf     
  return total



print("Programa calculadora de facturas v0.1 Jose Vicente Carratala")
base = input("Introduce la base de la factura: ")
base_numerico = float(base)


irpf = calculaIRPF(base_numerico)
total_factura = calculoTotal(base_numerico, irpf)


print("La base de la factura es: " + str(base_numerico))
print("El IRPF es: " + str(irpf))
print("Total a percibir: " + str(total_factura))
