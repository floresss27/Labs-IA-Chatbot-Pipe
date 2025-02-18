# 📌 Chatbot PIPE - Assistente de Projetos

Este é um chatbot desenvolvido para auxiliar pesquisadores e empresas na submissão de projetos para o **PIPE** (Programa de Inovação Tecnológica da FAPESP). O chatbot responde perguntas frequentes e fornece suporte para quem deseja participar do programa.

---

### **Clone e crie um ambiente virtual do python**
```bash
python3 -m venv env
source env/bin/activate  # Linux/Mac
env\Scripts\activate     # Windows
```
### **Instalar as dependências**
```bash
pip install -r requirements.txt
```

### **Treinar o modelo**
```bash
python model.py
```
Isso criará o arquivo `chatbot_model.h5` e os arquivos `words.pkl` e `classes.pkl`.

---

## **Como Rodar o Chatbot**
### **Iniciar a API Flask**
```bash
python chatbot.py
```
Isso iniciará um servidor Flask que processará as mensagens enviadas pelo chatbot.

### **Rodar a Interface Web (Streamlit)**
Em outro terminal, execute:
```bash
streamlit run app.py
```
Agora, acesse o chatbot pelo navegador em:
```
http://localhost:8501
```

---

## Explicação das Intenções (`intents.json`)
O chatbot é baseado em um conjunto de **intenções** que representam categorias de perguntas e respostas.  

| **Tag**                  | **Descrição** |
|--------------------------|--------------|
| `saudacao`              | Responde a saudações como "Oi", "Olá", "E aí". |
| `despedida`             | Lida com despedidas como "Tchau", "Até logo". |
| `sobre_pipe`            | Explica o que é o **PIPE** e seu propósito. |
| `como_participar`       | Explica quem pode se inscrever no **PIPE**. |
| `financiamento`         | Explica se o **PIPE** oferece financiamento e como funciona. |
| `documentacao`          | Lista os documentos necessários para inscrição. |
| `prazo`                | Explica os prazos de inscrição no **PIPE**. |
| `avaliacao`            | Explica os critérios usados para avaliar os projetos. |
| `problemas_inscricao`   | Dá suporte para quem está com problemas na inscrição. |
| `contato_suporte`       | Fornece informações de contato com o suporte do **PIPE**. |
| `requisitos_empresa`    | Explica os requisitos para empresas participarem. |
| `tempo_aprovacao`      | Explica quanto tempo leva para a aprovação do projeto. |
| `uso_dos_recursos`      | Explica onde os recursos do **PIPE** podem ser usados. |
| `propriedade_intelectual` | Explica quem detém os direitos dos projetos aprovados. |
| `reprovacao`           | Explica o que fazer caso o projeto seja recusado. |
| `curiosidade`          | Conta fatos interessantes sobre o **PIPE**. |
| `agradecimento`        | Responde a agradecimentos como "Obrigado". |
| `nao_entendi`         | Responde quando o chatbot não entende a pergunta. |

---