#!/usr/bin/env python3

import argparse
import glob
import os

import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFont

from exiftools import exifutils

font_color = (255, 255, 255)
output_file_name_suffix = '_exif'


def __insert_text_to_image(image_file_path, insert_text):
    base_img_cv2 = cv2.imread(image_file_path)

    base_img = Image.open(image_file_path).convert('RGBA')
    txt = Image.new('RGB', base_img.size, (0, 0, 0))
    draw = ImageDraw.Draw(txt)
    # TODO Specify Font file
    fnt = ImageFont.truetype('/Library/Fonts/Arial Black.ttf', size=(int)((base_img.size[0]+base_img.size[1])/150))

    textw, texth = draw.textsize(insert_text, font=fnt)

    draw.text(((base_img.size[0]*0.95 - textw) , (base_img.size[1]*0.95 - texth)),
              insert_text, font=fnt, fill=font_color)

    txt_array = np.array(txt)

    output_img = cv2.addWeighted(base_img_cv2, 1.0, txt_array, 1.0, 0)
    return output_img


def __insert_exif_overlay_to_image(image_file_path, debug_print, output_dir=None):
    print("Processing %s..." % image_file_path)

    filename_and_exif = exifutils.get_exif_as_dict(image_file_path, debug_print)
    exif_info = filename_and_exif.get("Exif")

    if exif_info:
        # TODO Configurable overlay.
        exif_text = \
            """
f/%(FNum)s %(ExposureTime)s %(FocalLength)smm ISO:%(ISO)s ExBias:%(ExposureBiasValue)s SS:%(ShutterSpeed)s
%(Make)s %(Model)s (%(LensMake)s %(LensModel)s)
%(Timestamp)s""" % {
                'ExposureBiasValue': exif_info.get('ExposureBiasValue'),
                'ExposureTime': "1/%s" % round(1 / exif_info.get('ExposureTime')),
                'FNum': exif_info.get('FNumber'),
                'FocalLength': exif_info.get('FocalLength'),
                'ISO': exif_info.get('ISOSpeedRatings'),
                'LensMake': exif_info.get('LensMake'),
                'LensModel': exif_info.get('LensModel'),
                'Make': exif_info.get('Make'),
                'Model': exif_info.get('Model'),
                'ShutterSpeed': exif_info.get('ShutterSpeedValue'),  # TODO math.log2(exif_info.get('ShutterSpeedValue')),
                'Timestamp': exif_info.get('DateTimeOriginal'), # TODO to Local time.
            }
        print("--- Exif info ---")
        print("%s" % exif_text)
        print("-----------------")
        output_image = __insert_text_to_image(image_file_path, exif_text)

        # TODO Configurable output path.
        output_dir = output_dir if output_dir else os.path.dirname(image_file_path)
        index_of_file_ext = os.path.basename(image_file_path).rindex(".")
        file_name_without_file_ext = os.path.basename(image_file_path)[:index_of_file_ext]
        file_ext = os.path.splitext(image_file_path)[1]
        output_file_name = "%s%s%s" % (file_name_without_file_ext, output_file_name_suffix, file_ext)
        output_file_path = os.path.join(output_dir, output_file_name)

        print("Output new image file to %s..." % output_file_path)
        cv2.imwrite(output_file_path, output_image)
        print("Done.")
    else:
        print("Exif information not included. Skipped.")


if __name__ == '__main__':
    arg_parser = argparse.ArgumentParser(description="Show Exif information of specified image file.")
    arg_parser.add_argument('input_path', type=str, help="Path for input image file or directory.")
    arg_parser.add_argument('--output_dir', type=str, help="Path for output directory. (DEFAULT Same place with input file)")
    arg_parser.add_argument('--debug', action='store_true', help="Print debug information.")
    args = arg_parser.parse_args()

    if os.path.isfile(args.input_path):
        __insert_exif_overlay_to_image(
            args.input_path,
            debug_print=args.debug,
            output_dir=args.output_dir
        )
    else:
        for path_for_file in glob.glob(args.input_path + "/*"):
            __insert_exif_overlay_to_image(
                path_for_file,
                debug_print=args.debug,
                output_dir=args.output_dir
            )
            print("")
