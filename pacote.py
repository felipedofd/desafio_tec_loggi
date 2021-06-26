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

    def funcao_destino(self):
        if self.codigo[3:6] == "111":
            return "Centro-oeste"
        elif self.codigo[3:6] == "333":
            return "Nordeste"
        elif self.codigo[3:6] == "555":
            return "Norte"
        elif self.codigo[3:6] == "888":
            return "Sudeste"
        elif self.codigo[3:6] == "000":
            return "Sul"
        else:
            return "INVÁLIDO"

    def funcao_cod_loggi(self):
        return self.codigo[6:9]

    def funcao_cod_vendedor(self):
        return self.codigo[9:12]

    def funcao_tipo_produto(self):
        if self.codigo[12:15] == "000":
            return "Jóias"
        elif self.codigo[12:15] == "111":
            return "Livros"
        elif self.codigo[12:15] == "333":
            return "Eletrônicos"
        elif self.codigo[12:15] == "555":
            return "Bebidas"
        elif self.codigo[12:15] == "888":
            return "Brinquedos"
        else:
            return "INVÁLIDO"

    def funcao_cod_valido(self):
        if len(self.codigo) == 15 and self.funcao_origem() != "INVÁLIDO" and self.funcao_destino() != "INVÁLIDO" and self.funcao_tipo_produto() != "INVÁLIDO":
            return "VÁLIDO"
        else:
            return "INVÁLIDO"

    def funcao_existe_produto_regiao(self, origem, produto):
        if (self.funcao_origem() == origem and self.funcao_tipo_produto() == produto):
            return "Tem " + produto + " na Região " + origem
        else:
            return "Não Tem " + produto + " na Região " + origem



