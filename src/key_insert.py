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

def itemRegister(name_item, price_item, check_name, check_price):
    #verificando se já existe registro com essa chave
    if check_name != None or check_price != None:
        print("JÁ EXISTE UM ITEM CADASTRADO COM ESTE VALOR OU NOME!")
        return

    item = struct_item()
    menu_prog = struct_menu()
    
    item["name"] = name_item

    item["price"] = price_item

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
        print("Preço: R$ " + i["price"])
        print("Ingredientes: " + i["igredients"])
        print("KCal: " + i["kcal"])
        
        if i["type_item"] == "bebida":
            print("Sabor: " + i["flavor_drink"]) 
        else: 
            print("Tipo de proteína: " + i["type_protein"])
            print("Porção por prato: " + i["protein_portion"])

def remove_item(index):
    """[Método recebe um índice correspondente ao arquivo sequencial e remove uma linha inteira deste 
    arquivo, ou seja, um item completo]
    
    Arguments:
        index {[inteiro]} -- [corresponde ao índice do arquivo sequencial]

    """    
    if index is None:
        print("O ELEMENTO NÃO ESTÁ CADASTRADO!")
        return False

    #obtendo a linha do arquivo da posição index
    item_remove = open("cardapy.csv").readlines()[index]

    archive_temp = open("cardapy_temp.csv", "w")

    #recriando o arquivo cardapy.csv sem o item a ser removido
    with open('cardapy.csv', 'r') as f:
        lines = f.readlines()
        for line in lines:
            output = str(line)
            if line == item_remove:
                line = ""
            archive_temp.write(line)

    #close, remove o arquivo antigo e renomeia o arquivo temporario para cardapy.csv
    archive_temp.close()
    os.remove("cardapy.csv")
    os.rename("cardapy_temp.csv", "cardapy.csv")        

def alter_register(index):
    """[Método recebe um índice e altera os campos correspondente ao seu tipo de item, podendo ser bebida 
    ou comida.]
    
    Arguments:
        index {[inteiro]} -- [corresponde ao índice do arquivo sequencial]
    
    """    
    #validação do índice
    if index is None:
        print("O ELEMENTO NÃO ESTÁ CADASTRADO!")
        return False
    
    #print do item
    return_dataIndex(index)
    print("\n==========================================")

    #recebendo o item do arquivo
    item = return_lineIndex(index)
    itemType_enum = struct_item_enum()
    itemType_enum_TypeDrinkOrProtein = struct_menu()
    
    for row in item:
        if row["type_item"] == "bebida":
            type_column = int(input("1-> NOME\n2-> PREÇO\n3-> IGREDIENTES\n4-> KCAL\n5-> TIPO DA BEBIDA\n6-> SABOR DA BEBIDA\n\nInforme o campo do produto que deseja alterar: "))
            type_column = itemType_enum["typeItem_drink"][type_column]

            system("clear")
            if type_column == "type_drink":
                new_value = int(input("1-> SUCO\n2-> REFRIGERANTE\n3-> ÁGUA\n\nInforme o tipo da bebida: "))
                new_value = itemType_enum_TypeDrinkOrProtein["type_drink"][new_value]
            
        else:
            type_column = int(input("1-> NOME\n2-> PREÇO\n3-> IGREDIENTES\n4-> KCAL\n5-> TIPO DA PROTEÍNA\n6-> PORÇÕES\n\nInforme o campo do produto que deseja alterar: "))
            type_column = itemType_enum["typeItem_protein"][type_column]

            system("clear")
            if type_column == "type_protein":
                new_value = int(input("1-> CARNE\n2-> PEIXE\n3-> VEGANO\n\nInforme o tipo da proteína: "))
                new_value = itemType_enum_TypeDrinkOrProtein["type_protein"][new_value]

        system("clear")
        if type_column == "name" or type_column == "price" or type_column == "igredients" or type_column == "kcal" or type_column == "flavor_drink":
            new_value = input("Informe o novo valor para o campo: ")
            if type_column == "name" or type_column == "igredients":
                new_value = new_value.upper()

        row[type_column] = new_value

        new_item = row

    remove_item(index)
    input_archive(new_item)

    #end method

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
