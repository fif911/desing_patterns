"""
Proxy that appears to be an underlying fully initialized object but in fact its not
its masquerading the underlying functionality

"""


class Bitmap:
    def __init__(self, filename):
        self.filename = filename
        print(f"Loading a image from filename")

    def draw(self):
        print(f"Drawing image {self.filename}")
    # it seems fine but actually its a bit problematic


class LazyBitmap:
    def __init__(self, filename):
        self.filename = filename
        self._bitmap = None

    def draw(self):
        if not self._bitmap:
            self._bitmap = Bitmap(self.filename)
        self._bitmap.draw()


def draw_image(image):
    print("About to draw image")
    image.draw()
    print("Done drawing image")


if __name__ == '__main__':
    # bmp = Bitmap("facepalm.jpg")
    bmp = LazyBitmap("facepalm.jpg")
    draw_image(bmp)
    print()
    draw_image(bmp)  # note that loading happens only once
    # but the problem is here
    # if we comment draw_image(bmp)
    # we still loading the image. And this process can be expensive
    # so the question is: how can we actually avoid drawing the image if we are not drawing it
    # one approach is to go to Bitmap class and modify it that its loads the image when we draw it
    # but lets image we dont want to modify it
    # lets build virtual proxy that will lazily load an image
