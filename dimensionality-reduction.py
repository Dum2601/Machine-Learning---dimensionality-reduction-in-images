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

image_path = '' # the path of your image file has to be in this variable

gray_img = to_grayscale(image_path)
gray_img.show() 

bw_img = binarize_image(gray_img, threshold=128)
bw_img.show()    
