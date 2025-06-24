from flask import Flask, render_template, request, send_file, send_from_directory
from werkzeug.utils import secure_filename
import os
from image_utils import compress_image, calculate_pixel_change, get_file_size_kb

app = Flask(__name__)

# Folder input/output di luar src/
UPLOAD_FOLDER = os.path.join('..', 'test', 'uploads')
COMPRESSED_FOLDER = os.path.join('..', 'test', 'compressed')

# Pastikan folder ada
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(COMPRESSED_FOLDER, exist_ok=True)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        file = request.files['image']
        quality = int(request.form['quality'])

        if file:
            filename = secure_filename(file.filename)
            input_path = os.path.join(UPLOAD_FOLDER, filename)
            file.save(input_path)

            # Nama file hasil
            output_filename = 'compressed_' + filename.rsplit('.', 1)[0] + '.jpg'
            output_path = os.path.join(COMPRESSED_FOLDER, output_filename)

            # Jalankan kompresi dan hitung data
            runtime = compress_image(input_path, output_path, quality)
            pixel_change = calculate_pixel_change(input_path, quality)
            original_size = get_file_size_kb(input_path)
            compressed_size = get_file_size_kb(output_path)

            # Path relatif untuk akses gambar via route khusus
            input_rel = f"test/uploads/{filename}"
            output_rel = f"test/compressed/{output_filename}"

            return render_template('index.html',
                                   input_image=input_rel,
                                   output_image=output_rel,
                                   runtime=round(runtime, 4),
                                   pixel_change=pixel_change,
                                   original_size=original_size,
                                   compressed_size=compressed_size,
                                   download_link=output_rel)

    return render_template('index.html')

# ROUTE: Menyediakan file dari luar folder static
@app.route('/test/<path:filename>')
def serve_test_files(filename):
    return send_from_directory('../test', filename)

@app.route('/download/<path:filename>')
def download_file(filename):
    return send_file(os.path.join('..', filename), as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
