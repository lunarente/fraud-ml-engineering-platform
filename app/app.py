import streamlit as st
import requests
import pandas as pd


API_URL = "http://127.0.0.1:8001/predict"

st.set_page_config(
    page_title="Fraud Detection Dashboard",
    page_icon="💳",
    layout="wide"
)


# =========================
# Funções auxiliares
# =========================
def parse_float(value, default=None):
    """
    Converte string com vírgula ou ponto para float.
    Também aceita valores numéricos nativos.
    """
    try:
        if isinstance(value, str):
            value = value.strip().replace(",", ".")
        return float(value)
    except (ValueError, TypeError):
        return default


def build_transaction_data(time_input, amount_input, variables):
    data = {"Time": time_input}
    data.update(variables)
    data["Amount"] = amount_input
    return data


def get_default_variables():
    return {f"V{i}": 0.0 for i in range(1, 29)}


# =========================
# Session state
# =========================
if "time_input" not in st.session_state:
    st.session_state.time_input = 0.0

if "amount_input" not in st.session_state:
    st.session_state.amount_input = 0.0

if "advanced_mode" not in st.session_state:
    st.session_state.advanced_mode = False

for i in range(1, 29):
    key = f"v_{i}"
    if key not in st.session_state:
        st.session_state[key] = 0.0


# =========================
# Header
# =========================
st.title("💳 Fraud Detection Dashboard")
st.caption("Simulação de predição de fraude em transações com cartão de crédito")

st.markdown("""
Este dashboard consome uma API de inferência treinada com um modelo de classificação
para estimar a probabilidade de fraude em uma transação.
""")

with st.expander("ℹ️ Sobre este projeto"):
    st.markdown("""
Este dashboard faz parte de um projeto de **Machine Learning Engineering** voltado para detecção de fraude em transações de cartão de crédito.

O sistema foi desenvolvido com:

- **Scikit-learn** para treinamento do modelo
- **FastAPI** para serviço de inferência
- **Streamlit** para interface interativa
- **Arquitetura modular em Python**
- **Pipeline de dados e avaliação de modelo**

O objetivo é simular um **motor de scoring antifraude** semelhante aos utilizados em sistemas financeiros.
""")

st.info(
    "Observação: no dataset utilizado, a variável `Time` representa o número de segundos "
    "desde a primeira transação registrada, e não o horário real da transação."
)

st.divider()


# =========================
# Métricas
# =========================
st.subheader("📈 Métricas de referência do modelo")

metric_col1, metric_col2, metric_col3, metric_col4 = st.columns(4)
metric_col1.metric("Recall (fraude)", "0.76")
metric_col2.metric("Precision (fraude)", "0.96")
metric_col3.metric("F1-score", "0.85")
metric_col4.metric("ROC AUC", "0.96")

st.divider()


# =========================
# Informações do modelo
# =========================
col_info1, col_info2, col_info3 = st.columns(3)

with col_info1:
    st.info("**Modelo:** Random Forest")

with col_info2:
    st.info("**Uso:** Simulação de scoring antifraude")

with col_info3:
    st.info("**Status:** API local")


# =========================
# Modo de uso
# =========================
st.subheader("⚙️ Modo de uso")

advanced_mode = st.toggle(
    "Ativar modo avançado (editar V1 a V28)",
    value=st.session_state.advanced_mode,
    help="No modo simplificado, o dashboard usa valores padrão para V1 a V28. No modo avançado, você pode editar manualmente todas as features."
)

st.session_state.advanced_mode = advanced_mode

if advanced_mode:
    st.warning("Modo avançado ativado: as variáveis V1 a V28 ficarão disponíveis para edição manual.")
else:
    st.success("Modo simplificado ativado: apenas os campos principais são exibidos.")


# =========================
# Dados principais da transação
# =========================
st.subheader("🧾 Dados da transação")

col_action1, col_action2, col_action3 = st.columns([1, 1, 3])

with col_action1:
    if st.button("🔄 Carregar exemplo"):
        st.session_state.time_input = 406.0
        st.session_state.amount_input = 149.62
        st.session_state.advanced_mode = False

        for i in range(1, 29):
            st.session_state[f"v_{i}"] = 0.0

with col_action2:
    if st.button("🚨 Simular fraude"):
        st.session_state.time_input = 472.0
        st.session_state.amount_input = 1.00
        st.session_state.advanced_mode = True

        for i in range(1, 29):
            st.session_state[f"v_{i}"] = 0.0

        st.session_state["v_4"] = 2.5
        st.session_state["v_10"] = -5.0
        st.session_state["v_12"] = -6.0
        st.session_state["v_14"] = -8.0
        st.session_state["v_17"] = -7.0

with col_action3:
    st.caption("Use os botões para testar rapidamente a integração com a API.")

st.caption("O botão de simulação utiliza valores extremos em features relevantes para aumentar a probabilidade de fraude.")

