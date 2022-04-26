import streamlit as st
from PIL import Image
# streamlit run app.py
st.set_option("deprecation.showfileUploaderEncoding", False)

st.title("Language Detection from Document Image Demo (AIPI540 CV Module)")
st.write("")

file_up = st.file_uploader("Upload an image", type="jpg")


import subprocess
subprocess.call(["main.sh"])

if file_up is not None:
    image = Image.open(file_up)
    st.image(image, caption="Uploaded Image.", use_column_width=True)
    st.write("")
    st.write("Just a second...")
    labels = predict(file_up)
