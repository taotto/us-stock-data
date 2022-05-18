import matplotlib.pyplot as plt
#from matplotlib.axis import Ticker
import streamlit as st 
import requests 
import simfin as sf
import pandas as pd
import numpy as np
from simfin.names import *

st.set_page_config(layout="wide")

sf.set_data_dir('~/simfin_data/')

sf.set_api_key(api_key="enter API key")

symbol = st.sidebar.text_input ("Symbol", value = "MSFT")

screen = st.sidebar.selectbox ("View", ("Company info", "Income statement", "Balance sheet", "Cash flow statement"))

#st.title(symbol + ' ' + screen)

#if screen == "Company info":
  #col1, col2, col3 = st.columns([3,4,3])
  #with col2:
    #st.title(symbol + ' ' + screen)

  #col1, col2 = st.columns ([1,2])
  #with col1:

    #df_company = sf.load_companies(market='us', index= ['Ticker'])

    #df_shareprices = sf.load_shareprices(variant='daily', market='us', index= ['Ticker', DATE])

    #st.markdown("<h2 style='text-align: center;color: #31333F;'>Info</h1>", unsafe_allow_html=True)

    #st.subheader ('Company name')
    #df_company.loc [symbol] [COMPANY_NAME]

    #df_price_ratios = sf.load_derived_shareprices(variant='daily', market='us', index= ['Ticker', DATE])

    #st.subheader ('Market-Cap')
    #df_banaan = df_price_ratios.loc [symbol] [MCAP] 
    #df_banaan.loc ['2022-03-14']

    #st.subheader ('P/E Ratio')
    #df_pe_today = df_price_ratios.loc [symbol] [PE_QUARTERLY]
    #df_pe_today.loc ['2022-03-14']


  #with col2:

    #df_shareprices = df_shareprices.loc [symbol]

    #st.markdown("<h2 style='text-align: center;color: #31333F;'>Share price</h2>", unsafe_allow_html=True)

   # st.line_chart(df_shareprices [SHARE_PRICE_CLOSE])


  #st.markdown("<h1 style='text-align: center; color: red;'>Some title</h1>", unsafe_allow_html=True)

if screen == "Income statement":
  col1, col2, col3 = st.columns([3,4,3])
  with col2:
    st.title(symbol + ' ' + screen)
  df_income = sf.load_income(variant='annual', market='us', index=['Ticker', FISCAL_YEAR])
  df_income2 = df_income.loc [symbol][[REVENUE, COST_REVENUE, GROSS_PROFIT, OPERATING_EXPENSES, SELLING_GEN_ADMIN
,RESEARCH_DEV
,DEPR_AMOR, OP_INCOME
,NON_OP_INCOME
,INTEREST_EXP_NET
, PRETAX_INCOME_LOSS_ADJ
,ABNORM_GAIN_LOSS,PRETAX_INCOME_LOSS, 
INCOME_TAX,INCOME_CONT_OP, NET_EXTR_GAIN_LOSS
, NET_INCOME]]

  df_tr_income = df_income2.transpose()

  df_income_done = df_tr_income[df_tr_income.columns[::-1]]

  df_income_done

  col1, col2, col3 = st.columns([3,2,7])

  with col1:
    st.markdown("<h2 style='text-align: center;color: #31333F;'>Select</h1>", unsafe_allow_html=True)

    select = st.multiselect ( 'Type something', ['Revenue', 'Gross profit', 'Net income'], ['Revenue'])

  with col2:
    pass


  with col3:
    if select == ['Revenue']:
      st.markdown("<h2 style='text-align: center;color: #31333F;'>Revenue</h1>", unsafe_allow_html=True)
      st.bar_chart(df_income_done.loc [REVENUE])

    if select == ['Gross profit']:
      st.markdown("<h2 style='text-align: center;color: #31333F;'>Gross profit</h1>", unsafe_allow_html=True)
      st.bar_chart(df_income_done.loc [GROSS_PROFIT])

    if select == ['Net income']:
      st.markdown("<h2 style='text-align: center;color: #31333F;'>Net income</h1>", unsafe_allow_html=True)
      st.bar_chart(df_income_done.loc [NET_INCOME])

    if select == ['Revenue', 'Net income']:
      st.markdown("<h2 style='text-align: center;color: #31333F;'>Revenue</h1>", unsafe_allow_html=True)
      st.bar_chart(df_income_done.loc [REVENUE])
      st.markdown("<h2 style='text-align: center;color: #31333F;'>Net income</h1>", unsafe_allow_html=True)
      st.bar_chart(df_income_done.loc [NET_INCOME])



