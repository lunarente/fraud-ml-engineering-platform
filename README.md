# Fraud ML Engineering Platform

Plataforma end-to-end para detecção de fraude em transações com cartão de crédito, desenvolvida com foco em Machine Learning Engineering, MLOps e arquitetura escalável em AWS.

Este projeto foi criado para demonstrar a construção de uma solução aplicada ao contexto financeiro, unindo engenharia de dados, machine learning, serving de modelos e visualização interativa de resultados.

---

## Objetivo do Projeto

Desenvolver um portfolio técnico que simule uma solução real de detecção de fraude, cobrindo desde a preparação dos dados até a disponibilização do modelo via API e dashboard.

O foco não é apenas treinar um modelo, mas estruturar um projeto com organização, reprodutibilidade, escalabilidade e visão de produto de dados.

---

## Problema de Negócio

Fraudes em transações financeiras representam um desafio crítico para instituições bancárias. Em cenários reais, o problema envolve:

- grande volume de transações
- classes altamente desbalanceadas
- necessidade de detectar fraudes com rapidez
- equilíbrio entre redução de perdas financeiras e experiência do cliente
- monitoramento contínuo da performance do modelo

Neste projeto, o objetivo é construir uma solução de classificação para apoio à detecção de fraude em cartão de crédito, utilizando o dataset `creditcard.csv`.

---

## Stack Tecnológica

### Linguagens e bibliotecas
- Python
- Pandas
- NumPy
- Scikit-learn
- XGBoost
- Matplotlib / Seaborn

### APIs e aplicações
- FastAPI
- Streamlit

### Engenharia e MLOps
- Git / GitHub
- Docker
- Estrutura modular em `src`
- Notebooks para exploração
- Ambiente virtual com `venv`

### Cloud e arquitetura
- AWS S3
- AWS Glue
- AWS Athena
- AWS Step Functions
- Fundamentos de SageMaker
- Terraform (em evolução)

---

## Estrutura do Projeto

```bash
fraud-ml-engineering-platform/
│
├── dashboard/        # Aplicação interativa para visualização de métricas e simulação de predições
├── data/             # Dados brutos e processados
├── infrastructure/   # Arquitetura cloud, deploy e componentes de infraestrutura
├── notebooks/        # Análises exploratórias e experimentos iniciais
├── src/              # Código principal do projeto (pipeline, treino, avaliação, inferência)
│
├── .dockerignore
├── .gitignore
├── Dockerfile
├── README.md
└── requirements.txt