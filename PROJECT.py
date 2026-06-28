# print("hell")
#from tkinter import Image

import streamlit as st
# from streamlit.navigation import page

# import streamlit as st
# st.title("My First Streamlit App")
# st.write("Hello World!")
# import streamlit as st
# st.title("Price prediction for devices")
# st.header("Header")
# st.subheader("Sub Header")
# st.text("Simple text")
# st.markdown("**Bold Text**")
# age = st.number_input(
#     "Enter your age",
#      min_value=1,
#      max_value=100)
# st.write("age",age)
# if st.button("Click me"):
#     st.success("button pressed!")
# st.sidebar.title("Menu")
# option = st.sidebar.selectbox(
#     "Select",
#      ["Home","About"]
# )
# from PIL import  Image
# st.set_page_config(
#     page_title="Image Upload Application",
#     page_icon="📷"
# )
# st.title("Image Upload Application")
# st.write("Upload one or more images")
# uploaded_files = st.file_uploader(
#     "Choose images",
#     type=["jpg", "jpeg", "png"],
#     accept_multiple_files=True
#
# )
# if uploaded_files:
#     st.success(
#     f"{len(uploaded_files)} images uploaded succesfully!"
# )
#     for file in uploaded_files:
#         image = Image.open(file)
#         st.image(
#             image,
#             caption=file.name,
#             use_container_width=True
#         )
#
# st.write(option)
# st.write("Filename:",file.name)
# st.write("Format:",image.format)
# st.write("Size:",image.size)
# st.write("---")

# import streamlit as st
# from PIL import Image
#
# st.set_page_config(
#     page_title="Image Upload App",
#     page_icon="📷"
# )
#
# st.title("📷 Image Upload Application")
#
# st.write("Upload one or more images")
#
# uploaded_files = st.file_uploader(
#     "Choose Images",
#     type=["jpg", "jpeg", "png"],
#     accept_multiple_files=True
# )
#
# if uploaded_files:
#
#     st.success(
#         f"{len(uploaded_files)} image(s) uploaded successfully!"
#     )
#
#     for file in uploaded_files:
#
#         image = Image.open(file)
#
#         st.image(
#             image,
#             caption=file.name,
#             use_container_width=True
#         )
#
#         st.write("Filename:", file.name)
#         st.write("Format:", image.format)
#         st.write("Size:", image.size)
#         st.write("---")
# About page
# This site has been created by a team known as The Tech Titans which in 2026 consists of two members Aaryan Garg and Saatvik Talwar
# from PIL import Image
# st.sidebar.title("Menu")
# option = st.sidebar.selectbox(
#     "Select",
#      ["Home","About"]
# )
# st.set_page_config(
#     page_title="About",
#     layout="wide",
# )
#
# if page == "Home":
#     st.title("Price prediction for devices")
#     col1,col2 = st.columns([1,2])
#     image = st.image("https://en.pimg.jp/108/489/578/1/108489578.jpg")
#     with col1:
#         st.image(
#             image,
#             caption="(Old Devices)",
#
#         )
#     with col2:
#         st.header("Price prediction for devices")
#         st.write("This project is only for prediction it may may or may not be to accurate")
#
# #About page
# elif page == "About":
#     st.title("About")
#
#     st.write("This site has been created by a team known as The Tech Titans which in 2026 consists of two members Aaryan Garg and Saatvik Talwar")


#import streamlit as st
# from PIL import Image
# import
#
# st.set_page_config(
#     page_title="About",
#     layout="wide",
# )
#
# # Sidebar Navigation
# page = st.sidebar.radio(
#     "Navigation",
#     ["Home", "About"]
# )
#
# if page == "Home":
#     st.title("Price Prediction for Devices")
#
#     col1, col2 = st.columns([1, 2])
#
#     with col1:
#         st.image(
#             "https://en.pimg.jp/108/489/578/1/108489578.jpg",
#             caption="Old Devices",
#             use_container_width=True
#         )
#
#     with col2:
#
#         st.write(
#             "This project is only for prediction. The results may or may not be completely accurate."
#         )
#     st.write("Upload one or more images")
#
#     uploaded_files = st.file_uploader(
#         "Choose Images",
#         type=["jpg", "jpeg", "png"],
#         accept_multiple_files=True
#     )
#
#     if uploaded_files:
#
#         st.success(
#             f"{len(uploaded_files)} image(s) uploaded successfully!"
#         )
#
#         for file in uploaded_files:
#             image = Image.open(file)
#
#             st.image(
#                 image,
#                 caption=file.name,
#                 use_container_width=True
#             )
#
#             st.write("Filename:", file.name)
#             st.write("Format:", image.format)
#             st.write("Size:", image.size)
#             st.write("---")
#
# About Page
# elif page == "About":
#     st.title("About")
#
#     st.write(
#         "This site has been created by a team known as The Tech Titans, "
#         "which in 2026 consists of two members: Aaryan Garg and Saatvik Talwar.")
#     st.header("Contact")
#     st.subheader("Saatvik Talwar")
#     st.write("Phone Number:8860080749")
#     st.write("Email Address: saatvik.techtitans@gmail.com")
#     st.subheader("Aaryan Garg")
#     st.write("Phone Number:9872977101")
#     st.write("Email Address: aaryan11077@gmail.com")
#     st.subheader("Common official Email Address✉️: thetechtitans@gmail.com")
#     st.write("Please feel free to give suggestions and issues with this app.")
#


import google.generativeai as genai

from PIL import Image

GEMINI_API_KEY = st.secrets["GEMINI_API_KEY"]
genai.configure(api_key=GEMINI_API_KEY)

model = genai.GenerativeModel("gemini-2.5-flash")

# streamlit UI

st.set_page_config(
    page_title="Generative AI",
    layout="centered"
)


st.title("An item price estimator")

st.write(
    "Upload an image and provide a description."
    "Gemini will analyze the item and estimate its market value"
)

uploaded_file = st.file_uploader(
    "Upload an image",
    type=["png", "jpg", "jpeg", "webp"]
)

description = st.text_area(
    "item description",
    placeholder="Exampple : Used Samsung Z fold 4 256GB, excellent condition"

)
if st.button("Estimate Price"):
    if uploaded_file is None:
        sṭ.warning("Please upload an image")
        st.stop()

    image = Image.open(uploaded_file)

    st.image(
        image,
        caption="Uploaded Item",
        use_container_width=True
    )
    prompt = f"""
   You are an expert of product valuation specialist.
   Analyze the uploaded image and the user's description

   user Description: 
   {description}
   Determine: 
   1.What the item appears to be.
   2.Its likely condition.
   3.Estimated price range in USD.
   4.Estimated price range in INR.
   5.Confidece score (0-100%).
   6.Key factors affecting the valuation.
   7.A short sumarry.

   Return the answer in clean markdown format.
   """
    try:
        with st.spinner("Annalyzing the item and estimating its market value..."):
            response = model.generate_content(
                [prompt, image]

            )
        st.subheader("Estimated Value")
        st.markdown(response.text)
    except Exception as e:
        st.error(f"Error: {e}")

