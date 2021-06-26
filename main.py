from pacote import Pacote


def funcao_agrupar_pacote_regiao(pacotes):
    lista_agrupada = []
    lista_sul = []
    lista_centro_oeste = []
    lista_norte = []
    lista_nordeste = []
    lista_sudeste = []

    for pacote in pacotes:
        if pacote.funcao_cod_valido() == "VÁLIDO":
            if pacote.funcao_destino() == "Sul":
                lista_sul.append(pacote)
            elif pacote.funcao_destino() == "Norte":
                lista_norte.append(pacote)
            elif pacote.funcao_destino() == "Sudeste":
                lista_sudeste.append(pacote)
            elif pacote.funcao_destino() == "Centro-oeste":
                lista_centro_oeste.append(pacote)
            elif pacote.funcao_destino() == "Nordeste":
                lista_nordeste.append(pacote)

    lista_agrupada.extend(lista_sul)
    lista_agrupada.extend(lista_norte)
    lista_agrupada.extend(lista_nordeste)
    lista_agrupada.extend(lista_sudeste)
    lista_agrupada.extend(lista_centro_oeste)

    return lista_agrupada
def main():
    pacotes = [
        Pacote('888555555123888'), Pacote('333333555584333'), Pacote('222333555124000'),
        Pacote('000111555874555'), Pacote("111888555654777"), Pacote("111333555123333"),
        Pacote("555555555123888"), Pacote("888333555584333"), Pacote("111333555123555"),
        Pacote("111333555124000"), Pacote("333888555584333"), Pacote("555888555123000"),
        Pacote("111888555123555"), Pacote("888000555845333"), Pacote("000111555874000")
    ]


main()
