#Escreva um programa que repita a leitura de uma senha até que ela seja válida. Para cada leitura de
#senha incorreta informada, escrever a mensagem "Senha Invalida! Tente novamente:". Quando a senha
#for informada corretamente deve ser impressa a mensagem "Acesso Permitido" e o algoritmo
#encerrado. Considere que a senha correta é o valor 2022.

senha_correta= 2022
senha= int(input("Digite a senha: "))
if senha==senha_correta:
    print("ACESSO PERMITIDO")
else:
    senha_correta=2022
    while senha != senha_correta:
        senha = int(input("SENHA INVALIDA!!! \nDigite a senha novamente: "))
        if senha==senha_correta:
            print("ACESSO PERMITIDO")






