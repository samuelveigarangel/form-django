def origem_destino_iguais(origem, destino, lista_de_erros):
    """ Verifica se origem e destino são iguais


    :param origem: A cidade de origem a ser informada
    :param destino: A cidade de destino a ser informada
    :param lista_de_erros: Uma lista com mensagem de erro de campos não podem ser iguais
    :return: mesagem de erro por referencia. mutavel
    """
    if origem.lower() == destino.lower():
            lista_de_erros['destino'] = 'Origem e destino não podem ser iguais'

def campo_tem_algum_numero(valor_campo, nome_campo, lista_de_erros):
    """ Verifica se possui algum digito numérico


    :param valor_campo: Objeto campo
    :param nome_campo:  O nome do campo a ser informado
    :param lista_de_erros: Uma lista com mensagem de erro não incluir números
    :return: messagem de erro por rreferencia. mutavel
    """
    if any(char.isdigit() for char in valor_campo):
        lista_de_erros[nome_campo] = 'Não inclua números neste campo'

def verifica_data(data_ida, data_volta, data_pesquisa, lista_de_erros):
    '''
    :param ida: data da viagem de ida
    :param volta:  data da viagem de volta
    :param lista_de_erros:  lista de erros
    :return: messagem erro por referencia. mutavel
    '''
    if data_ida > data_volta:
        lista_de_erros['data_ida'] = 'Data maior que a da volta.'

def verifica_data_pesquisa(data_ida, data_volta, data_pesquisa, lista_de_erros):

    if data_ida < data_pesquisa:
        lista_de_erros['data_ida'] = 'Data de ida anterior ao dia de hoje.'