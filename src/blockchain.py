import os
import sys
import json
from bson import json_util
root_folder = os.path.abspath(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(root_folder)

from src.bloque import Bloque
from datetime import datetime

class Singleton(type):
    __instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls.__instances:
            cls.__instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls.__instances[cls]

class Blockchain(metaclass=Singleton):
    def __init__(self):
        self.__cadena = []
        self.__zero_count = 0
        self.__crearGenesis()
        

    def __crearGenesis(self):
        bloqueGenesis = Bloque(0, "", "", "0", "0", "2021-01-01 00:00:00", self.__zero_count)
        self.__cadena.append(bloqueGenesis)
    
    def __crearBloque(self, cor, mot, hashArc, timestamp):
        newBloque = Bloque(self.__getNextBloqueIndex(), cor, mot, hashArc, self.__getPreviusBloqueHash(), timestamp, self.__zero_count)
        self.__cadena.append(newBloque)

    def __getNextBloqueIndex(self):
        return len(self.__cadena)

    def __getPreviusBloqueHash(self):
        return self.getHashByIndex(self.__getNextBloqueIndex() - 1)

    def crearBloque(self, cor, mot, hashArc):
        newBloque = Bloque(self.__getNextBloqueIndex(), cor, mot, hashArc, self.__getPreviusBloqueHash(), datetime.utcnow, self.__zero_count)
        self.__cadena.append(newBloque)

    def getHashByIndex(self, index):
        return self.__cadena[index].hashBloque
    
    def getBloqueByIndex(self, index):
        return self.__cadena[index]
    
    def getJsonBloqueByIndex(self, index):
        return json.dumps(self.__cadena[index], sort_keys=True, default=json_util.default)

    def setZero_count(self, count):
        self.__zero_count = count
