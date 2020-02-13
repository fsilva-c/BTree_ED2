from structs_prog import *

import csv
import os

header = "name,price,igredients,kcal,type_item,type_drink,flavor_drink,type_protein,protein_portion\n"

def system(value):
    if value == "pause":
        var = input("\nPressione uma tecla para continuar... ")
        
    elif value == "clear":
        print("\033c")
        #print(chr(27) + "[2j]")
        #print("\x1bc")

def itemRegister():
    item = struct_item()
    menu_prog = struct_menu()
    
    item["name"] = input("Informe o nome do produto: ")
    #caixa alta
    item["name"] = item["name"].upper()
    if key_validator(item["name"], "name") == False:
        return

    item["price"] = input("Informe o preco do produto: ")
    if key_validator(item["price"], "price") == False:
        return

    item["igredients"] = input("Informe os igredientes: ")
    item["igredients"] = item["igredients"].upper()
    
    item["kcal"]  = input("Informe a quantidade de kcal contida no item: ")
    
    while(True):
        item["type_item"] = int(input("1-> BEBIDA\n2-> COMIDA\n\nInforme o tipo do item: "))
        item["type_item"] = menu_prog["type_item"][item["type_item"]]

        if item["type_item"] == "bebida":
            item["type_drink"] = int(input("1-> SUCO\n2-> REFRIGERANTE\n3-> ÁGUA\n\nInforme o tipo da bebida: "))
            item["type_drink"] = menu_prog["type_drink"][item["type_drink"]]

            item["flavor_drink"] = input("Informe o sabor da bebida: ")
            break

        elif item["type_item"] == "comida":
            item["type_protein"] = int(input("1-> CARNE\n2-> PEIXE\n3-> VEGANO\n\nInforme o tipo da proteína: "))
            item["type_protein"] = menu_prog["type_protein"][item["type_protein"]]

            item["protein_portion"] = input("Informe a quantidade de porções que o prato rende: ")
            break

    input_archive(item)

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
            print("JÁ EXISTE UM ITEM CADASTRADO COM VALOR OU NOME " + value + "!")
            system("pause")

            return False

    archive.close()


def input_archive(struct):
    """
    função recebe um dicionário (novo item do cardapio) e escreve no arquivo cardapy.csv
    os valores que correspondem a cada chave.
    """
    archive = open("cardapy.csv", "a")
    item_write = csv.writer(archive, delimiter = ',')
    item_write.writerow(struct.values())
    archive.close()

def return_lineIndex(index):
    """ Método recebe uma chave e retorna um dicionário contendo os dados daquela linha do arquivo 
    sequencial."""

    #obtendo o conteudo da posição INDEX
    archive = open("cardapy.csv").readlines()[index]

    #escrevendo em um arquivo temporário o conteúdo de archive
    with open("tempCardapy.csv", "w") as archive_temp:
        archive_temp.write(header)
        archive_temp.write(archive)

    #lendo os dados do item da posição INDEX do arquivo temporário
    cardapy = open("tempCardapy.csv")
    item_cardapy = csv.DictReader(cardapy)
    os.remove("tempCardapy.csv")

    return item_cardapy

def return_dataIndex(index):
    """ Método recebe uma chave e retorna os dados relacionados ao item. """
    if index is None:
        print("O ELEMENTO NÃO ESTÁ CADASTRADO!")
        return False

    line_cardapy = return_lineIndex(index)
    
    for i in line_cardapy:
        print("Nome: " + i["name"])
        print("Preço: " + i["price"])
        print("Ingredientes: " + i["igredients"])
        print("KCal: " + i["kcal"])
        
        if i["type_item"] == "bebida":
            print("Sabor: " + i["flavor_drink"]) 
        else: 
            print("Tipo de proteína: " + i["type_protein"])
            print("Porção por prato: " + i["protein_portion"])

def remove_item(index):
    if index is None:
        print("O ELEMENTO NÃO ESTÁ CADASTRADO!")
        return False

    item_remove = open("cardapy.csv").readlines()[index]

    archive_temp = open("cardapy_temp.csv", "w")

    with open('cardapy.csv', 'r') as f:
        lines = f.readlines()
        for line in lines:
            output = str(line)
            if line == item_remove:
                line = ""
            archive_temp.write(line)
            
    archive_temp.close()
    os.remove("cardapy.csv")
    os.rename("cardapy_temp.csv", "cardapy.csv")        

def alter_register(index):
    remove_item(index)

    itemRegister()

def return_nameItem(index):
    """ Método printa na tela o nome e valor do item da posição index que foi passado como 
    parâmetro na função
    
    Arguments:
        index {[int]} -- [Índice recuperado da btree]
    """    
    line_cardapy = return_lineIndex(index)

    for i in line_cardapy:
        print("NOME:", i["name"])
        print("VALOR:", i["price"])