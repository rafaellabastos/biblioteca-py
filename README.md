# Biblioteca
Este programa realiza o CRUD: para cada usuário ele cria uma lista com o nome dos livros e informações específicas dele, permite visualizar a lista de livros cadastrados, permite atualizar determinadas informações cadastradas e pode excluir o livro da estante.

## Passo a passo:
1 - Colocar no terminal:
pip install oracledb
pip install pwinput

2 - Colocar suas permissões no SQL Developer
OBS.: também substituir no código as mesmas permissões nos campos determinados

3 - Criar a tabela no SQL Developer

drop table biblioteca cascade constraints;
CREATE TABLE biblioteca (
 ID NUMBER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
 NOME_LIVRO VARCHAR2(50),
 SEÇÃO_LIVRO VARCHAR2(50),
 AUTOR_LIVRO VARCHAR2(50),
 IDADE_MIN INT
);

4 - Entrar no programa com as mesmas permissões do SQL Developer

5 - Executar o programa