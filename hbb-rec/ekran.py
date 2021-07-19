#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import numpy as np
import streamlit as st
import pickle
import requests
import io

cola,colb,colc = st.beta_columns(3)
colb.image('./hblogo.jfif')


items = ["Dereotu","Limon Lamas 500 gr","Şeftali Paket 500 gr","Çilek 250 gr","Dr.Oetker Şekerli Vanilin 15'li 75 gr","Dana Antrikot 250 gr","Dana Biftek 250 gr","Nane","Pepsi Cola Pet 1.5 L","Lipton Demlik Poşet Çay Doğu Karadeniz 100'Lü"]
col1, col2, col3 = st.beta_columns(3)
text = col1.selectbox("Ürün Seçiniz(Örnek 10 ürün listelenmiştir)", items)
if text!="":
    url="http://127.0.0.1:8000/predict/"+text
    response=requests.get(url).content

#text=st.sidebar.text_input("item")
#if text!="":
    #url="http://127.0.0.1:8000/predict/"+text
    #response=requests.get(url).content
    
    #dff=pd.read_csv(io.StringIO(response.decode('utf-8'))).T

    st.write(response.decode('utf-8'))
    
    
    #df=pd.DataFrame(response.content)
    
    #st.dataframe(dff.style.highlight_max(axis=0))