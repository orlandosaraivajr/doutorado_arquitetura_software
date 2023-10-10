# Consumo de API

Consumo de API para a disciplina Arquitetura de Software: Teoria e Prática - Unesp Rio Claro

### Alunos

José William Pinto Gomes

Orlando Saraiva do Nascimento Júnior

### Visão Geral

Neste projeto, o script <b>Produtor</b> consome os dados via json, processa o dado e realiza o enfileiramento para o servidor RabbitMQ.

O script <b>Consumidor</b> consome o dado e o armazena em dois SGBDs diferentes: PostgreSQL e MySQL, conforme ilustra a imagem a seguir.


![Alt text](diagrama.png?raw=true "Fluxo de consumo de dados via API")

Dentre os vários aprendizados, este projeto explora o uso da metodologia dos [12 fatores](https://12factor.net/pt_br/).

### Servidor teste

1. Clone o repositório
2. Crie um virtualenv 
3. Ative a virtualenv
4. Instale as dependências
5. Rodar servidor micro_django

```console
git clone https://github.com/orlandosaraivajr/doutorado_arquitetura_software.git
cd doutorado_arquitetura_software/micro_django/
virtualenv -p python3 venv
source venv/bin/activate
pip install -r requirements.txt
python micro_django.py runserver
```

### Consumo API

1. Clone o repositório
2. Crie um virtualenv 
3. Ative a virtualenv
4. Instale as dependências
5. Editar credenciais
6. Rodar script producer.py e consumer.py

```console
git clone https://github.com/orlandosaraivajr/doutorado_arquitetura_software.git
cd doutorado_arquitetura_software/cliente/
virtualenv -p python3 venv
source venv/bin/activate
pip install -r requirements.txt
cp env .env
nano .env
python producer.py
python consumer.py
```