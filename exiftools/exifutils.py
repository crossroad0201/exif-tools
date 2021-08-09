import os

from PIL import Image, TiffImagePlugin
from PIL.ExifTags import TAGS

CONTROL_CHARS = dict.fromkeys(range(32))


def get_exif_as_dict(image_file_path, debug_print=False):
    def __trim_str(value):
        return str.strip(value.translate(CONTROL_CHARS))

    image = Image.open(image_file_path)

    exif_info = image._getexif()
    exif_dict = {}
    if exif_info:
        for tag_id, raw_value in exif_info.items():
            tag = TAGS.get(tag_id, tag_id)

            value = None
            if isinstance(raw_value, str):
                value = __trim_str(raw_value)
            elif isinstance(raw_value, int):
                value = raw_value
            elif isinstance(raw_value, float):
                value = raw_value
            elif isinstance(raw_value, bytes):
                try:
                    value = __trim_str(raw_value.decode('utf8'))
                except UnicodeDecodeError:
                    value = __trim_str(str(raw_value).replace('\u0000', ''))
            elif isinstance(raw_value, TiffImagePlugin.IFDRational):
                value = raw_value.__float__()
            else:
                value = str.strip(str(raw_value))

            if debug_print:
                print("DEBUG: %s[%s] = %s => %s" % (tag, type(raw_value), raw_value, value))

            exif_dict[tag] = value

    image_dict = {
        'FileName': os.path.basename(image_file_path),
        'Exif': exif_dict
    }

    return image_dict
