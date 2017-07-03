# Google Image Downloader

> A simple script that fetches images from Google with browser simulation.

## Pre-requisites

The following Python packages are required to run the script.

- selenium
- requests
- fake_useragent
- beautifulsoup4
- lxml

You can install them via `pip install -r requirements.txt`. You also need install the ChromeDriver
for selenium to work. Please refer to [here](https://sites.google.com/a/chromium.org/chromedriver/getting-started)
on how to install it.

## Usage

Once you installed all the packages, run the script with `-h` argument to see how it works

```bash
$ python3 download_images.py -h
usage: download_images.py [-h] keyword

positional arguments:
  keyword     the keyword to search

optional arguments:
    -h, --help  show this help message and exit
```

Therefore, to search something, simply type

```bash
$ python3 download_images.py <your keyword>
```

