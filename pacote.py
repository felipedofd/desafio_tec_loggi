class Pacote:
    def __init__(self, codigo):
        self.codigo = codigo

    def funcao_origem(self):
        if self.codigo[0:3] == "111":
            return "Centro-oeste"
        elif self.codigo[0:3] == "333":
            return "Nordeste"
        elif self.codigo[0:3] == "555":
            return "Norte"
        elif self.codigo[0:3] == "888":
            return "Sudeste"
        elif self.codigo[0:3] == "000":
            return "Sul"
        else:
            return "INVÁLIDO"
