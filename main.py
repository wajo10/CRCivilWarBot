from PIL import Image, ImageDraw
from random import randint, choice
import facebook
global cantones, listaCantones, listaRestantes, image, perdedor
graph = facebook.GraphAPI(access_token="EAAIbeSGZBSXABACQNM4lTHQQGZAdip7uZAL6e1Xrfp1tXms6IniL5KyMydDhHcISiCQrgMFzfer7ZCuU5G8PQvUD2JRnMKgYzT6ppGqTdLBdOpZBTI4QZCbnp1uvwjLpjgxlYgv9pcOtgYCHiGZAHAbl4ASHVARKFOcE6Sod4y4Xlg3OVMCspND5gNn57c9aiZBdZA77E5yWPMAZDZD", version="2.12")
perdedor = None
image = Image.open('cantones.png')
cantones = 83
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
    perdio=[]
    color = (randint(0,255),randint(0,255),randint(0,255),255)



    def imprimir(self):
        ImageDraw.floodfill(image, self.centro, self.color)
        if self.nombre == 'Heredia, Heredia':
            ImageDraw.floodfill(image, (412,242), self.color)
        if self.nombre == 'Puntarenas, Puntarenas':
            ImageDraw.floodfill(image, (170, 252), self.color)
            ImageDraw.floodfill(image, (179, 310), self.color)
        if self.nombre =="Golfito, Puntarenas":
            ImageDraw.floodfill(image, (556, 609), self.color)


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
        self.timesConquered=0
        self.parteDe = None
        listaCantones.append(self)
        listaRestantes.append(self)
def atacar():
    global cantones, perdedor
    flag = True
    while(cantones > 1):
        if cantones > 8:
            canton1 = choice(listaRestantes)
            if canton1.limitesConquistas == []:
                canton1.limitesConquistas.extend(canton1.limites)
            canton2 = choice(canton1.limitesConquistas)
        else:
            if flag:
                canton1 = choice(listaRestantes)
                canton2 = choice(listaCantones)
                flag = False
            else:
                canton2 = choice(listaCantones)

        x = canton1.poblacionConquistado + canton1.tamanoConquistado + canton2.poblacionConquistado + canton2.tamanoConquistado

        if flag:
            posCanton1 = 100*(canton1.tamanoConquistado+canton1.poblacionConquistado)/x
            posCanton2 = 100 * (canton2.tamanoConquistado + canton2.poblacionConquistado)/x
        else:
            posCanton1=99
            posCanton2=1
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
    global cantones, image, listaRestantes
    # Si el ganador esta conquistado, el ganador va a ser el dueno del ganador, siempre y cuando no sean del mismo territorio
    if ganador.conquistado:
        if ganador.parteDe != perdedor.parteDe and ganador != perdedor.parteDe:
            ganador = ganador.parteDe
        else:
            return
    if ganador == perdedor.parteDe or ganador.parteDe == perdedor or ganador.parteDe == perdedor.parteDe and ganador.parteDe is not None:
        #print("SALIR")
        return
    # Se agregan los limites del perdedor y se intenta eliminar el mismo
    ganador.limitesConquistas.extend(perdedor.limites)
    try:
        ganador.limitesConquistas.remove(ganador)
    except:
        pass
    # Se setea el nuevo tamano y la nueva poblacion
    ganador.tamanoConquistado += perdedor.tamano
    ganador.poblacionConquistado += perdedor.poblacion

    # Si otro canton era dueno del perdedor se le quita y pasa al ganador
    for x in listaRestantes:
        if perdedor in x.contiene:
            x.contiene.remove(perdedor)
            x.poblacionConquistado -= perdedor.poblacion
            x.tamanoConquistado -= perdedor.tamano
            for y in perdedor.limitesConquistas:
                if y in x.limitesConquistas:
                    x.limitesConquistas.remove(y)

            break
    ganador.contiene.append(perdedor)
    perdedor.timesConquered += 1
    pintar(ganador, perdedor)

    # Si el perdedor no estaba conquistado y no habia conquistado otros territorios
    if (not perdedor.conquistado) and len(perdedor.contiene) == 0:
        perdedor.conquistado = True
        perdedor.parteDe = ganador
        listaRestantes.remove(perdedor)
        print(str(ganador.nombre) + " Ha conquistado " + str(perdedor.nombre) + "\n" +
              perdedor.nombre + " ha sido eliminado. " + "Quedan: " + str(cantones))
        cantones -= 1
    else:
        if (perdedor.parteDe != None):
            otro = perdedor.parteDe
            otro.tamanoConquistado -= perdedor.tamano
            otro.poblacionConquistado -= perdedor.poblacion
            for x in perdedor.limitesConquistas:
                if x in otro.limitesConquistas:
                    otro.limitesConquistas.remove(x)
        # Si el perdedor es parte de otro canton se setean los nuevos atributos
            if (ganador.nombre == perdedor.parteDe.nombre):
                print("ERRORRRRRRR")
            print(str(ganador.nombre) + " ha conquistado el territorio de " + str(perdedor.nombre) +
                  " antes ocupado por " + perdedor.parteDe.nombre + "\n" + "restan: " + str(cantones))
            perdedor.parteDe = ganador
        else:
            print(str(ganador.nombre) + " ha conquistado el territorio de " + str(perdedor.nombre))



