# -*- coding: utf-8 -*-
"""
Created on Tue Mar  3 16:13:25 2026

@author: Administrator
"""

import streamlit as st
from scanner import scan
from ml_model import train_model

st.title("🚀 AI Trading System")

if st.button("Run Scanner"):
    results = scan()
    st.write(results[:5])

if st.button("Train ML Model"):
    model, acc = train_model()
    st.write("Model Accuracy:", acc)