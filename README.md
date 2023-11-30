# Exercicio-4

Quarto trabalho da aula de Técnicas de Desenvolvimento de Software Livre: fazer uma API em python que retorna o resultado das operações fatorial e Fibonacci de uma entrada em JSON pelo método POST 

### Funcionamento do código

O código myapi.py conta com a definição de 3 funções, a primeira para fazer o cálculo do fatorial, a segunda para fazer o cálculo da sequência de Fibonacci e a taerceira para carregar os dados em JSON do arquivo data.txt (para teste). Dentro da função decorador, é feito um requisito de que devem existir números nas duas chaves do JSON de entrada. Após isso, caso existam um número para fazer fatorial e um número para fazer Fibonacci, os dados do arquivo .txt são extraídos e as funções de cálculo são chamadas. Por fim, os resultados são colocados em JSON para serem exibidos assim que a função decorador for chamada.

Função decorador: @app.route('/calculos', methods=['POST']) --> define que a função que segue será chamada quando houver uma solicitação POST para a rota /calculos na sua aplicação Flask. 

### Aplicação e visualização no terminal

Após a criação do código foi dado 'export FLASK_APP=myapi.py' e posteriormente um 'flask run' no terminal para iniciar um servidor web.

É retornado o valor da porta em que esse servidor foi iniciado (nesse caso, a porta padrão, 5000), e enquanto ele está aberto, é realizado, em outro terminal, o comando 'curl -X POST http://127.0.0.1:5000/calculos', que retorna pelo método POST os resultados em JSON dos cálculos do código myapi.py.

#### Exemplo de aplicação realizada:

Entrada: {"fact": 6, "fib": 8}
Retorno: {"fact":720,"fib":[0,1,1,2,3,5,8,13]}

