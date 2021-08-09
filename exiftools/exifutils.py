import os

from PIL import Image, TiffImagePlugin
from PIL.ExifTags import TAGS


def get_exif_as_dict(image_file_path):
    image = Image.open(image_file_path)

    exif_info = image._getexif()
    exif_dict = {}
    if exif_info:
        for tag_id, raw_value in exif_info.items():
            tag = TAGS.get(tag_id, tag_id)

            value = None
            if isinstance(raw_value, str):
                value = raw_value
            elif isinstance(raw_value, int):
                value = raw_value
            elif isinstance(raw_value, float):
                value = raw_value
            elif isinstance(raw_value, bytes):
                try:
                    value = str.strip(raw_value.decode().replace('\u0000', ''))
                except UnicodeDecodeError:
                    value = str.strip(str(raw_value).replace('\u0000', ''))
            elif isinstance(raw_value, TiffImagePlugin.IFDRational):
                value = raw_value.__float__()
            else:
                value = str.strip(str(raw_value))

            # print("%s[%s] = %s = %s" % (tag, type(raw_value), raw_value, value))

            exif_dict[tag] = value

    image_dict = {
        'FileName': os.path.basename(image_file_path),
        'Exif': exif_dict
    }

    return image_dict
