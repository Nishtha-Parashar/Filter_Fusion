import base64
from PIL import Image
import sys
img_path = sys.argv[1]
img = Image.open(str(img_path))
save_path= img_path.replace(sys.argv[2], "Pic.jpeg")
img.convert('LA').save(save_path)
print()