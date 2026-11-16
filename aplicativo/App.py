import streamlit as st
import pandas as pd

st.title("Felix")

renda = st.number_input("Renda Mensal (R$)", min_value=0.0)

st.subheader("Seus gastos mensains")
st.caption("Clique na ultima linha para adicionar um gasto. Selecione uma linha e aperte Delete para remover.")

tabela_inicial = pd.DataFrame({
    "Gasto": ["Faculdade", "Cartão", "Lazer"],
    "Valor (R$)": [633.0, 600.0, 100.0],
})

gastos_df = st.data_editor(
    tabela_inicial,
    num_rows="dynamic",
    column_config={
        "Valor (R$)": st.column_config.NumberColumn(min_value=0.0, format="R$ %.2f"),
    },
)

total_gastos = gastos_df["Valor (R$)"].fillna(0).sum()
st.write(f"**Total de gastos:** R$ {total_gastos:,.2f}")


if st.button("Analisar"):
    sobra = renda - total_gastos
    reserva_ideal = total_gastos * 6
    st.metric("Sobra mensal", f"R$ {sobra:,.2f}")
    st.metric("Reserva de emergência ideal", f"R$ {reserva_ideal:,.2f}")
    if sobra <= 0:
        st.warning("Seus gastos superam a renda. Vamos revisar o orçamento primeiro.")