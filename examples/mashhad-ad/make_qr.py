"""Generate the public repository QR; uses external ReportLab and Pillow."""
from pathlib import Path
import json
from reportlab.graphics.barcode.qr import QrCodeWidget
from PIL import Image, ImageDraw

URL = 'https://github.com/SultanAlfaifi/mashhad-video'
root = Path(__file__).resolve().parent / 'assets'
root.mkdir(exist_ok=True)
code = QrCodeWidget(URL, barLevel='M')
code.qr.make()
matrix = code.qr.modules
border, scale = 4, 12
size = (len(matrix) + border * 2) * scale
im = Image.new('RGB', (size, size), 'white')
d = ImageDraw.Draw(im)
for y, row in enumerate(matrix):
    for x, dark in enumerate(row):
        if dark:
            x0, y0 = (x + border) * scale, (y + border) * scale
            d.rectangle((x0, y0, x0 + scale - 1, y0 + scale - 1), fill='black')
im.save(root / 'repository-qr.png')
(root / 'qr-matrix.json').write_text(json.dumps({'url': URL, 'error_correction': 'M', 'border_modules': border, 'modules': matrix}), encoding='utf-8')
print(URL)
