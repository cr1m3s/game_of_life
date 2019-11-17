from PIL import Image

if __name__ == '__main__':
    image = Image.open('index.png').convert('1')

    width, height = image.size[0], image.size[1]
    print(width, height)
    aspect_ratio = height / width
    new_width = 50
    new_height = aspect_ratio * new_width
    image = image.resize((new_width, int(new_height)))

    chars = [' *', ' #']
    pixels = image.getdata()
    for pixel in pixels:
        print(pixel)
    new_pixels = []
    for pixel in pixels:
        if pixel == 0:
            new_pixels.append('*')
        else:
            new_pixels.append('#')
    new_pixels = ''.join(new_pixels)
    new_pixels_count = len(new_pixels)
    ascii_image = [new_pixels
                   [index:index + new_width]
                   for index in range(0, new_pixels_count, new_width)]
    print(ascii_image[1][1])
    ascii_image = '\n'.join(ascii_image)
    #print(ascii_image)


