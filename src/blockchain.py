from datetime import datetime

class Block:
    def __init__(self, cor, mot, arc):
        self.correo = cor
        self.motivo = mot
        self.archivo = arc
        self.timestamp = datetime.now()