import os
import re
isPalavraReservada = ["var", "const", "typedef", "struct", "extends", "procedure",
                      "function", "start", "return", "if", "else", "then", "while", "read", "print", "int",
                      "real", "boolean", "string", "true", "false",
                      "global", "local"]
# if isPalavraReservada.__contains__("var"):
#     print("var"+" é uma palavra reservada")
# Está muito generico ainda precisa vim depois das Strings
findIdentificadores = re.compile(r'[a-zA-Z]\w+')
# Se não tiver ponto, é um número. Se começar ou terminar com ponto, é um erro
findNumerosDecimais = re.compile(r'\d+(\.\d+)?')
if findNumerosDecimais.match(".500"):
    if not ".500".__contains__("."):
        print(".500" + " é um Digito")
    # Talvez esse startswith possa sair
    elif not ".500".endswith(".") and not ".500".startswith("."):
        print(".500"+" é um Número")
    else:
        print(".500"+" é um erro")
findLetras = re.compile(r' [a-zA-Z] ')
# Muito generico, precisa vim depois dos comentarios
findOperadorAritmetico = re.compile(r'[+\-*\/++\-\-]')
findOperadorRelacionais = re.compile(r'==|!=|>|>=|<|<=|=')
findOperadorLogico = re.compile(r'&&|\|\||!')
findComentarioLinha = re.compile(r'\/\/')
# comentario de bloco achei confuso de fazer
findDelimitadores = re.compile(r';|,|\(|\)|{|}|\[|\]|\.')
findCadeiaCaracteres = re.compile(r"(\w+\s?)+")
# Simbolo é tudo???
findLinha = re.compile(r'.+')  # Se quiser pegar todo o conteudo de uma linha


files = os.listdir("./input/")
for file in files:
    pathName = open("./input/"+file, "r")
    codigoFonte = pathName.read()
    # print(codigoFonte)


#out = open("./output/"+file.replace("entrada", "saida"), "w")
# for token in tokens:
#     out.write(token+"\n")
