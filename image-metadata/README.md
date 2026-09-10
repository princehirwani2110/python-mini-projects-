# Image Metadata Extractor

A command-line tool that extracts EXIF metadata from image files — camera details, timestamp, and GPS location (when available) — and converts GPS coordinates into a clickable Google Maps link.

## What it does

- Reads basic image info: format, size, color mode
- Extracts EXIF data: camera make, model, date taken, software used
- Extracts and decodes GPS coordinates (if present), converting from degrees/minutes/seconds into decimal format
- Generates a direct Google Maps link from the coordinates

## Requirements

- Python 3
- Pillow

Install dependencies:
```bash
pip3 install Pillow
```

## Usage

```bash
python3 image_metadata.py <path_to_image>
```

Example:
```bash
python3 image_metadata.py test.jpg
```

## Example output

Filename: test.jpg
Format: JPEG
Size: (5712, 4284)
Mode: RGB

Checking for EXIF...
EXIF dict has 12 entries

--- Key Details ---
Camera Make: Apple
Camera Model: iPhone 16
Date Taken: 2026:08:23 17:20:29
Software: 26.5

GPS Coordinates: 28.613900, 77.209000
Google Maps: https://www.google.com/maps?q=28.613900,77.209000


## Notes

- Not all images contain EXIF data. Screenshots, and images sent through apps like WhatsApp or Instagram, typically have this metadata stripped.
- GPS data is only present if Location Services was enabled when the photo was taken.
- HEIC images (common on iPhone) need to be converted to JPEG first, since Pillow doesn't read HEIC natively:
```bash
  sips -s format jpeg input.HEIC --out output.jpg
```