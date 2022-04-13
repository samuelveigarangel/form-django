def origem_destino_iguais(origem, destino, lista_de_erros):
    """ Verifica se origem e destino são iguais


    :param origem: A cidade de origem a ser informada
    :param destino: A cidade de destino a ser informada
    :param lista_de_erros: Uma lista com mensagem de erro de campos não podem ser iguais
    :return: mesagem de erro
    """
    if origem.lower() == destino.lower():
            lista_de_erros['destino'] = 'Origem e destino não podem ser iguais'

def campo_tem_algum_numero(valor_campo, nome_campo, lista_de_erros):
    """ Verifica se possui algum digito numérico


    :param valor_campo: Objeto campo
    :param nome_campo:  O nome do campo a ser informado
    :param lista_de_erros: Uma lista com mensagem de erro não incluir números
    :return: messagem de erro
    """
    if any(char.isdigit() for char in valor_campo):
        lista_de_erros[nome_campo] = 'Não inclua números neste campo'
