from PIL import Image
import os

def get_license_image():

  root_dir = os.path.dirname(os.path.abspath(__file__))
  image_path = os.path.join('ressources','apache-logo.webp')
  
  return Image.open(os.path.join(root_dir,image_path))