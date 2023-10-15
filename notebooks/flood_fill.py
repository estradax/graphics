import numpy as np

def flood_fill4(img, x, y, fill, old):
    current = img[x, y]
    if current == np.float32(old):
        img[x, y] = fill
        flood_fill4(img, x+1, y, fill, old)
        flood_fill4(img, x-1, y, fill, old)
        flood_fill4(img, x, y+1, fill, old)
        flood_fill4(img, x, y-1, fill, old)

def flood_fill8(img, x, y, fill, old):
    current = img[x, y]
    if current == np.float32(old):
        img[x, y] = fill
        flood_fill8(img, x+1, y, fill, old)
        flood_fill8(img, x-1, y, fill, old)
        flood_fill8(img, x, y+1, fill, old)
        flood_fill8(img, x, y-1, fill, old)
        flood_fill8(img, x+1, y-1, fill, old)
        flood_fill8(img, x-1, y-1, fill, old)
        flood_fill8(img, x+1, y+1, fill, old)
        flood_fill8(img, x-1, y+1, fill, old)
