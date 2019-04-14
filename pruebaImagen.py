from PIL import Image, ImageDraw
image = Image.open('cantones3.png')

width, height = image.size
center = (int(0.5 * width), int(0.5 * height))
yellow = (255, 255, 0, 255)
ImageDraw.floodfill(image, (428, 283), value=yellow)

image.show()
image.save('restante.png')