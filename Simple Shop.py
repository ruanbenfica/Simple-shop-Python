from datetime import date
data =  date.today()

#Recolhe as informações do usuário e calcula o limite
def obter_limite():

    print ('\n\033[;1mSeja bem vindo a loja Tilty, aqui quem fala é o Ruan Gabriel.')
    print ('Para prosseguir precisamos fazer uma análise de crédito, por favor preencha as seguintes informações.\033[0;0m')


#Dados que o usuário irá digitar
    while True:

        cargo=input('Cargo:')
        valor=1

        while cargo.isnumeric():
            print('\033[31mCargo inválido, digite novamente.\033[0;0m')
            valor=0
            break

        if valor==1:
            break
    while True:
        try:
            salario = float(input('Salário:R$ '))
            if not 0 <= salario <= 90000000000:
                raise ValueError()
        except ValueError:
            print('\033[31mSalário inválido, digite novamente.\033[0;0m')
        else:
            break
    while True:
        try:
            ano_de_nascimento = int(input('Data de nascimento: '))
            if not 1900 <= ano_de_nascimento <= data.year:
                raise ValueError()
        except ValueError:
            print('\033[31mData de nascimento inválida, digite novamente.\033[0;0m')
        else:
            break

#Os dados do usuário serão mostrados na tela
    print()
    print('-'*100)
    print ('Essa são suas informações:')
    print ('Cargo:',cargo)
    print ('Salário:R$',salario)
    print ('Ano de nascimento:',ano_de_nascimento)


#Calculo da idade do usuário
    idade = int(data.year - ano_de_nascimento)
    print('Idade aproximada: {} anos'.format(idade))

# Análise de crédito do usuário
    limite = float(salario*(idade/1000))+100
    print('\nFizemos sua análise de crédito e você foi aprovado!! Esse é seu limite para gastar:\033[42m R$ {:.2f}\033[0;0m'.format(limite))
    print('-'*100)

    return limite,idade


#Solicita o valor dos produto e verifica se o usuário pode comprar
def verificar_produto(limite,idade):

    while True:
        preço=1

        while True:
            try:
                nome_produto = input('\nDigite o nome do produto que deseja comprar:')
                if nome_produto=='':
                    raise ValueError()
            except ValueError:
                print('\n\033[31mPreenchimento inválido, por favor digite o nome de um produto\033[0;0m.')
            else:
                break

        while True:
            try:
                preço_produto = float(input('\nDigite o preço do produto:R$'))
                if not 0 <= preço_produto <= 90000000000:
                    raise ValueError()
            except ValueError:
                print('\n\033[31mPreço do produto inválido, digite novamente.\033[0;0m')
            else:
                break

        valor_restante = float(limite - preço_produto)
        preço=1

        while preço_produto>limite:
            print('\n\033[31mO valor do produto ultrapassou seu saldo disponível, por favor, escolha outro produto.\033[0;0m')
            preço=0
            break

        if preço==1:
            break


    if preço_produto <= (0.6*limite):
    
        print('\nLiberado!')

    elif (0.9*limite) >= preço_produto >(0.6*limite):

        print('\nLiberado para pagar em até 2 vezes!')

    elif (0.9*limite)< preço_produto <=(1*limite):

        print('\nLiberado para pagar em até 3 vezes!')

    else:
    
        print('\nBloqueado!')


    #Cálculo de desconto
    valor_restante = float(limite - preço_produto)
    meu_nome = ('Ruan Gabriel Benfica Manoel')
    nome_separado = ('Ruan', 'Gabriel', 'Benfica', 'Manoel')
    desconto = len(nome_separado[0])
    valor_final = (preço_produto) - (desconto)

    if idade <= preço_produto <= len(meu_nome):

        print('\nVocê terá um desconto de R$',(float(desconto)))

        print('Valor com desconto:R$',valor_final)

        valor_restante=(limite-valor_final)

    print('\nSeu saldo restante é de:\033[42mR${:.2f}\033[0;0m'.format(valor_restante))
    print('-'*100)

    return valor_restante



#Cadastro de itens
def cadastro(valor_restante):

    while True:
        compra=1
        pergunta = input('\nGostaria de comprar mais algum produto?(SIM, NÃO)').upper()
        while not ((pergunta=='SIM') or (pergunta=='NÃO')):
            print('\n\033[31mPreenchimento inválido, digite novamente.\033[0;0m')
            compra=0
            break
        if compra==1:
            break
    while pergunta=='NÃO':
        print('\n\033[;1mObrigado por comprar na loja Tilty!')
        break



    if pergunta=="SIM":
        while True:
            try:
                quantidade = int(input('\nQuantos produtos a mais deseja comprar? '))
                if not 0 <= quantidade <= 50000000:
                    raise ValueError()
            except ValueError:
                print('\n\033[31mQuantidade inválida, digite novamente.\033[0;0m')
            else:
                break

        for prod in range(quantidade):
            limite=valor_restante
            valor_restante=verificar_produto(limite, idade)
        print('\n\033[;1mObrigado por comprar na loja Tilty!')



limite,idade=obter_limite()
valor_restante=verificar_produto(limite,idade)
cadastro(valor_restante)
























          



    
    


