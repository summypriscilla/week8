from PIL import image
image_path='/home/mokshitha/Downloads/week-8/nene.png'
image=image.open('/home/mokshitha/Downloads/week-8/nene.png')
x,y=100,100
rgb=image.getpixel((x,y))
print(f'RGB values at position ({x},{y}): {rgb}')
new_rgb=(255,0,0)
image.putpixel((x,y),new_rgb)
output_path='/home/mokshitha/Downloads/week-8/nene.png'
image.save(output_path)
image.close()
