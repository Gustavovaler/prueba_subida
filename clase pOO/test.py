
class Persona:
    
    def __init__(self, nombre, genero, edad):
        self.nombre = nombre
        self.genero = genero
        self.edad = edad
        
    def __str__(self):
        return f'Nombre = {self.nombre} - genero = {self.genero} - edad = {self.edad}' 
    
    def hacer_algo(self):
        self.caminar()
        self.detenerse()
        
        
    def caminar(self):
        print("Caminando")
        
    def detenerse(self):
        print("Detenido")


        
        
    
    





    


        
    
        