# MultiAgent-LangGraph

Este repositório implementa um sistema colaborativo baseado em agentes para gerar conteúdo e realizar pesquisas utilizando a biblioteca LangGraph. O projeto é composto por dois agentes principais:
- **Agente Conversacional**: Focado em criar textos bem estruturados e coerentes.
- **Agente de Busca**: Especializado em realizar pesquisas detalhadas.

Os agentes trabalham em conjunto para cumprir tarefas complexas em um fluxo baseado em estados.

---

## Lógica entre os Agentes

O fluxo de comunicação entre os agentes é baseado em estados e transições definidas na LangGraph. O **Agente de Escrita** inicia o fluxo processando uma solicitação e, caso precise de informações adicionais, transfere a execução para o **Agente de Busca**. Após obter as respostas, o fluxo retorna ao **Agente de Escrita**, que gera o conteúdo final. Caso a resposta seja conclusiva, o fluxo é encerrado automaticamente.

---

## Utilização do LangSmith

O projeto utiliza **LangSmith** para rastreamento e monitoramento das interações entre os agentes, garantindo transparência e melhorando a depuração do fluxo. O LangSmith permite armazenar logs estruturados das conversas, facilitando a análise do desempenho dos agentes e a identificação de melhorias. Com ele, é possível obter métricas detalhadas sobre as execuções e refinar continuamente a lógica do sistema.

---

## Ferramentas Utilizadas pelo Agente de Busca

O **Agente de Busca** utiliza várias ferramentas especializadas para obter informações relevantes:
- **Tavily Search**: Executa buscas detalhadas na web, retornando até 10 resultados refinados.
- **Wikipedia Search**: Obtém resumos de páginas da Wikipedia com base no tema pesquisado.
- **Weather API**: Consulta informações meteorológicas em tempo real.
- **Yahoo Finance News**: Obtém notícias do mercado financeiro.

Essas ferramentas são combinadas para fornecer respostas completas e contextualizadas ao **Agente de Escrita**.

---

## Moderação de Conteúdo sobre Engenharia Civil

Por meio de **prompt engineering**, os agentes são instruídos a evitar discussões sobre Engenharia Civil. Se um usuário solicitar informações sobre esse tema, o sistema responde com um aviso explícito e finaliza a interação. Esse mecanismo garante que o chatbot permaneça alinhado às diretrizes estabelecidas pelo projeto.

---

## Estrutura do Projeto

```
MultiAgent-LangGraph/
├── app/
│   ├── __init__.py               # Inicialização do módulo
│   ├── app.py                    # API principal
│   ├── agents/
│   │   ├── conversational.py     # Código do Agente Conversacional
│   │   ├── search.py             # Código do Agente de Busca
│   │   └── utils.py              # Funções auxiliares
│   └── middleware/
│       └── logging.py            # Registro de logs
├── manifests/
│   ├── deployment.yaml           # Manifesto do Deployment
│   ├── service.yaml              # Manifesto do Service
│   ├── hpa.yaml                  # Manifesto do HPA
├── docker/
│   ├── Dockerfile                # Arquivo Dockerfile
│   └── requirements.txt          # Dependências do projeto
├── tests/
│   ├── test_app.py               # Testes unitários para os agentes e API
├── docs/
│   ├── README.md                 # Documentação do projeto
│   ├── architecture.png          # Diagrama da arquitetura
│   └── api-docs.md               # Documentação detalhada da API
├── .gitignore                    # Ignorar arquivos desnecessários no Git
├── requirements.txt              # Dependências do projeto
└── .env                          # Chaves de API e variáveis de ambiente
```

---

## Configuração e Execução

### 1. Pré-requisitos
Certifique-se de ter as seguintes dependências instaladas:
- Python 3.8 ou superior
- Docker (opcional, para containerização)
- Gerenciador de pacotes `pip`

### 2. Instalação

Clone este repositório e instale as dependências:
```bash
# Clone o repositório
$ git clone https://github.com/seu-usuario/MultiAgent-LangGraph.git
$ cd MultiAgent-LangGraph

# Instale as dependências
$ pip install -r requirements.txt
```

### 3. Configuração
Renomeie o arquivo `.env.example` para `.env` e preencha as variáveis de ambiente com as chaves de API necessárias:
```env
LANGSMITH_TRACING=true
LANGSMITH_ENDPOINT="https://api.smith.langchain.com"
LANGSMITH_API_KEY="sua-api-key"
LANGSMITH_PROJECT="langchain-case"

OPENAI_API_KEY="sua-api-key"
SERPAPI_API_KEY="sua-api-key"
TAVILY_API_KEY="sua-api-key"
OPENWEATHERMAP_API_KEY="sua-api-key"
```

### 4. Execução

#### Localmente:
Execute o servidor Flask:
```bash
$ python app/app.py
```
A API estará disponível em `http://localhost:5001/api`.

#### Usando Docker:
Construa e execute o container:
```bash
$ docker build -t multiagent-langgraph .
$ docker run -p 5001:5001 multiagent-langgraph
```

---

## Testes

Testes unitários estão localizados no diretório `tests/`. Para executar os testes, use:
```bash
$ pytest tests/
```

---

## Documentação

### 1. **Diagrama de Arquitetura**
O fluxo entre os agentes está representado no arquivo `docs/architecture.png`.

![Diagrama de Arquitetura](docs/architecture.png)

### 2. **Documentação da API**
A documentação detalhada da API pode ser encontrada em `docs/api-docs.md`.

---

## Contribuição

1. Fork este repositório.
2. Crie uma branch para suas alterações (`git checkout -b feature/nova-funcionalidade`).
3. Commit suas alterações (`git commit -m 'Adiciona nova funcionalidade'`).
4. Envie para o branch principal (`git push origin feature/nova-funcionalidade`).
5. Abra um Pull Request.

---

## Licença
Este projeto está licenciado sob os termos da [Licença MIT](LICENSE).

---

## Contato
Para mais informações, entre em contato pelo email: `seu-email@dominio.com`

