#!/usr/bin/env python3

import argparse
import glob
import json
import os

from exiftools import exifutils

if __name__ == '__main__':
    arg_parser = argparse.ArgumentParser(description="Show Exif information of specified image file.")
    arg_parser.add_argument('input_path', type=str, help="Path for input image file or directory.")
    arg_parser.add_argument('--debug', action='store_true', help="Print debug information.")
    args = arg_parser.parse_args()

    result = args.input_path
    if os.path.isfile(args.input_path):
        result = exifutils.get_exif_as_dict(args.input_path, debug_print=args.debug)
    else:
        result = []
        for path_for_file in glob.glob(args.input_path + "/*"):
            result.append(exifutils.get_exif_as_dict(path_for_file, debug_print=args.debug))

    print(json.dumps(result, ensure_ascii=False, indent=2))
