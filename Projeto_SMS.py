#!/usr/bin/env python
# coding: utf-8

# # Projeto Hashtag
# ## Multiplas bases de dados e envio de mensagem SMS
# #### O projeto consiste em análise de mútiplas bases de dados para localizar uam informação e encaminhar por meio de uma mensagem SMS  

# In[ ]:


# Passo a Passo
# 1. Importar (abrir) seis bases de dados; Abrir 6 arquivos em Excel
# 2. Encontrar o valor determinado; 
# para cada arquivo verificar algum valor na coluna valor é > 55k.
# 3. Imprimir mensagem; 4. Enviar mensagem; 


# In[ ]:


import pandas as pd 


# In[ ]:


get_ipython().system('pip3 install openpyxl')


# In[ ]:


get_ipython().system('pip3 install twilio')
# Url —> https://www.twilio.com/docs/libraries/python


# In[ ]:


lista_meses =  ['janeiro', 'fevereiro', 'março', 'maio', 'junho']
for mes in lista_meses: 
    print(mes)
    tabela_vendas = pd.read_excel(f'{mes}.xlsx')
    print(tabela_vendas)


# In[ ]:


for mes in lista_meses: 
    print(mes)
    tabela_vendas = pd.read_excel(f'{mes}.xlsx')
    print(tabela_vendas)
    if (tabela_vendas['Vendas'] > 55000).any():
        print('Encontrou alguém com mais de 55.000')


# In[ ]:


for mes in lista_meses: 
   
    tabela_vendas = pd.read_excel(f'{mes}.xlsx')
    
    if (tabela_vendas['Vendas'] > 55000).any():
        print(f'No mês {mes} Encontrou alguém com mais de 55.000')


# In[67]:


# Quem e quando ?
for mes in lista_meses: 
    tabela_vendas = pd.read_excel(f'{mes}.xlsx')
    if (tabela_vendas['Vendas'] > 55000).any():
        vendedor  = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendedor'].values[0] 
        vendas = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000,'Vendas'].values[0] 
        print(f'No mês de {mes} a meta foi atingida!.Vendedor/a: {vendedor} com {vendas}')


# In[79]:


for mes in lista_meses: 
    tabela_vendas = pd.read_excel(f'{mes}.xlsx')
    if (tabela_vendas['Vendas'] > 55000).any():
        vendedor  = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendedor'].values[0] 
        vendas = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000,'Vendas'].values[0] 
        print(f'No mês de {mes} a meta foi atingida!.Vendedor/a: {vendedor} com {vendas}')
        from twilio.rest import Client
        account_sid= "ACdea1e4e49e6e0f2454f21bfacb3e93e0"
        auth_token= "af817a3abf8fb73008af1effa2f84d37"
        client = Client(account_sid, auth_token)
        message = client.messages.create(
            to="+55 11 981295915",  
            from_="+19198879201",
            body= f'No mês de {mes} a meta foi atingida!.Vendedor/a: {vendedor} com {vendas}')
        print(message.sid)


# In[ ]:




