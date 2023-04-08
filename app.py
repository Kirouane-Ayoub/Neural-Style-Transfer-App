from NeuralStyleTransfer import NST
import streamlit as st
import numpy as np 
import time
NST = NST()

st.set_page_config(
    page_title="Neural Style Transfer App",
    layout="wide",
    initial_sidebar_state="expanded")

with st.sidebar : 
    st.image("icon.png" , width=190)
    results_save = st.radio("Do you want to save Results ?" , ("Yes" , "No"))

tab0 , tab1 = st.tabs(["Home" , "Style Transfer"])
with tab0 : 
    st.header("About This Project : ")
    st.image("Home.jpeg")
    st.write("""Neural Style Transfer App is an innovative technology that allows users to transform their photos into unique artistic creations.
        Using deep neural networks, this app can apply the style of one image to the content of another,
        resulting in a beautiful fusion of two distinct visual styles. Whether you want to turn a family photo into a work of art or 
        experiment with different styles to create a stunning piece of digital art, Neural Style Transfer App makes it easy and fun.""")
with tab1 : 
    col1 , col2 = st.columns(2)

    with col1 : 
        content = st.file_uploader("Uploade Your Contant image : " , type=["png" ,"jpg" , "jpeg"])
        if content : 
            contant_img_name = content.name
    with col2 : 
        style = st.file_uploader("Uploade Your Style image : " , type=["png" ,"jpg" , "jpeg"])
        if style : 
            style_img_name = style.name

    _ , c1 , c2 , c3 , c4= st.columns(5)
    with st.spinner('Wait for it...'):
        with c2 : 
            start = st.button("Click To start")

        if start : 
            try : 
                stylized_image = NST.transfer(contant_img_name , style_img_name)
                st.image(np.squeeze(stylized_image))
            except : 
                pass
            if results_save : 
                NST.save_img(stylized_image=stylized_image , save_name=str(time.asctime()))
            st.success('Done!', icon="✅")

