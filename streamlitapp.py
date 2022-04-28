import streamlit as st
from PIL import Image
import os
import subprocess

# streamlit run app.py
st.set_option("deprecation.showfileUploaderEncoding", False)

st.title("MRI to CT Translation (AIPI540 Final Project)")
st.write("")

file_up = st.file_uploader("Upload an image", type="jpg")

if file_up is not None:
    with open(os.path.join("datasets/testingRuns/testA",file_up.name),"wb") as f:
        f.write(file_up.getbuffer())
    #subprocess.popen('main.sh', shell = True)
    subprocess.run("bash main.sh", shell = True)
    image = Image.open(file_up)
    st.image(image, caption="Uploaded MRI Image", use_column_width=True)
    st.write("")
    st.write("Just a second...")
    name_ext = file_up.name
    name_ext = name_ext.split(".")[0]
    name_ext = name_ext + "_fake.png"
    st.write(name_ext)
    st.image('results/checkpoints/testingRuns/test_latest/images/{}'.format(name_ext), caption="Fake CT Image", use_column_width=True)
