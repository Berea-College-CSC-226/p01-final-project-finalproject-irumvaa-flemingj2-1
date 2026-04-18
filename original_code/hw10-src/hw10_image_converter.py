from PIL import Image, ImageEnhance


def img_r_diff(img_1, img_2):
    red_shift = img_2.pixelList[0][0] - img_1.pixelList[0][0]
    return abs(red_shift)

class ImageConverter:
    """
    Useful tool for converting images
    """
    def __init__(self, img_path):
        self.im = Image.open(img_path)
        self.pixelList = list(self.im.getdata())
        self.im_modified = None

    def shift_red(self, shift_val):
        """
        Shifts the red pixels by amount shift_val

        Args:
            shift_val: the amount to shift the red channel

        Returns: None

        """
        im2_pixels = []

        for i in self.pixelList:
            newRed = (i[0] + shift_val)
            if newRed > 255:
                newRed = 255
            if newRed < 0:
                newRed = 0
            pixel = (newRed, i[1], i[2])
            im2_pixels.append(pixel)
        self.im_modified = Image.new('RGB', self.im.size)
        self.im_modified.putdata(im2_pixels)

    def save_img(self, filename):
        """
        Saves the image to filename

        Args:
            filename: String of the new files filename

        Returns: None

        """
        if self.im_modified:
            self.im_modified.save(filename)


def main():
    """
    Small program to demonstrate shifting red. The first one has very little red, thus very little shift is noticed.
    The second image has lots of red, so a large shift is noticed.

    Returns:

    """
    i = ImageConverter("images/map.png")
    i.shift_red(3)
    i.save_img("images/map_2.png")

    i = ImageConverter("images/RF9152.png")
    i.shift_red(-200)
    i.save_img("images/RF9152_2.png")


if __name__ == "__main__":
    main()