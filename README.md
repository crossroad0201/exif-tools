Exif Tools
====

Command line tools for manipulate Exif(Exchangeable image file format) information. 

![overlay-exif](https://github.com/crossroad0201/exif-tools/raw/main/overlay-sample.jpg)

Features...
* Show Exif.
* Insert Exif overlay.

# Setup

## Requirements

* Python 3.x
* Git

* **Only tested on a Mac OS.**

## Clone this repository.

```
> git clone https://github.com/crossroad0201/exif-tools.git
> cd exif-tools
```

## Install require modules

```
> pip install pillow
> pip install opencv-python
```

# Usage

## Show Exif

Show Exif information as JSON format.

```
> ./show-exif [--help] [DIR|FILE] [OPTIONS]
```

```
> show-exif sample-images/sample1.jpg
{
  "FileName": "sample1.jpg",
  "Exif": {
      "ResolutionUnit": 2,
      "ExifOffset": 740,
      "Make": "FUJIFILM",
      "Model": "X-S10",
      "Software": "Digital Camera X-S10 Ver2.00",
      "Orientation": 1,
      "DateTime": "2021:08:08 13:16:05",
      "YResolution": 72.0,
      "Copyright": "",
      "XResolution": 72.0,
      "Artist": "",
      "ExifVersion": "0232",
          :
  }
}

> python show-exif sample-images
[
  {
    "FileName": "sample1.jpg",
    "Exif": { ... }
  }
  {
    "FileName": "sample2.jpg",
    "Exif": { ... }
  }
]
 ```

## Insert Exif overlay to the image

Insert Exif information to the image file as an overlay. 

```
> ./overlay-exif.py [--help] [DIR|FILE] [OPTIONS]
```

# References

* https://github.com/karaage0703/python-image-processing/blob/master/photo_exif_date_print.py
* http://cachu.xrea.jp/perl/ExifTAG.html
* https://www.dinop.com/vc/exif01.html
* https://www.dinop.com/vc/exif02.html
* https://www.dinop.com/vc/exif03.html
* https://www.dinop.com/vc/exif04.html
