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


def funcao_pacotes_enviados_vendedor(pacotes):
    dicionario_vendedores = {}

    for pacote in pacotes:
        if pacote.funcao_cod_valido() == "VÁLIDO":
            if pacote.funcao_cod_vendedor() in dicionario_vendedores:
                dicionario_vendedores[pacote.funcao_cod_vendedor()] = dicionario_vendedores[
                                                                          pacote.funcao_cod_vendedor()] + 1
            else:
                dicionario_vendedores[pacote.funcao_cod_vendedor()] = 1

    return dicionario_vendedores


def funcao_relatorio_tipo_destino(pacotes):
    for pacote in funcao_agrupar_pacote_regiao(pacotes):
        if pacote.funcao_cod_valido() == "VÁLIDO":
            print("Região Destino: " + pacote.funcao_destino() + " - Tipo: " + pacote.funcao_tipo_produto())


def main():
    pacotes = [
        Pacote('888555555123888'), Pacote('333333555584333'), Pacote('222333555124000'),
        Pacote('000111555874555'), Pacote("111888555654777"), Pacote("111333555123333"),
        Pacote("555555555123888"), Pacote("888333555584333"), Pacote("111333555123555"),
        Pacote("111333555124000"), Pacote("333888555584333"), Pacote("555888555123000"),
        Pacote("111888555123555"), Pacote("888000555845333"), Pacote("000111555874000")
    ]

    print("a) Identificar o destino de cada pacote:")
    for pacote in pacotes:
        print(pacote.funcao_destino())

    print("b) Saber quais pacotes possuem códigos de barras válidos e/ou inválidos:")
    for pacote in pacotes:
        if pacote.funcao_cod_valido() == "VÁLIDO":
            print(pacote.codigo)

    print("c) Identificar se algum pacote que tem como origem a região Sul tem Brinquedos em seu conteúdo:")
    tem_brinquedos = False
    for pacote in pacotes:
        if pacote.funcao_existe_produto_regiao("Sul", "Brinquedos") == "VÁLIDO":
            tem_brinquedos = True
    if tem_brinquedos:
        print("Tem Brinquedos na Região Sul")
    else:
        print("Não tem Brinquedos na Região Sul")

    print("d) Listar os pacotes agrupados por região de destino (Considere apenas pacotes válidos):")
    lista_agrupados = funcao_agrupar_pacote_regiao(pacotes)
    for pacote in lista_agrupados:
        print(pacote.codigo + " - Região: " + pacote.funcao_destino())

    print("e) Listar o número de pacotes enviados por cada vendedor (Considere apenas pacotes válidos):")
    dicionario_vendedores = funcao_pacotes_enviados_vendedor(pacotes)
    for chave in dicionario_vendedores:
        print(chave + " Pacotes enviados: " + str(dicionario_vendedores[chave]))

    print("f) Gerar o relatório/lista de pacotes por destino e por tipo (Considere apenas pacotes válidos):")
    funcao_relatorio_tipo_destino(pacotes)


main()
