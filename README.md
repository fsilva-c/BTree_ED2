# BTree - ED2
Códigos desenvolvidos para o trabalho 3 da disciplina de Estruturas de Dados 2, ministrada pela prof. Inês Restovic.

## Objetivo
Representar as operações de consulta ao cardápio de um restaurante utilizando árvore b e arquivo sequencial.

## cardapy.csv
Arquivo sequencial em que armazenamos os dados referentes aos itens cadastrados no sistema.

O aquivo segue a seguinte estrutura:
```python
 item = {
        "name" : "NaN",
        "price" : "NaN",
        "igredients" : "NaN",
        "kcal" : "NaN",
        "type_item" : "NaN",
        "type_drink" : "NaN",
        "flavor_drink" : "NaN",
        "type_protein" : "NaN",
        "protein_portion" : "NaN"
    }
```
###### Exemplo:
```csv
name,price,igredients,kcal,type_item,type_drink,flavor_drink,type_protein,protein_portion
FRANGO ASSADO,25.99,"FRANGO, MOLHO DE TOMATE",600,2,NaN,NaN,carne,5
```

