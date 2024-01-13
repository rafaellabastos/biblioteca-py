# Biblioteca
Este programa realiza o CRUD de uma biblioteca: ele cadastra o nome do livro e informações específicas dele, permite visualizar a lista dos livros cadastrados, permite atualizar determinadas informações cadastradas e pode excluir o livro da estante.

## Passo a passo:
1 - Colocar no terminal:
pip install oracledb
pip install pwinput

2 - Colocar suas permissões no SQL Developer
OBS.: também substituir no código as mesmas permissões nos campos determinados

3 - Criar a tabela no SQL Developer

drop table biblioteca cascade constraints;
<br>CREATE TABLE biblioteca (
<br>ID NUMBER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
<br>NOME_LIVRO VARCHAR2(50),
<br>SEÇÃO_LIVRO VARCHAR2(50),
<br>AUTOR_LIVRO VARCHAR2(50),
<br>IDADE_MIN INT
<br>);

4 - Entrar no programa com as mesmas permissões do SQL Developer

5 - Executar o programa