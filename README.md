# Image Kernel Convolution Engine

An image processing application that demonstrates how classical convolution kernels work on images.
The project uses a FastAPI backend to apply convolution operations and a Streamlit UI to visually demonstrate the transformations.

This project focuses on backend logic, mathematical understanding of convolution, and clean API design.

---

## Features

- Upload images (PNG / JPG / JPEG)
- Apply classical convolution kernels:
  - Blur
  - Edge Detection
  - Sharpen
  - Emboss
- Backend implemented using FastAPI
- Image processing logic written from scratch using NumPy
- Interactive Streamlit-based user interface
- Clear visualization of original and transformed images

---

## Project Structure

image-kernel-convolution/
│
├── app/
│   ├── main.py
│   ├── convolution.py
│   ├── kernels.py
│   ├── models.py
│   └── __init__.py
│
├── ui/
│   └── streamlit_app.py
│
├── screenshots/
│
├── requirements.txt
└── README.md

---

## Tech Stack

- Python
- FastAPI
- Uvicorn
- NumPy
- Pillow (PIL)
- Streamlit

---

## Installation and Setup

Clone the repository:

git clone https://github.com/your-username/image-kernel-convolution.git  
cd image-kernel-convolution

Install dependencies:

pip install -r requirements.txt

---

## Running the Backend (FastAPI)

uvicorn app.main:app --reload

Backend URL:  
http://127.0.0.1:8000

API Documentation:  
http://127.0.0.1:8000/docs

---

## Running the Frontend (Streamlit)

streamlit run ui/streamlit_app.py

UI URL:  
http://localhost:8501

---

## How It Works

1. The user uploads an image through the Streamlit interface.
2. The image is converted to grayscale.
3. A selected convolution kernel is applied using NumPy.
4. The convolution is implemented from scratch without using OpenCV.
5. The transformed image is returned and displayed.

Zero padding is used to handle image borders.

---

## Screenshots

Screenshots of:
- Application interface
- Edge detection output
- Blur output

are available in the screenshots folder.

---

## Assessment Context

This project was developed as part of the Sparkable Digital Solutions Round 3 Backend Technical Assessment.

Focus areas:
- Backend development
- Algorithmic understanding
- API design
- Code clarity
- Ability to explain technical concepts

---

## Author

Kirlampalli Siva Sankar  
Backend + AI Intern Applicant  
India

---

## Notes

- Convolution logic is implemented manually using NumPy.
- No OpenCV or high-level image processing libraries are used.
- AI tools were used only for clarification and debugging.

