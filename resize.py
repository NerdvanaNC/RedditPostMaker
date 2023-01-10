from PIL import Image

def resize(filename):
  oldImg = Image.open(filename)
  width, height = oldImg.size

  newImg = Image.new('RGB', (width, width), '#121213')
  center = (width // 2) - (height // 2)
  newImg.paste(oldImg, (0, center))
  newImg.save(filename)

  return filename