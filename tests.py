from math import *
from random import *
global fechas, tabla, listaEquipos, campeonRegular, campeonLiguilla, campeonTotal, serie1, serie2, serie3
listaEquipos = []
tabla = []
class equipo:
    nombre = ""
    puntos = 0
    golFavor = 0
    golContra = 0
    golDiferencia = golFavor-golContra
    derrotas = 0
    def __init__(self,nombre):
        self.nombre = nombre
        listaEquipos.append(self)


def jornada(partidos):
    for x in range(0,len(partidos)):
        equipo1 = partidos[x][0]
        equipo2 = partidos[x][1]
        temporal = randint(0,22)
        goles1 = 0
        goles2 =0
        posibilidad = 0
        if temporal < 15:
            posibilidad = 3
        elif temporal >= 15 and temporal <= 20:
            posibilidad = 5
        elif temporal > 20:
            posibilidad = 7

        if equipo1.derrotas - equipo2.derrotas > 5:
            goles1 = randint(0,posibilidad-1)
            goles2 = randint(0,posibilidad)
        elif equipo1.derrotas - equipo2.derrotas > 2 and equipo1.derrotas - equipo2.derrotas <= 5:
            goles1 = randint(0, posibilidad - 1)
            goles2 = randint(0, posibilidad)
        elif equipo2.derrotas - equipo1.derrotas > 5:
            goles1 = randint(0, posibilidad)
            goles2 = randint(0, posibilidad -2)
        elif equipo2.derrotas - equipo1.derrotas > 2 and equipo2.derrotas - equipo1.derrotas <= 5:
            goles2 = randint(0, posibilidad - 1)
            goles1 = randint(0, posibilidad)
        else:
            goles2 = randint(0, posibilidad)
            goles1 = randint(0, posibilidad)
        equipo1.golFavor+=goles1
        equipo1.golContra+=goles2
        equipo2.golFavor+=goles2
        equipo2.golContra+=goles1
        equipo1.golDiferencia=equipo1.golFavor-equipo1.golContra
        equipo2.golDiferencia = equipo2.golFavor - equipo2.golContra
        if goles1 > goles2:
            equipo1.puntos+=3
            equipo2.derrotas+=1
        elif goles2 > goles1:
            equipo2.puntos+=3
            equipo1.derrotas += 1
        elif goles1 == goles2:
            equipo1.puntos+=1
            equipo2.puntos+=1
        print(equipo1.nombre + " "+ str(goles1) + " " + equipo2.nombre + " "+ str(goles2))
def semifinales(serie):
    global serie1, serie2
    equipo1 = serie[0][0]
    equipo2 = serie[1][0]
    goles1global = serie[0][1]
    goles2global = serie[1][1]
    numSerie = serie[2]
    partido = serie[3]

    posibilidad = 0



    if partido == 1:
        temporal = randint(0, 22)
        if temporal < 15:
            posibilidad = 3
        elif temporal >= 15 and temporal <= 20:
            posibilidad = 5
        elif temporal > 20:
            posibilidad = 7

        goles1 = randint(0,posibilidad)
        goles2 = randint(0,posibilidad)

        if numSerie == 1:
            serie1 = [[equipo1,goles1],[equipo2,goles2],1,2]
        elif numSerie == 2:
            serie2 = [[equipo1, goles1], [equipo2, goles2], 2, 2]
        print(equipo1.nombre + " "+ str(goles1) + " " + equipo2.nombre + " "+ str(goles2))
    elif partido == 2:
        temporal = randint(0, 22)
        if temporal < 15:
            posibilidad = 3
        elif temporal >= 15 and temporal <= 20:
            posibilidad = 5
        elif temporal > 20:
            posibilidad = 7

        goles1 = randint(0, posibilidad)
        goles2 = randint(0, posibilidad)

        print(equipo2.nombre + " " + str(goles2) + " " + equipo1.nombre + " " + str(goles1))
        print(equipo2.nombre + " " + str(goles2+goles2global) + " " + equipo1.nombre + " " + str(goles1+goles1global) + " GLOBAL")

        if goles1 + goles1global > goles2 + goles2global:
            listaEquipos.remove(equipo2)
            print(equipo1.nombre + " avanza a la final")
        elif goles2 +goles2global > goles1 + goles1global:
            listaEquipos.remove(equipo1)
            print(equipo2.nombre + " avanza a la final")
        elif goles2 +goles2global ==  goles1 + goles1global:
            if goles2global > goles1:
                listaEquipos.remove(equipo1)
                print(equipo2.nombre + " avanza a la final por gol visitante")
            elif goles2global < goles1:
                listaEquipos.remove(equipo2)
                print(equipo1.nombre + " avanza a la final por gol visitante")
            elif goles2global == goles1:
                ganador = randint(1,2)
                if ganador == 1:
                    listaEquipos.remove(equipo2)
                    print(equipo1.nombre + " avanza a la final por penales")
                elif ganador == 2:
                    listaEquipos.remove(equipo1)
                    print(equipo2.nombre + " avanza a la final por penales")
    return
