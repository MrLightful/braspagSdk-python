import json
from future.utils import integer_types


class ObjectJSON(object):

    def toJSON(self):
        dicionary = json.loads(json.dumps(self, default=lambda o: o.__dict__))

        dicionary = remove_none(dicionary)

        dicionary = process_name_key(dicionary)

        return json.dumps(dicionary, indent=2)

    def prepare(self):
        pass

    def __getattribute__(self, attribute):
        if attribute == '__dict__':
            self.prepare()

        return object.__getattribute__(self, attribute)


def process_name_key(dictionary):

    # If it's a list, process each item.
    if isinstance(dictionary, list):
        new_list = []
        for item in dictionary:
            new_list.append(process_name_key(item))
        return new_list

    # If it's not a dictionary (and not list), just return it as is.
    if not isinstance(dictionary, dict):
        return dictionary

    # If it's a dictionary, process each key/value.
    new_dictionary = {}
    for key in dictionary:
        new_dictionary[capitalize_key(key)] = process_name_key(dictionary[key])
    return new_dictionary


def capitalize_key(key):
    parts = key.split('_')

    new_parts = []
    for part in parts:
        new_parts.append(part.capitalize())

    return ''.join(new_parts)


def remove_none(dado):
    if isinstance(dado, dict):
        return remove_none_dict(dado)
    elif isinstance(dado, list):
        return remove_none_list(dado)

    return dado


def remove_none_dict(obj):
    retorno = {}
    for chave in obj:
        valor = obj[chave]
        types = integer_types + (float, complex)
        if valor or isinstance(valor, types):
            retorno[chave] = remove_none(valor)

    return retorno


def remove_none_list(lista):
    resposta = []
    for linha in lista:
        valor = remove_none(linha)
        resposta.append(valor)

    return resposta
