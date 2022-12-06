# ZSSN

Rede Social de Sobrevivência Zumbi é uma rede social em um cenário de mundo apocalíptico, que tem por função o compartilhamento de recursos entre sobreviventes. Ele também é uma API REST, que fará CRUD entre as informações. Inicialmente será feito em django e utilizara o protocolo HTTP, ou seja, não será em realtime, mas sim baseado em ações.


## Requisitos:
1. Uma página com as notícias das ações de outros usuários;
2. Uma página com um mapa resumido mostrando os sobreviventes perto de você;
3. Uma página com as informações do inventário e que mostre também as estátisticas de sobrevivência;
5. Uma loja de câmbio que apresente filtros de localização, preço e demanda.
6. Um menu que esteja em todas as páginas acima e que mostre informações como localização e recursos essenciais;

* Observações: 
    1. Os recurso não serão mostrados para outros sobrevivêntes, pois isso evitará roubos e furtos;
    2. O mapa o sobrevivente poderar registrar estruturas e locais, para informar possiveis locais de refugio ou hordas de zumbie;

## Tabelas:



1. Sobrevivente:
    * <img src="https://play-lh.googleusercontent.com/G7PgPigYZtgSYuI54jFWR0in7UHakWiPsHIzuqnV5Go9LYVM_tEt7QASOdUuhfBPCNE" width="80px">
    * Nome -> VARCHAR;
    * Idade -> INT;
    * Sexo -> VARCHAR;

2. Localização:
    * <img src="https://static.vecteezy.com/ti/vetor-gratis/p1/155483-mapa-do-tesouro-vector-gratis-vetor.jpg" width="80px">
    * Latitude -> FLOAT;
    * Longitude -> FLOAT;
    * Horário -> DATETIME;
    * sobrevivent -> Sobrevivente;

3. Recurso:https:
    * <img src="https://portalvidalivre.com/uploads/article/image/1528/Design_sem_nome_-_2022-01-24T061629.364.jpg" width="80px">
    * Descrição -> Ex .: "Munição .5mm - Tauros"
    * Quantidade -> INT
    * Validade -> VARCHAR - OBS: Se tiver
    * Tipo: -> VARCHAR - Ex .: "Água, Comida, Medicação, Armas, Munição, Circuito, Mapas, IE(Itens especiais)"