# 🚨 Fraud ML Engineering Platform

<p align="center">
  <b>Plataforma end-to-end de Machine Learning para detecção de fraude bancária</b><br>
  <i>Do dado bruto até API escalável e dashboard interativo</i>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10-blue">
  <img src="https://img.shields.io/badge/Machine%20Learning-Random%20Forest-green">
  <img src="https://img.shields.io/badge/API-FastAPI-009688">
  <img src="https://img.shields.io/badge/Dashboard-Streamlit-FF4B4B">
  <img src="https://img.shields.io/badge/Container-Docker-blueviolet">
  <img src="https://img.shields.io/badge/Status-Production%20Ready-success">
</p>

---

## 🎯 Sobre o Projeto

Este projeto simula uma solução real de **detecção de fraude em transações financeiras**, com foco em:

- 🧠 Machine Learning aplicado
- ⚙️ Engenharia de Machine Learning (MLE)
- 🔁 Pipeline end-to-end
- ☁️ Estrutura pronta para cloud (AWS)

A proposta vai além de um modelo:  
👉 entrega uma **plataforma completa**, organizada como um projeto de produção.

---

## 💼 Problema de Negócio

Fraudes financeiras são um dos maiores desafios para bancos.

O problema envolve:

- 📈 Alto volume de transações  
- ⚖️ Dataset extremamente desbalanceado  
- ⚡ Necessidade de resposta em tempo real  
- 💸 Redução de perdas financeiras  
- 👤 Preservação da experiência do cliente  

> 🎯 Objetivo: identificar transações fraudulentas com alta precisão e recall.

---

## 📊 Dataset

📌 **Credit Card Fraud Detection (Kaggle)**

| Feature | Descrição |
|--------|----------|
| `Time` | Segundos desde a primeira transação |
| `Amount` | Valor da transação |
| `V1 - V28` | Features transformadas via PCA |
| `Class` | Target (0 = normal, 1 = fraude) |

---

## 🧠 Modelagem

- 🌲 Random Forest (modelo principal)
- ⚖️ Tratamento de desbalanceamento
- 📏 Métricas utilizadas:
  - PR-AUC (principal)
  - Recall (fraudes)
  - Precision
  - ROC-AUC (comparativo)

---

## 🏗️ Arquitetura do Projeto

### 🔄 Pipeline

```text
Raw Data → Preprocessing → Feature Engineering → Model Training → Model Serving → Dashboard
        ┌──────────────────────────────┐
        │        Dataset Kaggle        │
        └──────────────┬───────────────┘
                       ▼
        ┌──────────────────────────────┐
        │      Pré-processamento       │
        └──────────────┬───────────────┘
                       ▼
        ┌──────────────────────────────┐
        │      Treinamento Modelo      │
        └──────────────┬───────────────┘
                       ▼
        ┌──────────────────────────────┐
        │     Artefatos (modelos)      │
        └───────┬───────────┬──────────┘
                ▼           ▼
        ┌────────────┐ ┌──────────────┐
        │  FastAPI   │ │  Streamlit   │
        └─────┬──────┘ └──────┬───────┘
              └──────┬────────┘
                     ▼
              👤 Usuário final
