Exif Tools
====

Command line tools for manipulate Exif(Exchangeable image file format) information. 

Features...
* Show Exif.
* Insert Exif overlay.

![overlay-exif](https://github.com/crossroad0201/exif-tools/raw/main/overlay-sample.jpg)

# Setup

## Requirements

* Python 3.x

* **Only tested on a Mac OS.**

## Get the code

Get the code via Git clone or download from Github.

### Git clone

```
> git clone https://github.com/crossroad0201/exif-tools.git
> cd exif-tools
```

### Download from Github

* Download from `Code > Download ZIP` .
* Unzip downloaded ZIP file to any place. (Ex. /User/Your name/Desktop/exif-tools-main)
* Open terminal and move to unzipped place.

## Install require modules

```
> pip install pillow
> pip install opencv-python
> pip install pyyaml
```

# Usage

## Show Exif

Show Exif information as JSON format.

```
> ./show-exif [--help] [DIR|FILE] [OPTIONS]
```

```
> ./show-exif sample-images/sample1.jpg
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

> ./show-exif sample-images
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

# Configuration

See [config.yaml](config.yaml).

You can specify any configuration file using '--config' option.

```
> ./overlay-exif.py sample-images/sample1.jpg --config custmized-config.yaml
``` 

# References

* https://github.com/karaage0703/python-image-processing/blob/master/photo_exif_date_print.py
* http://cachu.xrea.jp/perl/ExifTAG.html
* https://www.dinop.com/vc/exif01.html
* https://www.dinop.com/vc/exif02.html
* https://www.dinop.com/vc/exif03.html
* https://www.dinop.com/vc/exif04.html