if screen == "Balance sheet":
  col1, col2, col3 = st.columns([3,4,3])
  with col2:
    st.title(symbol + ' ' + screen)
  df_balance = sf.load_balance(variant='annual', market='us', index=['Ticker', 'Fiscal Year']) 
  df_balance = df_balance.loc [symbol] [[CASH_EQUIV_ST_INVEST
, ACC_NOTES_RECV,INVENTORIES, TOTAL_CUR_ASSETS
, PROP_PLANT_EQUIP_NET, LT_INVEST_RECV, OTHER_LT_ASSETS, TOTAL_NONCUR_ASSETS, TOTAL_ASSETS, PAYABLES_ACCRUALS
, ST_DEBT, TOTAL_CUR_LIAB
, LT_DEBT, TOTAL_NONCUR_LIAB, TOTAL_LIABILITIES, SHARE_CAPITAL_ADD, TREASURY_STOCK, RETAINED_EARNINGS, TOTAL_EQUITY, TOTAL_LIAB_EQUITY]]

  df_tr_balance = df_balance.transpose()

  df_tr_balance[df_tr_balance.columns[::-1]]

  col1, col2, col3 = st.columns([3,2,7])
  with col1:
    st.markdown("<h2 style='text-align: center;color: #31333F;'>Select</h1>", unsafe_allow_html=True)

    select_balance = st.selectbox ("Select", ("Total assets", "Total liabilities", "Shareholders equity"))

  with col2:
    pass


  with col3:
    if select_balance == 'Total assets':
      st.markdown("<h2 style='text-align: center;color: #31333F;'>Total assets</h1>", unsafe_allow_html=True)
      st.bar_chart(df_tr_balance.loc [TOTAL_ASSETS])

    if select_balance == 'Total liabilities':
      st.markdown("<h2 style='text-align: center;color: #31333F;'>Total liabilities</h1>", unsafe_allow_html=True)
      st.bar_chart(df_tr_balance.loc [TOTAL_LIABILITIES])

    if select_balance == 'Shareholders equity':
      st.markdown("<h2 style='text-align: center;color: #31333F;'>Shareholders equity</h1>", unsafe_allow_html=True)
      st.bar_chart(df_tr_balance.loc [TOTAL_EQUITY])




if screen == "Cash flow statement":
  col1, col2, col3 = st.columns([3,4,3])
  with col2:
    st.title(symbol + ' ' + screen)
  df_cashflow = sf.load_cashflow(variant='annual', market='us', index= [ 'Ticker', 'Fiscal Year'])
  df_cashflow = df_cashflow.loc [symbol] [[NET_INCOME_START, DEPR_AMOR, NON_CASH_ITEMS, CHG_WORKING_CAPITAL, CHG_ACCOUNTS_RECV, CHG_INVENTORIES, CHG_ACC_PAYABLE, CHG_OTHER, NET_CASH_OPS, CHG_FIX_ASSETS_INT, NET_CHG_LT_INVEST, NET_CASH_ACQ_DIVEST, NET_CASH_INV, DIVIDENDS_PAID, CASH_REPAY_DEBT, CASH_REPURCHASE_EQUITY, NET_CASH_FIN, NET_CHG_CASH]]

  df_tr_cashflow = df_cashflow.transpose ()

  df_tr_cashflow[df_tr_cashflow.columns[::-1]]

  col1, col2, col3 = st.columns([3,2,7])
  with col1:
    st.markdown("<h2 style='text-align: center;color: #31333F;'>Select</h1>", unsafe_allow_html=True)

    select_cashflow = st.selectbox ("Select", ("Net change in cash", "Net cash from operating activities", "Net income"))

  with col2:
    pass


  with col3:
    if select_cashflow == 'Net change in cash':
      st.markdown("<h2 style='text-align: center;color: #31333F;'>Net change in cash</h1>", unsafe_allow_html=True)
      st.bar_chart(df_tr_cashflow.loc [NET_CHG_CASH])

    if select_cashflow == 'Net cash from operating activities':
      st.markdown("<h2 style='text-align: center;color: #31333F;'>Net cash from operating activitiess</h1>", unsafe_allow_html=True)
      st.bar_chart(df_tr_cashflow.loc [NET_CASH_OPS])

    if select_cashflow == 'Net income':
      st.markdown("<h2 style='text-align: center;color: #31333F;'>Net income</h1>", unsafe_allow_html=True)
      st.bar_chart(df_tr_cashflow.loc [NET_INCOME_START])
