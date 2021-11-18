from PIL import Image
import numpy as np

img = Image.open("img2.jpg")
arr = np.array(img)
a = len(arr)
a1 = len(arr[1])
i = 0
while i <= a - 10:
    j = 0
    while j <= a1 - 10:
        pixels = 0
        for n in range(i, i + 10):
            for k in range(j, j + 10):
                r = arr[n][k][0]
                g = arr[n][k][1]
                b = arr[n][k][2]
                M = (int(r) + int(g) + int(b)) / 3
                pixels += M
        pixels = int(pixels // 100)
        for n in range(i, i + 10):
            for k in range(j, j + 10):
                arr[n][k][0] = int(pixels // 50) * 50
                arr[n][k][1] = int(pixels // 50) * 50
                arr[n][k][2] = int(pixels // 50) * 50
        j = j + 10
    i = i + 10
res = Image.fromarray(arr)
res.save('res.jpg')
