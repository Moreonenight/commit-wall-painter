from PIL import Image, ImageFont, ImageDraw
import os

COMMIT_PIXEL_LIST = [50, 30, 20, 10]
STANDARD_CHAR_LIST = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\\|()1{}[]?-_+~<>i!lI;:,\"^'\`. ")

def img2ascii(grey_image, char_list, scaled_img_width=53, scaled_img_height=7):
    scaled_grey_img = grey_image.resize((scaled_img_width, scaled_img_height))
    char_list_length = len(char_list)
    ascii_img = [[None for i in range(scaled_img_width)] for j in range(scaled_img_height)]

    for i in range(scaled_img_height):
        for j in range(scaled_img_width):
            brightness = scaled_grey_img.getpixel((j, i))
            ascii_img[i][j] = char_list[min(int(brightness * char_list_length / 255), char_list_length-1)]
    return ascii_img


im = Image.new("RGB", (53, 11), (255, 255, 255))
dr = ImageDraw.Draw(im)
font = ImageFont.truetype("smallest_pixel-7.ttf", 10)

# im = Image.open("test.png")
text = '  MY TEST :)'
# text = '1234567'

dr.text((0, 0), text, font=font, fill="#000000")
im = im.crop((0,2,53,9))

grey_image = im.convert("L")
outCommit = img2ascii(grey_image, COMMIT_PIXEL_LIST)
outPreview = img2ascii(grey_image, STANDARD_CHAR_LIST)
print(outCommit)

for i in range(len(outPreview)):
    for j in range(len(outPreview[i])):
        print(str(outPreview[i][j]), end='') 
    print()

# with open('preview.txt','w',encoding='gbk') as output:
#     for i in range(len(outPreview)):
#         for j in range(len(outPreview[i])):
#             output.write(str(outPreview[i][j])) 
#         output.write('\n') 
