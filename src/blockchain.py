from datetime import datetime
from hashlib import sha256
import json

class Block:
    def __init__(self, cor, mot, arc, hant, hblock, hverif):
        self.correo = cor
        self.motivo = mot
        self.archivo = arc
        #self.timestamp = datetime.now()
        self.hashAnt = hant
        self.hashBlock = hblock
        self.hashVerif = hverif

    def crearHash(self):
        hash = json.dumps(self.__dict__, sort_keys=True)
        return sha256(hash.encode()).hexdigest()

    def mostrar(self):
        print("A nombre de: ", self.correo)
        print("Motivo: ", self.motivo)
        #print("Fecha: ", self.tiempo)

class Blockchain:
    def __init__(self):
        self.cadena = []
        self.crearGenesis()

    def crearGenesis(self):
        bloqueGenesis = Block("", "", "", "0", "0", "0")
        bloqueGenesis.hashBlq = bloqueGenesis.crearHash()
        self.cadena.append(bloqueGenesis) 