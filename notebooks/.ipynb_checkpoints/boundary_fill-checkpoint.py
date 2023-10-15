def boundary_fill4(img, x, y, fill, boundary):
    current = img[x, y]
    if current != boundary and current != fill:
        img[x, y] = fill
        boundary_fill4(img, x+1, y, fill, boundary)
        boundary_fill4(img, x-1, y, fill, boundary)
        boundary_fill4(img, x, y+1, fill, boundary)
        boundary_fill4(img, x, y-1, fill, boundary)

def boundary_fill8(img, x, y, fill, boundary):
    current = img[x, y]
    if current != boundary and current != fill:
        img[x, y] = fill
        boundary_fill8(img, x+1, y, fill, boundary)
        boundary_fill8(img, x-1, y, fill, boundary)
        boundary_fill8(img, x, y+1, fill, boundary)
        boundary_fill8(img, x, y-1, fill, boundary)
        boundary_fill8(img, x+1, y-1, fill, boundary)
        boundary_fill8(img, x-1, y-1, fill, boundary)
        boundary_fill8(img, x+1, y+1, fill, boundary)
        boundary_fill8(img, x-1, y+1, fill, boundary)
