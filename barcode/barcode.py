import os
from tkinter import Tk
from tkinter.filedialog import askopenfilename
from PIL import Image
from PIL import ImageEnhance
import zbar

# Crea la ventana de diálogo de selección de archivo
root = Tk()
root.withdraw()

# Solicita al usuario que seleccione una imagen
file_path = askopenfilename()

# Carga la imagen seleccionada utilizando la biblioteca Pillow
image = Image.open(file_path)

# Mejora el contraste y la nitidez de la imagen para mejorar la detección de códigos de barras
enhancer = ImageEnhance.Contrast(image)
image = enhancer.enhance(2)
enhancer = ImageEnhance.Sharpness(image)
image = enhancer.enhance(2)

# Crea un objeto de decodificador de código de barras utilizando la biblioteca zbar
scanner = zbar.Scanner()

# Convierte la imagen a escala de grises y la escanea para buscar códigos de barras
gray_image = image.convert('L')
barcodes = scanner.scan(gray_image)

# Imprime los datos de los códigos de barras encontrados
for barcode in barcodes:
    print(barcode.data.decode('utf-8'))

