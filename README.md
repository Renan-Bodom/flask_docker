# CarFord
### Desafio técnico da AdviceHealth

Da inicialização do sistema:

- Para iniciar todos os componentes utilizando o Docker Compose, certifique-se de estar na pasta raiz do projeto, onde se encontra o arquivo docker-compose.yml.

- Em seguida, execute o seguinte comando (pode ser necessário utilizar root dependendo do sistema):

$ `docker-compose up`

- Aguarde a inicialização dos contêineres docker, o tempo de inicialização pode variar conforme o hardware utilizado.

- Enquanto o banco é configurado com as devidas tabelas e colunas, o sistema não ficará disponível, podendo apresentar erro de sobrecarga. Uma vez que o banco ainda não esta disponível para utilização do sistema.

- Aguarde um tempo ou acompanhe pelo terminal a inicialização do banco MySQL. Ao final, basta acessar o ip 127.0.0.1:5000 pelo navegador de internet.

- Para uma melhor experiência com o sistema, o comando a seguir pode ser executado para inserir alguns dados ao banco (lembre-se de estar na pasta raiz do projeto e da necessidade de utilizar root):

$ `docker exec -i db-carford mysql -uroot -pnork < api/db/dadosTeste.sql`


Do uso:

- A lixeira vermelha exclui o morador, se o mesmo possuir carro(s), os carro(s) também são eliminados do banco.

- O X azul exclui os carros e mantém os moradores cadastrados.

- Moradores com mais de 3 carros são identificados na página de cadastrar carros. Assim como moradores sem carros identificados na página home.


Extra:

Para acessar o terminal do docker contendo o MySQL, execute o comando:

$ `docker exec -it db-carford /bin/bash`

Em seguida, para realizar consultas direto no banco, e verificar o relacionamento, execute:

$ `mysql -uroot -pnork`
$ `use nork`

Lista de moradores:

$ `select * from moradores;`

Consulta relacionada:

$ `SELECT moradores.name, cars.modelo, cars.cor FROM cars INNER JOIN moradores ON cars.morador_idmoradores = moradores.id;`
