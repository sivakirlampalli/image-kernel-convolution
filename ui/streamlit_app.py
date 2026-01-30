import streamlit as st
import requests
from PIL import Image
import io

st.set_page_config(page_title="Image Kernel Convolution", layout="centered")

logo = Image.open("ui/logo.png")

st.image(logo, width=80)
st.title("Image Kernel Convolution Engine")

st.write("Upload an image and apply different convolution kernels.")

uploaded_file = st.file_uploader(
    "Upload an image",
    type=["png", "jpg", "jpeg"]
)

kernel = st.selectbox(
    "Choose a kernel",
    ["emboss", "blur", "sharpen", "edge"]
)

if uploaded_file is not None:
    st.image(uploaded_file, caption="Original Image",  use_container_width=True)

    if st.button("Apply Convolution"):
        files = {"image": uploaded_file}
        params = {"kernel_name": kernel}

        try:
            response = requests.post(
                "http://127.0.0.1:8000/transform/convolution",
                files=files,
                params=params,
                timeout=30
            )

            if response.status_code == 200:
                output_image = Image.open(io.BytesIO(response.content))
                st.image(output_image, caption="Transformed Image", use_column_width=True)
            else:
                st.error("Error processing image")

        except Exception as e:
            st.error(f"Failed to connect to backend: {e}")
