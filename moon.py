#!/usr/bin/python3

import os
import ephem
import math
from wand.image import Image
from wand.drawing import Drawing
from wand.color import Color

full_moon_image = "moon.png"            # Input (full moon) image file name
phase_moon_image = "/tmp/moon_phase.png"    # Output image file name

path = os.path.dirname(os.path.realpath(__file__))

m = ephem.Moon()
m.compute()
phase = 1 - m.moon_phase
a = m.elong


#Draw phase shade on input moon image and save
with Image(filename=f'{path}/{full_moon_image}') as img:
    radius = img.height // 2
    with Drawing() as draw:
        draw.fill_color = Color("rgba(0, 0, 0, 0.7)")
        for y in range(radius):
            x = round(math.sqrt(radius**2 - y**2))
            X = radius - x*math.copysign(1,a)
            Y = radius - y
            Y_mirror = radius + y
            moon_width = 2 * (radius - X)
            shade = round(moon_width * phase)
            x_shade = X + shade
            draw.line((X, Y), (x_shade, Y))
            if Y_mirror != Y:
                draw.line((X, Y_mirror), (x_shade, Y_mirror))
        draw(img)
        img.save(filename=phase_moon_image)
