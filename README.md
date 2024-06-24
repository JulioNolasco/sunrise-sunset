# Micro serviço simples que retorna qual próximo dia e horário do por ou nascer do sol, de acordo com lagitude e longitude passada.

# Configuração
- Faça o clone do arquivo ```.env.example``` com o nome de ```.env```
- Preencha a variavel ```APP_PORT``` com a porta desejada para rodar o projeto

### Utilizando o Docker
- Instale o [Docker](https://www.docker.com/).
- Agora para iniciar a aplicação execute ```docker compose up ```
- URL para requisição ``` /api/sun-info-get ```
- Exemplo de requisição ``` http://127.0.0.1:5000//api/sun-info-get?lat=-23.5653114&lng=-46.642659&type=sunset ```
