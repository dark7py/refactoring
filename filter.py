from PIL import Image
import numpy as np
import math


def get_size_from_input(inp: str, img_width: int, img_height: int):
    inp = inp.split(' ')

    if len(inp) == 1 and inp[0].endswith('px'):
        pixels_count = int(inp[0][0:-2])

        if pixels_count < 1:
            raise ValueError('Pixel count cannot be lesser than 1')

        pixel_side = int(math.sqrt((img_width * img_height) / pixels_count))
        return [pixel_side, pixel_side]

    if len(inp) > 0:
        side1 = int(img_width / 100 * int(inp[0][0:-1])) if inp[0].endswith('%') else int(inp[0])

        if side1 < 1:
            raise ValueError('Pixel side cannot be lesser than 1')

        side2 = side1
        if len(inp) > 1:
            side1 = int(img_height / 100 * int(inp[1][0:-1])) if inp[1].endswith('%') else int(inp[1])
            if side2 < 1:
                raise ValueError('Pixel side cannot be lesser than 1')
        return [side1, side2]

    raise ValueError('Wrong Input!')


def get_filtered_arr(array: np.ndarray, height: int, width: int, pixel_height, pixel_width, gray_step):
    i = 0
    while i < height:
        j = 0
        while j < width:
            pixel_sum = 0
            pixel_bottom_border = height_arr if (i + pixel_height) > height_arr else i + pixel_height
            pixel_right_border = width_arr if (j + pixel_width) > width_arr else j + pixel_width
            for n in range(i, pixel_bottom_border):
                for k in range(j, pixel_right_border):
                    r, g, b = array[n][k]
                    median = (int(r) + int(g) + int(b)) / 3
                    pixel_sum += median
            pixel_sum = int(
                int(pixel_sum // ((pixel_bottom_border - i) * (pixel_right_border - j))) // gray_step) * gray_step
            for n in range(i, pixel_bottom_border):
                for k in range(j, pixel_right_border):
                    array[n][k] = [pixel_sum, pixel_sum, pixel_sum]
            j += pixel_width
        i += pixel_height
    return array


img = Image.open("img2.jpg")
arr = np.array(img)
height_arr = len(arr)
width_arr = len(arr[0])

p_height, p_width = get_size_from_input(input('Please, input pixel parameters\n'
                                              'Possible parameters:\n'
                                              '- pixel width and height separated by space (absolute)\n'
                                              '- pixel width and height separated by space (relative (use "%"))\n'
                                              '- pixel width and height (one number, square pixel)\n'
                                              '- pixel count (number with "px" at the end)\n'), width_arr, height_arr)

step = 256 // int(input('Please, input gradation count\n'))
extension = input('Please, input file extension (jpg, png, etc.)\n')

res = Image.fromarray(get_filtered_arr(arr, height_arr, width_arr, p_height, p_width, step))
res.save(f'res.{extension}')
