from PIL import Image

def resize(filename):
  oldImg = Image.open(filename)
  width, height = oldImg.size

  newImg = Image.new('RGB', (width, width), '#1a1a1b' if 'post' in filename else '#242425')
  center = (width // 2) - (height // 2)
  newImg.paste(oldImg, (0, center))
  newImg.save(filename)

  return filename