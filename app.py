import streamlit as st
from datetime import date

st.title("Calculadora de dias entre datas 📅")

st.write("Selecione as datas para calcular a diferença em dias.")

# Inputs de data
data_inicial = st.date_input(
    "Data inicial",
    value=date.today()
)

data_final = st.date_input(
    "Data final",
    value=date.today()
)

# Botão
if st.button("Calcular"):
    if data_final < data_inicial:
        st.error("A data final deve ser igual ou posterior à data inicial.")
    else:
        diferenca = (data_final - data_inicial).days

        st.subheader("Resultado")
        st.write(f"Diferença entre as datas: **{diferenca} dias**")
