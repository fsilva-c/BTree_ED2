from menu_prog import struct_item

import csv
import os

header = "name,price,igredients,kcal,type_item,type_drink,flavor_drink,type_protein,protein_portion\n"

def system(value):
    if value == "pause":
        var = input("\nPressione uma tecla para continuar... ")

def key_validator(value, INDEX):
    """
        função percorre o arquivo sequencial cardapy.txt e verifica pelo indice se há algum dado
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
    item_write = csv.writer(archive, delimiter = ',')
    item_write.writerow(struct.values())
    archive.close()

def return_dataIndex(INDEX):
    #obtendo o conteudo da posição INDEX
    archive = open("cardapy.csv").readlines()[INDEX]

    #escrevendo em um arquivo temporário o conteúdo de archive
    with open("tempCardapy.csv", "w") as archive_temp:
        archive_temp.write(header)
        archive_temp.write(archive)

    #lendo os dados do item da posição INDEX
    cardapy = open("tempCardapy.csv")
    item_cardapy = csv.DictReader(cardapy)
    os.remove("tempCardapy.csv")
    
    for i in item_cardapy:
        print("Nome: " + i["name"])
        print("Preço: " + i["price"])
        print("Ingredientes: " + i["igredients"])
        print("KCal: " + i["kcal"])
        
        if i["type_item"] == "bebida":
            print("Sabor: " + i["flavor_drink"]) 
        else: 
            print("Tipo de proteína: " + i["type_protein"])
            print("Porção por prato: " + i["protein_portion"])

    cardapy.close()


return_dataIndex(7)
