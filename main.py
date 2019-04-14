from PIL import Image, ImageDraw
image = Image.open('cantones3.png')
class canton:
    conquistado = False
    tamano = 0
    poblacion = 0
    limites = []
    nombre = ""
    centro = (0,0)
    color = (0,0,0,0)

    def __init__(self, conquistado, tamano, poblacion, limites, nombre, centro):
        """Constructor de clase Persona"""
        self.nombre = nombre
        self.conquistado = conquistado
        self.poblacion = poblacion
        self.limites = limites
        self.centro = centro

    def imprimir(self):
        ImageDraw.floodfill(image, self.centro, self.color)
        if self.nombre == 'Heredia, Heredia':
            ImageDraw.floodfill(image, (412,242), self.color)
        if self.nombre == 'Puntarenas, Puntarenas':
            ImageDraw.floodfill(image, (170, 252), self.color)
            ImageDraw.floodfill(image, (179, 310), self.color)
        image.show()



SJ = canton(False, 44.62, 288054,[],"San José, San José", (400,289))
Alajuela = canton(False, 388.43, 254886, [], "Alajuela, Alajuela", (376,268))
Desamparados = canton(False, 118.26, 208411,[], "Desamparados, San José", (414,310))
SC= canton(False, 3347.98, 163745, [], "San Carlos, Alajuela", (328,171))
Cartago = canton(False, 287.77, 147898, [] , "Cartago, Cartago", (444,313))
PZ = canton(False, 1905.51, 134534,[], "Pérez Zeledón, San José", (497,416))
Pococi = canton(False, 2403.49, 125962,[], "Pococi, Limón", (495,170))
Heredia = canton(False, 282.60, 123616,[], "Heredia, Heredia", (394,276))
Puntarenas = canton(False, 1842.33, 115019,[], "Puntarenas, Puntarenas",(234,256))
Goicochea = canton(False, 31.50, 115084, [], "Goicochea, San José", (419,283))
Union = canton(False, 44.83, 99399, [], "La Union, Cartago", (428,293))
Limon = canton(False, 1765.79, 94415, [], "Limon, Limón", (626,327))
SR = canton(False, 1018.64, 805660, [], "San Ramón, Alajuela", (296,228))
Alajuelita = canton(False, 21.17, 77603, [], "Alajuelita, San José", (400,298))
Turrialba = canton(False, 1642.67, 35201, [], "Turrialba, Cartago", (528,298))
Grecia = canton(False,141.52, 65824,[], 'Grecia', (358,256))
Curridabat = canton(False, 15.95, 65206, [], "Curridabat, San José",(419,292))
Tibas = canton(False, 8.15, 64842, [], "Tibás, San José", (405,283))
Liberia = canton(False, 1436.47, 62987, [], "Liberia, Guanacaste", (100,119))
Coronado = canton(False, 222.20, 60486, [], "Vásquez de Coronado, San José", (435,267))
Aserri = canton(False, 167.10, 57892, [], "Aserrí, San José", (396,329))
Paraiso = canton(False, 411.91, 57743, [], "Paraíso, Cartago", (480,341))
Sarapiqui = canton(False, 2140.54, 57147, [], "Sarapiquí, Heredia", (422,177))
Siquirres = canton(False, 860.19, 56786, [], "Siquirres, Limón", (532,238))
Moravia = canton(False, 28.62, 30178, [], "Moravia, San José", (420,274))
Escazu = canton(False, 34.39, 56509, [], "Escazú, San José", (393,294))
SantaCruz = canton(False, 1312.27, 55104,[], "Santa Cruz, Guanacaste", (45,230))
Nicoya = canton(False, 1333.68, 25.838, [], "Nicoya, Guanacaste", (112,232))
MontesDeOca = canton(False, 15.16, 2622,[], 'Montes de Oca, San José', (424,286))
SantaAna = canton(False, 61.42, 49123, [], "Santa Ana, San José", (380,292))
SanRafael = canton(False, 48.9, 45965, [], "San Rafael, Heredia", (407,265))
Oreamuno = canton(False, 202.31, 45473, [], "Oreamuno, Cartago", (456,270))
BuenosAires = canton(False, 2384.22, 45244, [], "Buenos Aires, Puntarenas", (603,457))
Upala = canton(False, 1580.67, 43953, [], "Upala, Alajuela", (161,84))
Naranjo =canton(False, 126.62, 42713, [], "Naranjo, Alajuela", (340,251))



Moravia.color = (255,0,255,255)
Moravia.imprimir()