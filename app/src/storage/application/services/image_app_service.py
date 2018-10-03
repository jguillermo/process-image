import PIL
import piexif
from PIL import Image


class ImageAppService:

    def __init__(self, file, name):
        self.name = name
        self.file = file
        self.rbg_img = None

    def _get_rgb_image(self):
        if self.rbg_img is None:
            orientation = self._get_orientation()
            image = Image.open(self.file)
            if orientation == 6:
                image = image.rotate(270, expand=True)
            self.rbg_img = image.convert('RGB')
        return self.rbg_img.copy()

    def image_resize(self, basewidth):
        img = self._get_rgb_image()
        path_file = '/app/files/{}_{}.jpg'.format(self.name, basewidth)
        wpercent = (basewidth / float(img.size[0]))
        hsize = int((float(img.size[1]) * float(wpercent)))
        img = img.resize((basewidth, hsize), PIL.Image.ANTIALIAS)
        img.save(path_file)
        return path_file

    def _get_orientation(self):
        imgo = Image.open(self.file)
        orientacion = 0
        try:
            if 'exif' in imgo.info:
                exif_dict = piexif.load(imgo.info["exif"])
                if piexif.ImageIFD.Orientation in exif_dict["0th"]:
                    orientacion = exif_dict["0th"][piexif.ImageIFD.Orientation]
        except Exception as e:
            print(e)
            orientacion = 0
        return orientacion
