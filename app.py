import streamlit as st
import pandas as pd
from PIL import Image
import subprocess
import os
import base64
import pickle

# Molecular descriptor calculator
def desc_calc():
    # Performs the descriptor calculation
    bashCommand = "java -Xms2G -Xmx2G -Djava.awt.headless=true -jar ./PaDEL-Descriptor/PaDEL-Descriptor.jar -removesalt -standardizenitro -fingerprints -descriptortypes ./PaDEL-Descriptor/PubchemFingerprinter.xml -dir ./ -file descriptors_output.csv"
    process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    output, error = process.communicate()
    os.remove('molecule.smi')

# File download
def filedownload(df):
    csv = df.to_csv(index=False)
    b64 = base64.b64encode(csv.encode()).decode()  # strings <-> bytes conversions
    href = f'<a href="data:file/csv;base64,{b64}" download="prediction.csv">Download Predictions</a>'
    return href

# Model building
def build_model(input_data):
    # Reads in saved regression model
    load_model = pickle.load(open('covid_organism_353_model.pkl', 'rb'))
    # Apply model to make predictions
    prediction = load_model.predict(input_data)
    st.header('**预测值**')
    prediction_output = pd.Series(prediction, name='pIC50')
    molecule_name = pd.Series(load_data[1], name='molecule_name')
    df = pd.concat([molecule_name, prediction_output], axis=1)
    st.write(df)
    st.markdown(filedownload(df), unsafe_allow_html=True)

# Logo image
image = Image.open('logo.png')

st.image(image, use_column_width=True)

# Page title
st.markdown("""
# 基于机器学习模型的新冠小分子抑制剂活性预测

- This application is designed to predict the bioactivity of molecules inhibiting the COVID-19 virus, not a single protein. Out of the initial 10,086 small molecule data points downloaded from the Chembl database, only 657 had readily available IC50 values. To enhance the reliability of the model, IC50 values between 1,000 and 10,000 nanomolar were excluded due to concerns about the accuracy and reproducibility of the biology assay. This filtering process resulted in a refined dataset of 353 data points, which were used to build a random forest prediction model correlating molecular descriptors with IC50 values.
- 该应用程序旨在预测抑制COVID-19病毒的分子的生物活性。从Chembl数据库中下载了10,086个小分子数据点，其中只有657个具有可用的IC50值。为了提高模型的可靠性，排除了1,000至10,000纳摩尔之间的IC50值，原因是对生物学测定的准确性和重复性存在疑虑。这一筛选过程导致了353个数据点的精选数据集，用于构建分子描述符和IC50值之间的随机森林预测模型。

**Credits**
- Built and deployed by [Quantao Sun](https://github.com/quantaosun)
- Model training details see [Github repo](https://github.com/quantaosun/QSAR-COVID-19-App)
- App framework from `Python` + `Streamlit` by [Chanin Nantasenamat](https://medium.com/@chanin.nantasenamat))
- Descriptor calculated using [PaDEL-Descriptor](http://www.yapcwsoft.com/dd/padeldescriptor/) [[Read the Paper]](https://doi.org/10.1002/jcc.21707).
---
""")

# Sidebar
with st.sidebar.header('上传待预测小分子结构'):
    uploaded_file = st.sidebar.file_uploader("Upload your input file", type=['txt'])
    st.sidebar.markdown("""
[Example input file](https://raw.githubusercontent.com/quantaosun/QSAR-COVID-19-App/main/example_covid19.txt)
""")

if st.sidebar.button('预测'):
    load_data = pd.read_table(uploaded_file, sep=' ', header=None)
    load_data.to_csv('molecule.smi', sep = '\t', header = False, index = False)

    st.header('**上传的原始文件**')
    st.write(load_data)

    with st.spinner("分子描述符计算中..."):
        desc_calc()

    # Read in calculated descriptors and display the dataframe
    st.header('**完整分子描述符**')
    desc = pd.read_csv('descriptors_output.csv')
    st.write(desc)
    st.write(desc.shape)

    # Read descriptor list used in previously built model
    st.header('**部分核心分子描述符**')
    Xlist = list(pd.read_csv('descriptor_list.csv').columns)
    desc_subset = desc[Xlist]
    st.write(desc_subset)
    st.write(desc_subset.shape)

    # Apply trained model to make prediction on query compounds
    build_model(desc_subset)
else:
    st.info('请在左侧上传未知小分子SMILES开始预测,上传的格式应为txt格式，其中的SMILES应当为每行一个分子，只有smiles不要包含任何其他如名称等无关要素!')

    # Logo image
image = Image.open('regression.png')
st.header('Model built by training set ')
st.image(image, use_column_width=True)
