# Sistemas de vendas
# Seção Cadastras Vendas
    # Campo Data
    # Campo Vendedor - Ana, Bruno, Carla
    # Campo Poduto - Notebook, Fone, Celular
    # Campo Quantidade
    # Campo Valor
    # Campo Cadastrar Venda
        # Quando eu clicar no botão -> adicionar a venda na tabela
# Seção de vendas Cadastradas
    # Tabela com as Vendas
# Seção Dashboard
    # Card/Métrica -> Faturamento Total
    # Gráfico de Barra/Coluna -> Venda por vendedor
    # Gráfico de Pizza -> Venda por produto

import streamlit as st
import pandas as pd
import plotly.express as px

# Carregar a base de vendas
tabela_vendas = pd.read_csv("vendas.csv")

st.write("# Sistema de Vendas")

#* Seção de cadastro de vendas
st.sidebar.write("## Cadastro de Vendas")

data = st.sidebar.date_input("Data")
vendedor = st.sidebar.selectbox("Vendedor", ["Ana", "Bruno", "Carla"])
produto = st.sidebar.selectbox("Produto", ["Notebook", "Fone", "Celular"])
quantidade = st.sidebar.number_input("Quantidade", min_value=1, step=1)
valor = st.sidebar.number_input("Valor da Venda", min_value=0.0, step=0.01)
botao_cadastrar = st.sidebar.button("Cadastrar Venda")

# logica de cadastro
if botao_cadastrar:
        nova_venda = [str(data), vendedor, produto, quantidade, valor]
        ultima_linha = len(tabela_vendas)
        tabela_vendas.loc[ultima_linha] = nova_venda
        tabela_vendas.to_csv("vendas.csv", index=False)
        st.success("Venda cadastrada com sucesso!")

#* Seção de vizualizar as vendas
st.write("## Vendas Cadastradas")
st.dataframe(tabela_vendas)

#* Seção de Dashboard
st.write("## Dashboard")

# Card/Métrica -> Faturamento Total
faturamento_total = tabela_vendas["valor"].sum()
st.metric("Faturamento Total", f"R$ {faturamento_total:,.2f}")

# Gráfico de Barra/Coluna -> Venda por vendedor
grafico1 = px.bar(tabela_vendas, x="vendedor", y="valor", color="produto", title="Venda por Vendedor")
st.plotly_chart(grafico1)

# Gráfico de Pizza -> Venda por produto
grafico2 = px.pie(tabela_vendas, names="produto", values="valor", hole=0.5, title="Venda por Produto")
st.plotly_chart(grafico2)
