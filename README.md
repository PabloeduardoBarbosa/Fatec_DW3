# Fatec_DW3_Projeto_Avaliativo

### Descrição do Algoritmo de Consulta de Dados Meteorológicos

Este algoritmo foi desenvolvido para consultar dados meteorológicos usando a API OpenWeatherMap com base no nome da cidade fornecido pelo usuário.

#### Passos do Algoritmo:

1. Importe as bibliotecas necessárias:
   - `datetime`: Para manipular informações de data e hora.
   - `requests`: Para fazer solicitações HTTP à API OpenWeatherMap.

2. Defina as variáveis:
   - `BASE_URL`: A URL base da API OpenWeatherMap.
   - `API_KEY`: Sua chave de API válida para acessar a API OpenWeatherMap.
   - Solicite ao usuário que insira o nome da cidade usando `input()` e armazene-o na variável `CITY`.

3. Crie uma função `kelvin_to_celcius_fahrenheit` que converte a temperatura de Kelvin para Celsius e Fahrenheit.

4. Construa a URL da API OpenWeatherMap com a chave da API e o nome da cidade fornecidos pelo usuário.

5. Use um bloco `try...except` para capturar exceções que podem ocorrer durante a solicitação da API.

6. Faça uma solicitação GET para a URL da API usando `requests.get(url)` e armazene a resposta em `response`.

7. Verifique o status code da resposta:
   - Se for `200`, a solicitação foi bem-sucedida, e os dados meteorológicos estão disponíveis.
   - Se for `404`, a cidade fornecida não foi encontrada.
   - Para qualquer outro status code, exiba uma mensagem de erro genérica.

8. Se o status code for `200` (OK), analise os dados JSON da resposta:
   - Extraia informações como temperatura, sensação térmica, velocidade do vento, umidade, descrição do clima, nascer do sol e pôr do sol.

9. Converta a temperatura de Kelvin para Celsius e Fahrenheit usando a função `kelvin_to_celcius_fahrenheit`.

10. Exiba as informações meteorológicas formatadas na tela, incluindo:
    - Temperatura em Celsius e Fahrenheit.
    - Velocidade do vento.
    - Umidade.
    - Descrição do clima em formato capitalizado.
    - Horário do nascer do sol e pôr do sol em formato de data e hora.

11. Se o status code for `404`, informe ao usuário que a cidade não foi encontrada.

12. Se ocorrer um erro de conexão durante a solicitação, trate-o e informe ao usuário.

13. Capture exceções gerais e desconhecidas e forneça mensagens de erro apropriadas.

14. O programa é concluído.

Este algoritmo permite aos usuários obter informações meteorológicas atualizadas para a cidade de sua escolha, lida com erros comuns de conexão e fornece feedback adequado com base no status code da API OpenWeatherMap. Certifique-se de ter uma chave de API válida para usar este algoritmo.
