from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.responses import StreamingResponse
import numpy as np
from PIL import Image
import io

from app.kernels import KERNELS
from app.convolution import apply_convolution

app = FastAPI(title="Image Kernel Convolution API")


@app.get("/kernels/list")
def list_kernels():
    return {"kernels": list(KERNELS.keys())}


@app.post("/transform/convolution")
async def transform_image(
    image: UploadFile = File(...),
    kernel_name: str = "blur"
):
    if kernel_name not in KERNELS:
        raise HTTPException(status_code=400, detail="Invalid kernel name")

    # Read and convert image to grayscale
    img = Image.open(image.file).convert("L")
    img_array = np.array(img)

    kernel = KERNELS[kernel_name]
    result = apply_convolution(img_array, kernel)

    # Convert back to image
    output_img = Image.fromarray(result)
    buffer = io.BytesIO()
    output_img.save(buffer, format="PNG")
    buffer.seek(0)

    return StreamingResponse(buffer, media_type="image/png")
