from PIL import Image
import pytesseract

class Languages:
    CHS = 'chi_sim'
    CHT = 'chi_tra'
    ENG = 'eng'
    MIX = 'eng+chi_sim'

def img_to_str(image_path, lang=Languages.ENG):
    return pytesseract.image_to_string(Image.open(image_path), lang)

print(img_to_str('/Users/gitwork/sp1_dev/python/text-detection/data/results/0PVC-U管材1.jpg', lang=Languages.MIX))
