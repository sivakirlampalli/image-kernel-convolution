import numpy as np

def apply_convolution(image_array: np.ndarray, kernel: np.ndarray) -> np.ndarray:
    """
    Apply convolution to a grayscale image using NumPy.
    Implements convolution from scratch (no OpenCV).
    """

    image_height, image_width = image_array.shape
    kernel_height, kernel_width = kernel.shape

    pad_h = kernel_height // 2
    pad_w = kernel_width // 2

    # Zero padding the image
    padded_image = np.pad(
        image_array,
        ((pad_h, pad_h), (pad_w, pad_w)),
        mode="constant",
        constant_values=0
    )

    output = np.zeros((image_height, image_width))

    for i in range(image_height):
        for j in range(image_width):
            region = padded_image[i:i + kernel_height, j:j + kernel_width]
            output[i, j] = np.sum(region * kernel)

    # Normalize values to valid image range
    output = np.clip(output, 0, 255)

    return output.astype(np.uint8)
