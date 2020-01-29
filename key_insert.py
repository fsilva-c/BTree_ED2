import csv

def system(value):
    if value == "pause":
        var = input("\nPressione uma tecla para continuar... ")

def key_validator(value, INDEX):
    """
        função percorre o arquivo sequencial cardapy.csv e verifica pelo indice se há algum dado
        igual ao valor passado na insercao de um novo item.
    """

    #casting pois o arquivo é lido em forma de string
    value = str(value)

    archive = open("cardapy.csv")
    items = csv.DictReader(archive)

    #verifica se o valor passado pela funcao é igual a algum dado do arquivo
    for lines in items:
        if lines[INDEX] == value:
            print("Já existe um item cadastrado com valor ou nome " + value + "!")
            system("pause")

            return False

    archive.close()

def input_archive(struct):
    """
    função recebe um dicionário e escreve no arquivo cardapy.csv os valores que correspondem a cada chave.
    """
    archive = open("cardapy.csv", "a")
    item_write = csv.writer(archive, delimiter=',')
    item_write.writerow(struct.values())
    archive.close()
