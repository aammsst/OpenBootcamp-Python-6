class Alumno:

    _nombre = ""
    _nota = 0
    
    def insertarNombre(self, nombre):
        self._nombre = nombre

    def insertarNota(self, nota):
        self._nota = nota

    def isAproved(self):
        estado =  "Aprobado!" if (self._nota >= 6) else "Desaprobado"
        print("El alumno", self._nombre,"esta:", estado, "- nota:", self._nota, "\n")

matias = Alumno()
tomas = Alumno()
ramon = Alumno()

matias.insertarNombre("Matías")
matias.insertarNota(10)
matias.isAproved()

tomas.insertarNombre("Tomás")
tomas.insertarNota(3)
tomas.isAproved()

ramon.insertarNombre("Ramón")
ramon.insertarNota(6)
ramon.isAproved()
