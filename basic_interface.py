
# from PubmedArticle_s import article_spider as sp
import streamlit as st
from streamlit_option_menu import  option_menu
import os
import time
import pandas as pd
from io import StringIO

#定义网页标题
st.set_page_config(page_title='知识图谱补全系统',layout='wide')
#定义边栏导航
with st.sidebar:
    choose = option_menu('知识图谱补全系统',['系统功能介绍', '导入数据集','新增实体关系','三元组评分', '图谱补全', '图谱展示'],
                         icons=['home', '1-square', '2-square', '3-square', '4-square', '5-square'])
    
if choose == '系统功能介绍':
        # 定义页面标题
    st.title('知识图谱补全系统')
    # 写入文本
    st.write('该系统基于给定数据集进行知识图谱补全，功能如下：')
    st.write('1. 该系统允许上传训练集和支持集，用于补全模型的训练和预测')
    st.write('2. 该系统支持新增实体和三元组，用于更新知识图谱')
    st.write('3. 该系统支持为给定候选三元组评分，并给出对应的评分依据')
    st.write('4. 该系统支持对给定候选三元组进行补全，并给出对应的补全结果')
    st.write('5. 该系统支持展示训练集和支持集对应的图谱')
elif choose == '导入数据集':
    # 上传文件
    import streamlit as st

    uploaded_files = st.file_uploader("Choose a CSV file", accept_multiple_files=True)
    for uploaded_file in uploaded_files:
        bytes_data = uploaded_file.read()
        st.write("filename:", uploaded_file.name)
        st.write(bytes_data)