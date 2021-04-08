from datetime import datetime
from hashlib import sha256
import json

class Bloque:
    def __init__(self, index, cor, mot, hashArc, hashAnt):
        self.index = index
        self.correo = cor
        self.motivo = mot
        self.hashArc = hashArc
        self.hashAnt = hashAnt
        self.hashBloque = self.crearHash()
        #self.timestamp = datetime.now()

    def crearHash(self):
        hash = json.dumps(self.__dict__, sort_keys=True)
        return sha256(hash.encode()).hexdigest()

class Blockchain:
    def __init__(self):
        self.cadena = []
        self.crearGenesis()

    def crearGenesis(self):
        bloqueGenesis = Bloque(0, "", "", "0", "0")
        self.cadena.append(bloqueGenesis)
    
    def crearBloque(self):
        pass

    def getHashByIndex(self, index):
        return self.cadena[index].hashBloque