def updateTabla(listaEquipos):
    global tabla
    tabla = listaEquipos[:]
    tabla.sort(key=lambda x: (x.puntos,x.golDiferencia,x.golFavor), reverse=True)
    for x in range(0,len(tabla)):
        print(str(x+1)+". " + tabla[x].nombre + " ____________ " + str(tabla[x].puntos) + " pts"+ "   " + str(tabla[x].golDiferencia)+ " GD")


lda = equipo("Liga Deportiva Alajuelense")
saprissa = equipo("Deportivo Saprissa")
csh = equipo("Club Sport Herediano")
csc = equipo("Club Sport Cartaginés")
pz = equipo("Municipal Pérez Zeledón")
sc = equipo("Asociación Deportiva San Carlos")
ucr  = equipo("Universidad de Costa Rica")
guadalupe = equipo("Guadalupe FC")
santos = equipo("Santos de Guápiles FC")
limon = equipo("Limón FC")
jicaral = equipo("Jicaral Sercoba")
grecia = equipo("Municipal Grecia")
fechas =[
    [[csc,santos],[grecia,jicaral],[guadalupe,lda],[pz,limon],[sc,saprissa],[ucr,csh]],
    [[jicaral,csc],[csh,grecia],[limon,lda],[santos,guadalupe],[saprissa,pz],[ucr,sc]],
    [[lda,csh],[jicaral,ucr],[csc,sc],[grecia,limon],[guadalupe,pz],[santos,saprissa]],
    [[csh,jicaral],[limon,santos],[pz,lda],[sc,grecia],[saprissa,guadalupe],[ucr,csc]],
    [[lda,saprissa],[jicaral,sc],[csc,csh],[grecia,ucr],[guadalupe,limon],[santos,pz]],
    [[grecia,lda],[csh,limon],[pz,csc],[sc,santos],[saprissa,jicaral],[ucr,guadalupe]],
    [[lda,ucr],[jicaral,pz],[csh,guadalupe],[limon,sc],[santos,grecia],[saprissa,csc]],
    [[lda,santos],[csc,grecia],[guadalupe,jicaral],[limon,saprissa],[pz,ucr],[sc,csh]],
    [[jicaral,santos],[csc,lda],[grecia,guadalupe],[csh,saprissa],[sc,pz],[ucr,limon]],
    [[lda,sc],[guadalupe,csc],[limon,jicaral],[pz,grecia],[santos,csh],[saprissa,ucr]],
    [[jicaral,lda],[csc,limon],[grecia,saprissa],[csh,pz],[sc,guadalupe],[ucr,santos]],
    [[lda,guadalupe],[jicaral,grecia],[csh,ucr],[limon,pz],[santos,csc],[saprissa,sc]],
    [[lda,limon],[csc,jicaral],[grecia,csh],[guadalupe,santos],[pz,saprissa],[sc,ucr]],
    [[csh,lda],[limon,grecia],[pz,guadalupe],[sc,csc],[saprissa,santos],[ucr,jicaral]],
    [[lda,pz],[jicaral,csh],[csc,ucr],[grecia,sc],[guadalupe,saprissa],[santos,limon]],
    [[csh,csc],[limon,guadalupe],[pz,santos],[sc,jicaral],[saprissa,lda],[ucr,grecia]],
    [[lda,grecia],[jicaral,saprissa],[csc,pz],[guadalupe,ucr],[limon,csh],[santos,sc]],
    [[csc,saprissa],[grecia,santos],[guadalupe,csh],[pz,jicaral],[sc,limon],[ucr,lda]],
    [[jicaral,guadalupe],[grecia,csc],[csh,sc],[santos,lda],[saprissa,limon],[ucr,pz]],
    [[lda,csc],[guadalupe,grecia],[limon,ucr],[pz,sc],[santos,jicaral],[saprissa,csh]],
    [[jicaral,limon],[csc,guadalupe],[grecia,pz],[csh,santos],[sc,lda],[ucr,saprissa]],
    [[lda,jicaral],[guadalupe,sc],[limon,csc],[pz,csh],[santos,ucr],[saprissa,grecia]]
    ]
for x in range(0,22):
    print("Fecha " +str(x+1)+" ______________________")
    jornada(fechas[x])
print("__________________________________________________________________")
updateTabla(listaEquipos)
campeonRegular=tabla[0]
print(campeonRegular.nombre + " CAMPEON")
tabla = tabla[0:4]
serie1=[[tabla[0],0],[tabla[3],0],1,1]
serie2=[[tabla[1],0],[tabla[2],0],2,1]
for x in range(0,2):
    print("__________________________________________________________________")
    semifinales(serie1)
    print("__________________________________________________________________")
    semifinales(serie2)