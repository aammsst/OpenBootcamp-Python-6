class Vehiculo:

    color = ""
    ruedas = 4
    puertas = 2

class Coche(Vehiculo):

    velocidad = 0
    cilindrada = 0

c = Coche()
c.color = "Azul"
c.velocidad = 260 #Km/h
c.cilindrada = 3500 #cc

print("Color del coche:", c.color)
print("Cantidad de ruedas:", c.ruedas)
print("Cantidad de puertas:", c.puertas)
print("Velocidad del coche:", c.velocidad, "Km/h")
print("Cilindrada del coche:", c.cilindrada, "cc")
