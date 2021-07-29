from PIL import Image
import os

directory = "./pre/"
directory2 = "./post/"

for filename in os.listdir(directory):
    if filename.endswith(".png"):
        # print(os.path.join(directory, filename))
        img = Image.open(os.path.join(directory, filename))  # get image
        img = img.convert("RGBA")
        datas = img.getdata()

        newData = []
        for item in datas:
            if item[0] == 255 and item[1] == 255 and item[2] == 255:
                newData.append((255, 255, 255, 0))
            else:
                newData.append(item)
        img.putdata(newData)

        img.save("./post/"+filename+"_mod.png", "PNG")


for filename in os.listdir(directory2):
    if filename.endswith(".png"):
        # print(os.path.join(directory, filename))
        img2 = Image.open(os.path.join(directory, filename))  # get image

        pixels = img2.load()  # create the pixel map

        for i in range(img2.size[0]):  # for every pixel:
            for j in range(img2.size[1]):
                if not any(value <= 10 for value in pixels[i, j]):
                    pixels[i, j] = (255, 255, 255)  # change to white

        img2.save("./final/"+filename+"_final.png", "PNG")

