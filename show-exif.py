#!/usr/bin/env python3

import glob
import json
import os
import sys

from exiftools import exifutils

if __name__ == '__main__':
    param = sys.argv
    path_for_file_or_dir = param[1]

    result = None
    if os.path.isfile(path_for_file_or_dir):
        result = exifutils.get_exif_as_dict(path_for_file_or_dir)
    else:
        result = []
        for path_for_file in glob.glob(path_for_file_or_dir + "/*"):
            result.append(exifutils.get_exif_as_dict(path_for_file))

    print(json.dumps(result, ensure_ascii=False, indent=2))
