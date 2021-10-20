from detector_de_mutantes import isMutant
from generador import Generador

if __name__ == "__main__":
    generador=Generador()
    aux=0
    for i in range(100):
        if isMutant(generador.generate()):
            aux+=1

    print("El algoritmo encontró "+str(aux)+" mutantes")    

    
