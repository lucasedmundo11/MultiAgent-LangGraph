# Documentação da API MultiAgent-LangGraph

## Visão Geral
A API MultiAgent-LangGraph é um serviço RESTful construído utilizando Flask. Ela gerencia interações entre agentes conversacionais e de pesquisa para fornecer respostas estruturadas e enriquecidas por meio da biblioteca LangGraph.

## URL Base
A API é acessível na seguinte URL quando executada localmente:
```
http://localhost:5001/api
```

Se implantada em um ambiente remoto, substitua `localhost` pelo domínio apropriado.

---

## **Endpoint Principal**
### `POST /api`

### **Descrição**
Este endpoint processa uma requisição contendo uma mensagem do usuário. A mensagem é analisada pelos agentes, que utilizam fluxos de decisão para gerar uma resposta.

### **Requisição**
- **Método**: `POST`
- **Cabeçalhos Requeridos**:
  - `Content-Type: application/json`
- **Corpo da Requisição (JSON)**:
  ```json
  {
    "message": "Texto da mensagem a ser processada"
  }
  ```

### **Exemplo de Requisição**
```bash
curl -X POST "http://localhost:5001/api" \
     -H "Content-Type: application/json" \
     -d '{"message": "Explique a teoria da relatividade."}'
```

### **Resposta**
- **Código 200 - Sucesso**:
  - Retorna a resposta final processada pelos agentes.
  ```json
  {
    "message": "Explique a teoria da relatividade.",
    "response": "A teoria da relatividade, proposta por Albert Einstein, consiste em duas partes: a relatividade restrita e a relatividade geral..."
  }
  ```
- **Código 400 - Erro na Requisição**:
  - Se o corpo da requisição estiver malformado.
  ```json
  {
    "error": "O campo 'message' é obrigatório."
  }
  ```
- **Código 500 - Erro Interno**:
  - Em caso de falha no processamento interno da API.
  ```json
  {
    "error": "Erro interno do servidor."
  }
  ```

---

## **Fluxo de Processamento**
1. A requisição é recebida e validada.
2. O fluxo de estados LangGraph é inicializado.
3. A mensagem é enviada para o **Agente de Escrita**.
4. Se necessário, o **Agente de Busca** coleta informações adicionais.
5. A resposta final é gerada e retornada ao usuário.

---

## **Erros Comuns e Soluções**
| Código | Descrição | Possível Solução |
|--------|-----------|-----------------|
| 400 | Campo 'message' ausente ou inválido | Verifique se a requisição inclui o campo `message`. |
| 500 | Erro interno do servidor | Revise logs do servidor para identificar problemas. |

---

## **Executando a API Localmente**

1. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```
2. Configure variáveis de ambiente (`.env`):
   ```plaintext
   OPENAI_API_KEY="sua-chave-api"
   ````
3. Inicie o servidor:
   ```bash
   python app/app.py
   ```
4. A API estará disponível em `http://localhost:5001/api`

---

## **Testes**
Testes podem ser executados utilizando `pytest`:
```bash
pytest tests/
```

---

## **Conclusão**
Esta API facilita interações entre usuários e agentes de IA, fornecendo respostas inteligentes e contextualizadas. Para mais detalhes sobre a arquitetura, consulte a documentação completa do projeto.