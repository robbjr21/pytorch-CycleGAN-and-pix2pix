import streamlit as st
from PIL import Image
# streamlit run app.py
st.set_option("deprecation.showfileUploaderEncoding", False)

st.title("MRI to CT Translation (AIPI540 Final Project)")
st.write("")

file_up = st.file_uploader("Upload an image", type="jpg")


#import subprocess
#subprocess.call(["main.sh"])

if file_up is not None:
    image = Image.open(file_up)
    st.image(image, caption="Uploaded MRI Image", use_column_width=True)
    st.write("")
    st.write("Just a second...")
    st.image(results/checkpoints/testingRuns/test_latest/images/mri1440_fake.png, caption="Fake CT Image", use_column_width=True)
