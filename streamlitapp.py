import streamlit as st
from PIL import Image
import os
import subprocess

# streamlit run app.py
st.set_option("deprecation.showfileUploaderEncoding", False)

st.title("MRI to CT Translation (AIPI540 Final Project)")
st.write("")

file_up = st.file_uploader("Upload an image", type="jpg")

subprocess.call(["main.sh"])

if file_up is not None:
    with open(os.path.join("datasets/testingRuns/testA",file_up.name),"wb") as f:
        f.write(file_up.getbuffer())
    subprocess.call(['sh', './main.sh'])
    image = Image.open(file_up)
    st.image(image, caption="Uploaded MRI Image", use_column_width=True)
    st.write("")
    st.write("Just a second...")
    name_ext = file_up.name + "_fake"
    st.write(name_ext)
    st.image('results/checkpoints/testingRuns/test_latest/images/mri1440_fake.png', caption="Fake CT Image", use_column_width=True)