col1, col2 = st.columns(2)

with col1:
    time_raw = st.text_input(
        "Tempo desde a primeira transação (segundos)",
        value=f"{float(st.session_state.time_input):.2f}",
        key="time_widget",
        help="No dataset original, 'Time' representa segundos desde a primeira transação registrada."
    )
    st.caption("Use ponto ou vírgula como separador decimal. Exemplo: 406.00 ou 406,00")

with col2:
    amount_raw = st.text_input(
        "Valor da transação",
        value=f"{float(st.session_state.amount_input):.2f}",
        key="amount_widget"
    )
    st.caption("Use ponto ou vírgula como separador decimal. Exemplo: 149.62 ou 149,62")

time_input = parse_float(time_raw, default=None)
amount_input = parse_float(amount_raw, default=None)

if time_input is None:
    st.error("Digite um valor válido para Time. Exemplo: 406.00 ou 406,00")
    time_input = 0.0

if amount_input is None:
    st.error("Digite um valor válido para Amount. Exemplo: 149.62 ou 149,62")
    amount_input = 0.0


# =========================
# Variáveis do modelo
# =========================
variables = get_default_variables()

if advanced_mode:
    with st.expander("⚙️ Configuração avançada das variáveis do modelo", expanded=True):
        col_a, col_b, col_c = st.columns(3)

        with col_a:
            for i in range(1, 11):
                variables[f"V{i}"] = st.number_input(
                    f"V{i}",
                    value=float(st.session_state[f"v_{i}"]),
                    key=f"v_{i}"
                )

        with col_b:
            for i in range(11, 21):
                variables[f"V{i}"] = st.number_input(
                    f"V{i}",
                    value=float(st.session_state[f"v_{i}"]),
                    key=f"v_{i}"
                )

        with col_c:
            for i in range(21, 29):
                variables[f"V{i}"] = st.number_input(
                    f"V{i}",
                    value=float(st.session_state[f"v_{i}"]),
                    key=f"v_{i}"
                )
else:
    with st.expander("🔍 Como o modo simplificado funciona"):
        st.markdown("""
No modo simplificado, o dashboard envia apenas os campos principais preenchidos por você:

- `Time`
- `Amount`

As variáveis `V1` a `V28` são preenchidas automaticamente com valores padrão (`0.0`) apenas para permitir a execução do modelo.

Em um sistema real, essas features seriam geradas automaticamente pelo pipeline de dados.
""")


transaction_data = build_transaction_data(
    time_input=time_input,
    amount_input=amount_input,
    variables=variables
)


# =========================
# Botão de predição
# =========================
st.divider()

col_btn1, col_btn2 = st.columns([1, 3])

with col_btn1:
    predict_clicked = st.button("🔍 Predict Fraud", use_container_width=True)

with col_btn2:
    st.caption("Preencha os campos principais e execute a inferência via API.")


# =========================
# Chamada da API
# =========================
if predict_clicked:
    try:
        response = requests.post(
            API_URL,
            json=transaction_data,
            timeout=10
        )

        if response.status_code == 200:
            result = response.json()

            fraud_probability = float(result["fraud_probability"])
            prediction = int(result["prediction"])

            st.subheader("📊 Resultado da predição")

            result_col1, result_col2 = st.columns(2)

            with result_col1:
                st.metric(
                    label="Probabilidade de fraude",
                    value=f"{fraud_probability:.4f}"
                )

            with result_col2:
                label = "FRAUDE" if prediction == 1 else "NORMAL"
                st.metric("Classificação do modelo", label)

            st.write("Faixa interpretativa de risco")
            st.progress(min(max(fraud_probability, 0.0), 1.0))

            chart_data = pd.DataFrame({
                "Classe": ["Normal", "Fraude"],
                "Probabilidade": [1 - fraud_probability, fraud_probability]
            })

            st.bar_chart(chart_data.set_index("Classe"))

            if fraud_probability >= 0.70:
                st.error("Risco alto: a transação apresenta forte sinal de fraude.")
            elif fraud_probability >= 0.30:
                st.warning("Risco moderado: a transação merece revisão adicional.")
            else:
                st.success("Risco baixo: a transação apresenta comportamento mais próximo do normal.")

            with st.expander("🔎 Ver resposta bruta da API"):
                st.json(result)

            with st.expander("📦 Ver payload enviado para a API"):
                st.json(transaction_data)

        else:
            st.error(f"Erro na API: {response.status_code} - {response.text}")

    except requests.exceptions.ConnectionError:
        st.error("Não foi possível conectar à API. Verifique se o FastAPI está rodando.")
    except requests.exceptions.Timeout:
        st.error("A API demorou para responder. Tente novamente.")
    except Exception as e:
        st.error(f"Erro inesperado: {e}")


# =========================
# Rodapé
# =========================
st.divider()
st.caption("Projeto de portfólio em Machine Learning Engineering • Desenvolvido por Luciana Narente")