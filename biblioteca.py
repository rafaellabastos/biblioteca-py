"""
1. Cadastrar livro: cadastra um novo livro gerando automaticamente um ID
2. Listar livros: captura todos os livros gravados na tabela e os apresenta no terminal
3. Alterar livro: faz a edição do registro caso o ID solicitado exista
4. Excluir livro: apaga o registro da tabela caso o ID solicitado exista
5. Sair: encerra a execução da aplicação
"""

# Importar as bibliotecas
import oracledb
import pwinput


# Conexão com o banco de dados
try:
    usuario = input('Usuário: ')
    senha = pwinput.pwinput('Senha: ')

    conn = oracledb.connect(user=usuario, password=senha, host="oracle.fiap.com.br", port=1521, service_name='ORCL')

    cursor = conn.cursor()

except Exception as erro:
    print(f'Erro: {erro}')
    conexao = False

else:
    conexao = True


# Cadastrar informações do livro
def cadastrar():
    try:
        print('\n-----CADASTRAR LIVRO-----')

        nome = input('Digite o nome do livro: ')
        secao = input('Digite a seção do livro: ')
        autor = input('Digite o autor do livro: ')
        idade = int(input('Digite a idade mínima: '))

        cadastro = f"""INSERT INTO biblioteca (NOME_LIVRO, SECAO_LIVRO, AUTOR_LIVRO, IDADE_MIN) VALUES ('{nome}', '{secao}', '{autor}', {idade})"""

        cursor.execute(cadastro)
        conn.commit()

    except ValueError:
        print('Digite um número inteiro para a idade!')
    
    except:
        print('Erro na transação do BD')
    
    else:
        print('\nDados gravados com sucesso')


# Listar livros cadastrados
def listar():
    try: 
        print('\n-----LISTA DOS LIVROS-----')

        lista_dados = []

        consulta = f"""SELECT * FROM biblioteca"""

        cursor.execute(consulta)
        data = cursor.fetchall()

        for dt in data:     
            lista_dados.append(dt) 

        lista_dados = sorted(lista_dados)

        if len(lista_dados) == 0:   
            print(f'\nNão há livros cadastrados')
        else: 
            for item in lista_dados:
                print(item)

    except:
        print('Erro na transação do BD')
    
    else:
        input('\nPressione ENTER para continuar')


# Alterar informações do livro
def alterar():
    try:
        print("\n-----ALTERAR LIVRO-----")

        lista_dados = []

        livro_id = int(input('Escolha um ID: '))

        consulta = f"""SELECT * FROM biblioteca WHERE id = {livro_id}"""

        cursor.execute(consulta)
        data = cursor.fetchall()

        for dt in data:
            lista_dados.append(dt)

        if len(lista_dados) == 0:
            print('\nNão há um livro cadastro com esse ID')
        else:
            novo_nome = input('Digite um novo nome: ')
            nova_secao = input('Digite uma nova seção: ')
            novo_autor = input('Digite um novo autor: ')
            nova_idade = int(input('Digite uma nova idade mínima: '))

            alteracao = f"""UPDATE biblioteca SET
                            nome_livro = '{novo_nome}',
                            secao_livro = '{nova_secao}',
                            autor_livro = '{novo_autor}',
                            idade_min = '{nova_idade}'
                            WHERE id = {livro_id}"""
            cursor.execute(alteracao)
            conn.commit()

            print('\nDados atualizados com sucesso')

    except ValueError:
        print('\nDigite um valor inteiro')
    
    except Exception:
        print('\nErro na transação com o BD')
    
    else: 
        input('\nPressione ENTER para continuar')


# Excluir livro
def excluir():
    try:
        print('\n-----EXCLUIR LIVROS-----')

        lista_dados = []

        livro_id = int(input('Escolha um ID: '))

        consulta = f"""SELECT * FROM biblioteca WHERE id = {livro_id}"""

        cursor.execute(consulta)
        data = cursor.fetchall()

        for dt in data:
            lista_dados.append(dt)

        if len(lista_dados) == 0:
            print('\nNão há um livro cadastrado com esse ID')
        
        else:
            exclusao = f"""DELETE FROM biblioteca WHERE id = {livro_id}"""

            cursor.execute(exclusao)
            conn.commit()

            print('\nLivro excluído com sucesso')

    except ValueError:
        print('\nDigite um número inteiro para o id')
    
    except Exception:
        print('\nErro de transação no BD')


# Menu de opções
while conexao:
    print('\n1. Cadastrar livro'
          '\n2. Listar livros'
          '\n3. Excluir livro'
          '\n4. Alterar livro'
          '\n5. Sair')
    
    escolha = int(input('Selecione uma opção: '))

    match escolha:
        case 1:
            cadastrar()

        case 2: 
            listar()

        case 3:
            excluir()

        case 4:
            alterar()

        case 5:
            print('Fim de programa!')
            break
        
        case _:
            print('Opção incorreta')
