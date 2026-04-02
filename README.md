# 💳 Fraud ML Engineering Platform

Plataforma end-to-end para detecção de fraude em transações financeiras, desenvolvida com foco em **Machine Learning Engineering, MLOps e arquitetura escalável**.

Este projeto simula uma solução próxima ao ambiente real de bancos, cobrindo desde a preparação dos dados até o serving do modelo via API e visualização em dashboard.

---

## 🎯 Objetivo

Construir uma solução de Machine Learning com visão de produto de dados, integrando:

* engenharia de dados
* modelagem preditiva
* avaliação com métricas adequadas
* disponibilização via API
* interface interativa para consumo
* conteinerização para deploy

---

## 🏦 Problema de Negócio

Fraudes em transações financeiras representam um desafio crítico para instituições como bancos e fintechs.

Principais desafios:

* alto volume de transações
* dados altamente desbalanceados
* necessidade de detecção em tempo real
* custo elevado de falsos negativos
* impacto direto no risco financeiro

Neste contexto, o objetivo é detectar fraudes com alta sensibilidade, mantendo equilíbrio com falsos positivos.

---

## 📊 Dataset

Utiliza o dataset público de transações com cartão de crédito:

🔗 https://www.kaggle.com/code/rehamh/credit-card-fraud-detection

* features anonimizadas (`V1` a `V28`)
* `Time`: segundos desde a primeira transação
* `Amount`: valor da transação
* `Class`: variável alvo (0 = normal, 1 = fraude)

> O dataset não está versionado no repositório por restrições de tamanho.

---

## 🧠 Abordagem de Modelagem

Foram avaliados diferentes algoritmos:

* Regressão Logística
* Random Forest
* XGBoost
* Isolation Forest (comparativo)

O modelo escolhido para produção foi:

👉 **Random Forest**

Critérios:

* robustez em dados desbalanceados
* boa performance geral
* interpretabilidade

---

## 📏 Métricas de Avaliação

Devido ao desbalanceamento, priorizamos:

* PR-AUC ⭐
* Recall
* Precision
* F1-score

O ROC-AUC foi utilizado como métrica complementar.

---

## 🏗️ Arquitetura da Solução

```text
Dados → Pré-processamento → Feature Engineering → Treinamento
     → Serialização do modelo → API (FastAPI)
     → Dashboard (Streamlit)
```

---

## 📂 Estrutura do Projeto

```text
fraud-ml-engineering-platform/
│
├── app/                # Dashboard (Streamlit)
├── src/
│   ├── api/            # API (FastAPI)
│   ├── data/           # Preparação de dados
│   ├── models/         # Treino e avaliação
│   ├── schemas/        # Validação de dados
│   ├── services/       # Lógica de predição
│   └── utils/
│
├── models/             # Modelos serializados
├── data/               # Estrutura de dados (sem dataset)
├── notebooks/          # Análises exploratórias
│
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── README.md
```

---

## 🚀 Como Executar

### 🔹 1. Clonar o repositório

```bash
git clone https://github.com/lunarente/fraud-ml-engineering-platform.git
cd fraud-ml-engineering-platform
```

---

### 🔹 2. Criar ambiente virtual

```bash
python -m venv .venv
```

Ativar:

**Windows**

```bash
.venv\Scripts\activate
```

**Linux/Mac**

```bash
source .venv/bin/activate
```

---

### 🔹 3. Instalar dependências

```bash
pip install -r requirements.txt
```

---

### 🔹 4. Rodar API

```bash
uvicorn src.api.main:app --reload --port 8000
```

Acesse:

👉 http://127.0.0.1:8000/docs

---

### 🔹 5. Rodar Dashboard

```bash
streamlit run app/app.py
```

---

### 🔹 6. Rodar com Docker

```bash
docker build -t fraud-ml-app .
docker run -p 8000:8000 fraud-ml-app
```

---

## 🔌 Exemplo de Uso da API

### Endpoint

```text
POST /predict
```

### Payload

```json
{
  "Time": 10000,
  "V1": -1.359807,
  "V2": -0.072781,
  "V3": 2.536347,
  "V4": 1.378155,
  "V5": -0.338321,
  "V6": 0.462388,
  "V7": 0.239599,
  "V8": 0.098698,
  "V9": 0.363787,
  "V10": 0.090794,
  "V11": -0.5516,
  "V12": -0.617801,
  "V13": -0.99139,
  "V14": -0.311169,
  "V15": 1.468177,
  "V16": -0.470401,
  "V17": 0.207971,
  "V18": 0.025791,
  "V19": 0.403993,
  "V20": 0.251412,
  "V21": -0.018307,
  "V22": 0.277838,
  "V23": -0.110474,
  "V24": 0.066928,
  "V25": 0.128539,
  "V26": -0.189115,
  "V27": 0.133558,
  "V28": -0.021053,
  "Amount": 149.62
}
```

---

## 🧪 Testes

```bash
pytest
```

---

## ⚙️ Tecnologias Utilizadas

* Python
* Pandas / NumPy
* Scikit-learn
* XGBoost
* FastAPI
* Streamlit
* Docker
* AWS

---

## 💡 Diferenciais do Projeto

* estrutura modular de engenharia
* separação entre treino e inferência
* API pronta para consumo
* dashboard integrado
* pipeline reprodutível
* foco em métricas de negócio
* organização em padrão escalável

---

## 👩‍💻 Autora

**Luciana Narente**

* GitHub: https://github.com/lunarente
* LinkedIn: https://www.linkedin.com/in/luciana-narente

---

## 📌 Observação Final

Este projeto foi desenvolvido com foco em demonstrar habilidades práticas em Machine Learning Engineering aplicadas ao contexto financeiro, aproximando-se de cenários reais de produção.
