#-*- coding: utf-8 -*-
# python 2.7
alpha = {} #Existe um alfabeto escondido dentro de alguma corredor do bloco C. Procure e tente executar o código

def gernerate(chars):
	result = ''
	for char in chars:
		if char in alpha:
			result += alpha[char]
		else:
			result += char
	return result

input_chars = raw_input("Insira uma sequencia de caracteres: \n")

print(gernerate(input_chars)