def pintar (ganador,perdedor):
    ImageDraw.floodfill(image, perdedor.centro, ganador.color)
    if perdedor.nombre == 'Heredia, Heredia':
        ImageDraw.floodfill(image, (412, 242), ganador.color)
    elif perdedor.nombre == 'Puntarenas, Puntarenas':
        ImageDraw.floodfill(image, (170, 252), ganador.color)
        ImageDraw.floodfill(image, (179, 310), ganador.color)
    elif perdedor.nombre == "Golfito, Puntarenas":
        ImageDraw.floodfill(image, (556, 609), ganador.color)

# ___________INSTANCIACION DE CADA CANTON_________________________________________
SJ = canton(False, 44.62, 288054, [], "San José, San José", (400, 289))
Alajuela = canton(False, 388.43, 254886, [], "Alajuela, Alajuela", (376, 268))
Desamparados = canton(False, 118.26, 208411, [], "Desamparados, San José", (414, 310))
SC = canton(False, 3347.98, 163745, [], "San Carlos, Alajuela", (328, 171))
Cartago = canton(False, 287.77, 147898, [], "Cartago, Cartago", (444, 313))
PZ = canton(False, 1905.51, 134534, [], "Pérez Zeledón, San José", (497, 416))
Pococi = canton(False, 2403.49, 125962, [], "Pococi, Limón", (495, 170))
Heredia = canton(False, 282.60, 123616, [], "Heredia, Heredia", (394, 276))
Puntarenas = canton(False, 1842.33, 115019, [], "Puntarenas, Puntarenas", (234, 256))
Goicochea = canton(False, 31.50, 115084, [], "Goicochea, San José", (419, 283))
Union = canton(False, 44.83, 99399, [], "La Union, Cartago", (428, 293))
Limon = canton(False, 1765.79, 94415, [], "Limón, Limón", (626, 327))
SR = canton(False, 1018.64, 805660, [], "San Ramón, Alajuela", (296, 228))
Alajuelita = canton(False, 21.17, 77603, [], "Alajuelita, San José", (400, 298))
Turrialba = canton(False, 1642.67, 35201, [], "Turrialba, Cartago", (528, 298))
Grecia = canton(False, 141.52, 65824, [], 'Grecia', (358, 256))
Curridabat = canton(False, 15.95, 65206, [], "Curridabat, San José", (419, 292))
Tibas = canton(False, 8.15, 64842, [], "Tibás, San José", (405, 283))
Liberia = canton(False, 1436.47, 62987, [], "Liberia, Guanacaste", (100, 119))
Coronado = canton(False, 222.20, 60486, [], "Vásquez de Coronado, San José", (435, 267))
Aserri = canton(False, 167.10, 57892, [], "Aserrí, San José", (396, 329))
Paraiso = canton(False, 411.91, 57743, [], "Paraíso, Cartago", (480, 341))
Sarapiqui = canton(False, 2140.54, 57147, [], "Sarapiquí, Heredia", (422, 177))
Siquirres = canton(False, 860.19, 56786, [], "Siquirres, Limón", (532, 238))
Moravia = canton(False, 28.62, 30178, [], "Moravia, San José", (420, 274))
Escazu = canton(False, 34.39, 56509, [], "Escazú, San José", (393, 294))
SantaCruz = canton(False, 1312.27, 55104, [], "Santa Cruz, Guanacaste", (45, 230))
Nicoya = canton(False, 1333.68, 25.838, [], "Nicoya, Guanacaste", (112, 232))
MontesDeOca = canton(False, 15.16, 2622, [], 'Montes de Oca, San José', (424, 286))
SantaAna = canton(False, 61.42, 49123, [], "Santa Ana, San José", (380, 292))
SanRafael = canton(False, 48.9, 45965, [], "San Rafael, Heredia", (407, 265))
Oreamuno = canton(False, 202.31, 45473, [], "Oreamuno, Cartago", (456, 270))
BuenosAires = canton(False, 2384.22, 45244, [], "Buenos Aires, Puntarenas", (603, 457))
Upala = canton(False, 1580.67, 43953, [], "Upala, Alajuela", (161, 84))
Naranjo = canton(False, 126.62, 42713, [], "Naranjo, Alajuela", (340, 251))
Corredores = canton(False, 620.60, 41831, [], "Corredores, Puntarenas", (663, 590))
Guarco = canton(False, 167.79, 41793, [], "El Guarco, Cartago", (437, 330))
Guacimo = canton(False, 576.48, 41266, [], "Guácimo, Limón", (498, 225))
Barva = canton(False, 53.80, 40660, [], "Barva, Heredia", (399, 255))
SantoDomingo = canton(False, 24.84, 40072, [], "Santo Domingo, Heredia", (409, 278))
Golfito = canton(False, 1753.96, 39150, [], "Golfito, Puntarenas", (630, 548))
CotoBrus = canton(False, 933.91, 38453, [], "Coto Brus, Puntarenas", (657, 511))
Matina = canton(False, 772.64, 37721, [], "Matina, Limón", (585, 256))
Carrillo = canton(False, 577.54, 37122, [], "Carrillo, Guanacaste", (64, 172))
SantaBarbara = canton(False, 53.21, 36243, [], "Santa Bárbara, Heredia", (391, 257))
Palmares = canton(False, 38.06, 34716, [], "Palmares, Alajuela", (328, 266))
Puriscal = canton(False, 553.00, 33004, [], "Puriscal, San José", (338, 332))
Talamanca = canton(False, 2809.93, 30712, [], "Talamanca, Limón", (608, 394))
Osa = canton(False, 1930.24, 29433, [], "Osa, Puntarenas", (534, 511))
Poas = canton(False, 73.84, 29199, [], "Poás, Alajuela", (369, 255))
Esparza = canton(False, 216.80, 28644, [], "Esparza, Puntarenas", (277, 284))
SanPablo = canton(False, 7.53, 27671, [], "San Pablo, Heredia", (403, 275))
Quepos = canton(False, 543.77, 26861, [], "Quepos, Puntarenas", (402, 400))
Mora = canton(False, 162.04, 26294, [], "Mora, San José", (364, 303))
Canas = canton(False, 682.20, 26201, [], "Cañas, Guanacaste", (186, 193))
Atenas = canton(False, 127.19, 25460, [], "Atenas, Alajuela", (335, 280))
LosChiles = canton(False, 1358.86, 23735, [], " Los Chiles, Alajuela", (274, 85))
Belen = canton(False, 12.15, 21633, [], "Belén, Heredia", (384, 278))
SanIsidro = canton(False, 26.96, 20633, [], "San Isidro, Heredia", (415, 267))
Orotina = canton(False, 141.92, 20341, [], "Orotina, Alajuela", (296, 299))
Acosta = canton(False, 342.24, 20209, [], "Acosta, San José", (370, 333))
Flores = canton(False, 6.96, 20037, [], "Flores, Heredia", (389, 273))
Tilaran = canton(False, 638.39, 19640, [], "Tilarán, Guanacaste", (226, 180))
Bagaces = canton(False, 1273.49, 19536, [], "Bagaces, Guanacaste", (166, 169))
LaCruz = canton(False, 1383.90, 19181, [], "La Cruz, Guanacaste", (78, 52))
Sarchi = canton(False, 120.25, 18085, [], "Sarchí, Alajuela", (359, 226))
Abangares = canton(False, 675.76, 18039, [], "Abangares, Guanacaste", (216, 222))
Garabito = canton(False, 316.31, 17229, [], "Garabito, Puntarenas", (292, 324))
Tarrazu = canton(False, 297.50, 16280, [], "Tarrazú, San José", (418, 366))
Parrita = canton(False, 478.79, 16115, [], "Parrita, Puntarenas", (354, 370))
Guatuso = canton(False, 758.32, 15508, [], "Guatuso, Alajuela", (245, 121))
Jimenez = canton(False, 286.43, 14669, [], "Jiménez, Cartago", (487, 313))
Alvarado = canton(False, 81.06, 14312, [], "Alvarado, Cartago", (467, 287))
MontesOro = canton(False, 244.76, 12950, [], "Montes de Oro, Puntarenas", (264, 251))
Zarcero = canton(False, 155.13, 12205, [], "Zarcero, Alajuela", (328, 227))
LeonCortes = canton(False, 120.80, 12200, [], "León Cortés, San José", (412, 341))
Nandayure = canton(False, 565.59, 11121, [], "Nandayure, Guanacaste", (134, 300))
RioCuarto = canton(False, 254.20, 11074, [], "Río Cuarto, Alajuela", (374, 192))
Hojancha = canton(False, 261.42, 7197, [], "Hojancha, Guanacaste", (112, 284))
Dota = canton(False, 400.22, 6948, [], "Dota, San José", (446, 365))
SanMateo = canton(False, 125.90, 6136, [], "San Mateo, Alajuela", (304, 283))
Turrubares = canton(False, 415.29, 5512, [], "Turrubares, San José", (314, 315))
IslaCoco = canton(False, 23.85, 20000, [], "Isla del Coco, Puntarenas", (103, 598))

