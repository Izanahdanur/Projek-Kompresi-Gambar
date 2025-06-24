from PIL import Image   # Library proses gambar
import time             # Mengukur waktu kompresi
import os               # Operasi file

def compress_image(input_path, output_path, quality_percent=50):    # Fungsi utama kompresi gambar
    start = time.time()
    with Image.open(input_path) as img: # Buka gambar
        img = img.convert("RGB")
        original_size = img.size

        # Resize down
        new_size = (
            int(original_size[0] * quality_percent / 100),
            int(original_size[1] * quality_percent / 100)
        )
        downscaled = img.resize(new_size, Image.LANCZOS)

        # Resize back to original
        upscaled = downscaled.resize(original_size, Image.LANCZOS)
        upscaled.save(output_path, format='JPEG')
    return time.time() - start

def calculate_pixel_change(original_path, quality_percent):     # Fungsi menghitung persentase perubahan jumlah pixel
    with Image.open(original_path) as img:
        width, height = img.size
        original_pixels = width * height
        new_width = int(width * quality_percent / 100)
        new_height = int(height * quality_percent / 100)
        new_pixels = new_width * new_height

        change = 100 * (original_pixels - new_pixels) / original_pixels
        return round(change, 2)

def get_file_size_kb(path):     # Fungsi untuk menghitung ukuran file (dalam KB)
    size_bytes = os.path.getsize(path)
    return round(size_bytes / 1024, 2)
