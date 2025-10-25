# Project: Image Dimensionality Reduction

## Description

This project implements a manual process of **dimensionality reduction** in digital images.
The goal is to transform a color image (RGB) into two simplified representations:

1. **Grayscale (0–255)** – representing light intensity.
2. **Binarized (0 and 255)** – black-and-white output.

The process is carried out **without using any built-in image processing functions**, relying only on the **Pillow (PIL)** library for image loading and creation.

---

## Process Steps

### 1. Image Loading

The image is read using the **Pillow** library, converted to RGB mode, and its dimensions are obtained for manual pixel iteration.

```python
image = Image.open(image_path).convert("RGB")
```

---

### 2. Grayscale Conversion

Each pixel is processed individually using the standard perceptual luminance formula:

[
\text{Gray} = 0.299R + 0.587G + 0.114B
]

The resulting value is stored in a new image created in **“L” (luminance)** mode.

```python
gray_val = int(0.299 * r + 0.587 * g + 0.114 * b)
gray.putpixel((x, y), gray_val)
```

---

### 3. Binarization

The grayscale image is scanned again.
A **threshold** value is defined, and each pixel is classified as:

* **255 (white)** if greater than the threshold, or
* **0 (black)** otherwise.

The new image is created in **“1” (binary)** mode.

```python
bw.putpixel((x, y), 255 if gray_val > threshold else 0)
```

---

## Full Code

```python
from PIL import Image

def to_grayscale(image_path):
    image = Image.open(image_path).convert("RGB")
    gray = Image.new("L", image.size)
    w, h = image.size
    
    for x in range(w):
        for y in range(h):
            r, g, b = image.getpixel((x, y))
            gray_val = int(0.299 * r + 0.587 * g + 0.114 * b)
            gray.putpixel((x, y), gray_val)
    
    return gray

def binarize_image(gray_image, threshold=128):
    bw = Image.new("1", gray_image.size)
    w, h = gray_image.size
    
    for x in range(w):
        for y in range(h):
            gray_val = gray_image.getpixel((x, y))
            bw.putpixel((x, y), 255 if gray_val > threshold else 0)
    
    return bw

image_path = 'path/to/image.jpg'

gray_img = to_grayscale(image_path)
gray_img.show()

bw_img = binarize_image(gray_img, threshold=128)
bw_img.show()
```

---

## Key Concepts

| Concept                      | Description                                                                           |
| ---------------------------- | ------------------------------------------------------------------------------------- |
| **Dimensionality Reduction** | Removes redundant color components, reducing 3 color channels (RGB) to 1 (luminance). |
| **Grayscale Conversion**     | Represents pixel light intensity from 0 (black) to 255 (white).                       |
| **Binarization**             | Segments the image into two regions based on a fixed threshold.                       |

---

## Dependencies

Install the required library:

```bash
pip install pillow
```

---

## Expected Results

After execution, the program will display three image versions:

1. **Original** – color RGB image.
2. **Grayscale** – simplified image with values ranging from 0 to 255.
3. **Binarized** – purely black-and-white image (0 and 255).

These representations demonstrate how **dimensionality reduction** retains structural information while simplifying visual data for further use in **neural networks** or **computer vision preprocessing**.

---

Examples:

original JPG:

<img width="516" height="412" alt="image" src="https://github.com/user-attachments/assets/4f938666-ddac-435a-8270-75d96892de96" />

Results:

<img width="1058" height="424" alt="image" src="https://github.com/user-attachments/assets/e3862c22-ed03-4de5-97b8-583928361be0" />



All pixel-level operations (computation, grayscale conversion, and binarization) are performed **manually**, without relying on any built-in functions from Pillow or OpenCV.
This manual approach serves a didactic purpose, allowing a clear understanding of how **dimensionality reduction** and **basic computer vision** techniques operate internally.
