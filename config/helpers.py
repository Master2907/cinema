import os
from datetime import datetime
from django.utils.deconstruct import deconstructible


@deconstructible
class UploadTo:

    def __init__(self, folder):
        self.folder = folder

    def __call__(self, instance, filename):
        # my_photo.png => [my_photo, png]
        ext = os.path.splitext(filename)[1]

        return "{}/{:%Y-%m}/{:%Y-%m-%d-%H-%M-%S-%f}{}".format(
            self.folder,
            datetime.now(),
            datetime.now(),
            ext
        )
