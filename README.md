# Biblioteca
Este programa realiza o CRUD de uma biblioteca: ele cadastra o nome do livro e informações específicas dele, permite visualizar a lista dos livros cadastrados, permite atualizar determinadas informações cadastradas e pode excluir o livro da estante.

## Passo a passo:
1 - Colocar no terminal:
<br>pip install oracledb
<br>pip install pwinput

2 - Colocar suas permissões no SQL Developer
<br>OBS.: também substituir no código as mesmas permissões nos campos determinados

3 - Criar a tabela no SQL Developer

drop table biblioteca cascade constraints;
<br>CREATE TABLE biblioteca (
<br>&nbsp; ID NUMBER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
<br>&nbsp; NOME_LIVRO VARCHAR2(50),
<br>&nbsp; SECAO_LIVRO VARCHAR2(50),
<br>&nbsp; AUTOR_LIVRO VARCHAR2(50),
<br>&nbsp; IDADE_MIN INT
<br>);

4 - Entrar no programa com as mesmas permissões do SQL Developer

5 - Executar o programa