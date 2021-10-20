import random

class Generador:
    
    def generate(self):
        dna=[]
        for i in range(6):
            fila=''
            for j in range(6):
                letra=random.choice(["T","A","C","G"])
                fila+=letra
            
            dna.append(fila)
        return dna