# ________________LIMITES DE CADA CANTON_______________________________________________________________________
SJ.limites = [Belen, Heredia, SantoDomingo, Tibas, Goicochea, MontesDeOca, Curridabat, Desamparados, Alajuelita,
              Escazu]
Alajuela.limites = [Sarapiqui, Heredia, Belen, SantaBarbara, SantaAna, Mora, Atenas, Grecia, Poas, Sarchi,
                    RioCuarto]
Desamparados.limites = [Curridabat, SJ, Alajuelita, Aserri, LeonCortes, Dota, Guarco, Cartago, Union]
SC.limites = [LosChiles, Guatuso, Tilaran, SR, Zarcero, Sarchi, RioCuarto, Sarapiqui]
Cartago.limites = [Goicochea, Coronado, Desamparados, Guarco, MontesDeOca, Union, Oreamuno, Paraiso]
PZ.limites = [Paraiso, Dota, Quepos, Osa, BuenosAires, Talamanca, Turrialba]
Pococi.limites = [Sarapiqui, Guacimo, Oreamuno, Turrialba]
Heredia.limites = [Barva, SantaBarbara, SanRafael, SanIsidro, Sarapiqui, Flores, Belen, SantoDomingo, SJ, Union]
Puntarenas.limites = [Nandayure, Abangares, Esparza, SR, SanMateo, Tilaran, IslaCoco]
Goicochea.limites = [Coronado, Moravia, Tibas, SJ, MontesDeOca, Cartago]
Union.limites = [MontesDeOca, Curridabat, Cartago, Desamparados]
Limon.limites = [Talamanca, Matina, Turrialba]
SR.limites = [SC, Zarcero, SanMateo, Atenas, Palmares, Naranjo, Tilaran, MontesOro, Puntarenas, Esparza]
Alajuelita.limites = [SJ, Escazu, Acosta, Aserri, Desamparados]
Turrialba.limites = [Pococi, Guacimo, Siquirres, Matina, Limon, Talamanca, Jimenez, Alvarado, Oreamuno, Paraiso, PZ]
Grecia.limites = [Poas, Alajuela, Sarchi, Alajuela, Atenas, Naranjo]
Curridabat.limites = [MontesDeOca, SJ, Union, Desamparados]
Tibas.limites = [SantoDomingo, SJ, Goicochea, Moravia]
Liberia.limites = [Bagaces, LaCruz, Carrillo, Upala]
Coronado.limites = [Heredia, SanIsidro, Moravia, Goicochea, Cartago, Oreamuno, Sarapiqui]
Aserri.limites = [Alajuelita, Acosta, Parrita, Tarrazu, LeonCortes, Desamparados]
Paraiso.limites = [Alvarado, Oreamuno, Dota, PZ, Jimenez, Turrialba, Cartago]
Sarapiqui.limites = [SC, RioCuarto, Alajuela, Heredia, Limon]
Siquirres.limites = [Pococi, Matina, Guacimo, Turrialba]
Moravia.limites = [SanIsidro, SantoDomingo, Tibas, Goicochea, Coronado]
Escazu.limites = [Belen, SantaAna, Mora, Acosta, Alajuelita]
SantaCruz.limites = [Carrillo, Bagaces, Nicoya]
Nicoya.limites = [SantaCruz, Abangares, Hojancha, Nandayure]
MontesDeOca.limites = [Goicochea, SJ, Curridabat, Union, Cartago]
SantaAna.limites = [Alajuela, Belen, Mora, Escazu]
SanRafael.limites = [Heredia, Barva, SanPablo, SanIsidro]
Oreamuno.limites = [Pococi, Cartago, Paraiso, Coronado, Alvarado, Turrialba]
BuenosAires.limites = [Talamanca, PZ, Osa, CotoBrus, Golfito, IslaCoco]
Upala.limites = [LosChiles, Guatuso, Canas, Bagaces, Liberia, LaCruz]
Naranjo.limites = [Zarcero, Atenas, Sarchi, Grecia, SR, Palmares, RioCuarto]
Corredores.limites = [Golfito, CotoBrus]
Guarco.limites = [Cartago, Desamparados, Dota]
Guacimo.limites = [Pococi, Turrialba, Siquirres]
Barva.limites = [SantaBarbara, Heredia, Flores, SanRafael]
SantoDomingo.limites = [SanPablo, SanIsidro, Heredia, Moravia, SJ, Tibas]
Golfito.limites = [Osa, BuenosAires, CotoBrus, Corredores]
CotoBrus.limites = [BuenosAires, Talamanca, Golfito, Corredores]
Matina.limites = [Siquirres, Limon, Turrialba]
Carrillo.limites = [Liberia, SantaCruz, Bagaces]
SantaBarbara.limites = [Flores, Barva, Alajuela, Heredia]
Palmares.limites = [SR, Atenas, Naranjo]
Puriscal.limites = [Turrubares, Acosta, Mora, Parrita]
Talamanca.limites = [CotoBrus, Limon, PZ, Turrialba, BuenosAires]
Osa.limites = [PZ, BuenosAires, Golfito, Golfito, IslaCoco]
Poas.limites = [Sarchi, Alajuela, Grecia]
Esparza.limites = [SR, Puntarenas, MontesOro, Garabito, SanMateo, Orotina, IslaCoco]
SanPablo.limites = [SantoDomingo, SanRafael, SanIsidro, Heredia]
Quepos.limites = [Tarrazu, Dota, PZ, Parrita, Osa, IslaCoco]
Mora.limites = [Alajuela, Atenas, Puriscal, Turrubares, SantaAna, Acosta]
Canas.limites = [Guatuso, Bagaces, Tilaran, Nicoya]
Atenas.limites = [Naranjo, Grecia, Palmares, SR, Mora, Turrubares, Alajuela, SanMateo, Orotina]
LosChiles.limites = [Upala, SC, Guatuso]
Belen.limites = [Alajuela, Flores, Heredia, SJ, Escazu, SantaAna]
SanIsidro.limites = [Coronado, Moravia, SantoDomingo, SanRafael, SanPablo]
Orotina.limites = [Atenas, SanMateo, Garabito, Turrubares, Esparza]
Acosta.limites = [Alajuelita, Escazu, Mora, Puriscal, Parrita, Aserri]
Flores.limites = [SantaBarbara, Barva, Heredia, Belen]
Tilaran.limites = [Guatuso, Canas, SC, Abangares, SR, Tilaran]
Bagaces.limites = [Upala, Liberia, Carrillo, Canas, Nicoya, SantaCruz]
LaCruz.limites = [Upala, Liberia]
Sarchi.limites = [SC, Grecia, Poas, Alajuela, Zarcero, Naranjo, RioCuarto]
Abangares.limites = [Canas, Tilaran, Puntarenas]
Garabito.limites = [Esparza, Orotina, Parrita, Turrubares]
Tarrazu.limites = [Parrita, Quepos, Dota]
Parrita.limites = [Quepos, Puriscal, Acosta, Aserri, Tarrazu, Turrubares, Garabito]
Guatuso.limites = [LosChiles, Canas, Tilaran, Upala, SC]
Jimenez.limites = [Alvarado, Turrialba, Paraiso]
Alvarado.limites = [Jimenez, Oreamuno, Paraiso, Turrialba]
MontesOro.limites = [SR, Esparza, Puntarenas]
Zarcero.limites = [SC, Sarchi, SR, Naranjo]
LeonCortes.limites = [Tarrazu, Dota, Desamparados, Aserri]
Nandayure.limites = [Nicoya, Hojancha, Puntarenas]
RioCuarto.limites = [SC, Sarapiqui, Alajuela, Sarchi]
Hojancha.limites = [Nicoya, Nandayure]
Dota.limites = [Desamparados, Paraiso, Guarco, Quepos, PZ, Tarrazu, LeonCortes]
SanMateo.limites = [SR, Atenas, Esparza, Orotina, Puntarenas]
Turrubares.limites = [Atenas, Orotina, Garabito, Parrita, Puriscal, Mora]
IslaCoco.limites = [Puntarenas, Esparza, Osa, BuenosAires, Quepos]

#atacar()

image.show()
image.save("restantes.png")
graph.put_photo(image=open("restantes.png", 'rb'),
                message='Primera Prueba')