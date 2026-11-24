"""After publishing the website, create its permanent QR image:
python make_qr.py https://USERNAME.github.io/REPO/
"""
import sys
import qrcode
from pathlib import Path
if len(sys.argv) != 2 or not sys.argv[1].startswith('https://'):
    raise SystemExit('Usage: python make_qr.py https://YOUR-PUBLISHED-SITE-URL/')
url = sys.argv[1].strip()
qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_H, box_size=14, border=4)
qr.add_data(url); qr.make(fit=True)
img = qr.make_image(fill_color='#083e39', back_color='white').convert('RGB')
path = Path(__file__).parent / 'qr-code.png';img.save(path)
print(f'QR saved: {path}\nTarget: {url}')
