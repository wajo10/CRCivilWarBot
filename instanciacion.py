from PIL import Image, ImageDraw
from random import randint, choice
global cantones, listaCantones, listaRestantes, image
image = Image.open('provincias.png')
cantones = 7
listaCantones=[]
listaRestantes=[]
class canton:
    conquistado = False
    tamano = 0
    poblacion = 0
    tamanoConquistado=0
    poblacionConquistado=0
    limites = []
    limitesConquistas = limites
    contiene = []
    nombre = ""
    centro = (0,0)
    parteDe = None
    color = (randint(0,255),randint(0,255),randint(0,255),255)



    def imprimir(self):
        ImageDraw.floodfill(image, self.centro, self.color)
        if self.nombre == 'Puntarenas, Puntarenas':
            ImageDraw.floodfill(image, (121, 141), self.color)


    def __init__(self, conquistado, tamano, poblacion, limites, nombre, centro):
        """Constructor de clase Canton"""
        self.nombre = nombre
        self.conquistado = conquistado
        self.poblacion = poblacion
        self.poblacionConquistado=poblacion
        self.tamano=tamano
        self.tamanoConquistado=tamano
        self.centro = centro
        self.color = (randint(0,255),randint(0,255),randint(0,255),255)
        self.imprimir()
        self.limites = []
        self.limitesConquistas=limites
        self.contiene = []
        self.parteDe = None
        listaCantones.append(self)
        listaRestantes.append(self)
        self.imprimir()
def atacar():
    global cantones, perdedor
    while(cantones > 1):
        canton1 = choice(listaRestantes)
        if canton1.limitesConquistas == []:
            canton1.limitesConquistas.extend(canton1.limites)
        canton2 = choice(canton1.limitesConquistas)
        x=canton1.poblacionConquistado+canton1.tamanoConquistado+canton2.poblacionConquistado+canton2.tamanoConquistado
        posCanton1 = 100*(canton1.tamanoConquistado+canton1.poblacionConquistado)/x
        posCanton2 = 100 * (canton2.tamanoConquistado + canton2.poblacionConquistado)/x

        resultante = randint(1,100)
        if (posCanton1 > posCanton2):
            if resultante >= posCanton2:
                definicion(canton1, canton2)
            else:
                definicion(canton2, canton1)
        else:
            if resultante > posCanton1:
                definicion(canton1, canton2)
            else:
                definicion(canton1, canton2)
    else:
        print("Gano el canton: " + str(listaRestantes[0].nombre))

def definicion(ganador,perdedor):
    global cantones,image, listaRestantes
    #Si el ganador esta conquistado, el ganador va a ser el dueno del ganador, siempre y cuando no sean del mismo territorio
    if ganador.conquistado:
        if ganador.parteDe != perdedor.parteDe and ganador != perdedor.parteDe:
            ganador = ganador.parteDe
        else:
            return
    if ganador == perdedor.parteDe or ganador.parteDe == perdedor or ganador.parteDe == perdedor.parteDe and ganador.parteDe is not None:
        print("SALIR")
        return
    try:
        if ganador.nombre == perdedor.parteDe.nombre:
            print("DEBERIA SALIR")
            return
    except:
        pass
    #Se agregan los limites del perdedor y se intenta eliminar el mismo
    ganador.limitesConquistas.extend(perdedor.limites)
    try:
        ganador.limitesConquistas.remove(ganador)
    except:
        pass
    #Se setea el nuevo tamano y la nueva poblacion
    ganador.tamanoConquistado += perdedor.tamano
    ganador.poblacionConquistado += perdedor.poblacion

    #Si otro canton era dueno del perdedor se le quita y pasa al ganador
    for x in listaRestantes:
        if perdedor in x.contiene:
            x.contiene.remove(perdedor)
            break
    ganador.contiene.append(perdedor)

    #Si el perdedor no estaba conquistado y no habia conquistado otros territorios
    if (not perdedor.conquistado) and len(perdedor.contiene)==0:
        perdedor.conquistado = True
        perdedor.parteDe = ganador
        listaRestantes.remove(perdedor)
        print(str(ganador.nombre) + " Ha conquistado " + str(perdedor.nombre)+"\n"+
              perdedor.nombre + " ha sido eliminado. " +"Quedan: " +str(cantones))
        cantones-=1
    else:
        #Si el perdedor es parte de otro canton se setean los nuevos atributos
        if (perdedor.parteDe != None):
            perdedor.parteDe.tamanoConquistado-=perdedor.tamano
            perdedor.parteDe.poblacionConquistado-= perdedor.poblacion
            for x in perdedor.limitesConquistas:
                if x in perdedor.parteDe.limitesConquistas:
                    perdedor.parteDe.limitesConquistas.remove(x)
            if (ganador.nombre == perdedor.parteDe.nombre):
                print("ERRORRRRRRR")
            print(str(ganador.nombre) + " ha conquistado el territorio de " + str(perdedor.nombre) +
                  " antes ocupado por " +perdedor.parteDe.nombre + "\n" +"restan: " +str(cantones))
            perdedor.parteDe = ganador
        else:
            print(str(ganador.nombre) + " ha conquistado el territorio de " + str(perdedor.nombre))
#_______________________________________________________________
    ImageDraw.floodfill(image, perdedor.centro, ganador.color)
    if perdedor.nombre == 'Puntarenas, Puntarenas':
        ImageDraw.floodfill(image, (121, 141), ganador.color)
#______________________________________________________________


# ___________INSTANCIACION DE CADA CANTON_________________________________________
SJ = canton(False, 44.62, 288054, [], "San José, San José", (193, 143))
Alajuela = canton(False, 388.43, 254886, [], "Alajuela, Alajuela", (176, 107))
Puntarenas = canton(False, 118.26, 208411, [], "Puntarenas, Puntarenas", (284, 201))
Guanacaste = canton(False, 3347.98, 163745, [], "Guanacaste", (98, 82))
Cartago = canton(False, 287.77, 147898, [], "Cartago, Cartago", (238, 135))
Limon = canton(False, 1905.51, 134534, [], "Limon", (278, 153))
Heredia = canton(False, 2403.49, 125962, [], "Heredia, Heredia", (206, 85))


# ________________LIMITES DE CADA CANTON_______________________________________________________________________
SJ.limites = [Heredia,Alajuela,Limon,Puntarenas,Cartago]
Alajuela.limites = [Guanacaste,Puntarenas,SJ,Heredia]
Puntarenas.limites = [Limon,Guanacaste,Alajuela,SJ]
Guanacaste.limites = [Alajuela,Puntarenas]
Cartago.limites = [Heredia,Limon,SJ,Heredia]
Limon.limites = [Cartago,SJ,Puntarenas]
Heredia.limites = [Limon,SJ,Alajuela,Cartago]


atacar()

image.show()