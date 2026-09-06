from PIL import Image
from PIL.ExifTags import TAGS, GPSTAGS


def get_basic_info(image_path):
    img = Image.open(image_path)
    print(f"Filename: {image_path}")
    print(f"Format: {img.format}")
    print(f"Size: {img.size}")
    print(f"Mode: {img.mode}")
    return img

def get_exif_data(img):
    exif_data = img.getexif()
    
    if not exif_data:
        print("\nNo EXIF data found in this image.")
        return {}
    
    readable_exif = {}
    for tag_id, value in exif_data.items():
        tag_name = TAGS.get(tag_id, tag_id)
        readable_exif[tag_name] = value
    
    return readable_exif


def print_key_details(exif):
    print("\n--- Key Details ---")
    print(f"Camera Make: {exif.get('Make', 'Not available')}")
    print(f"Camera Model: {exif.get('Model', 'Not available')}")
    print(f"Date Taken: {exif.get('DateTime', 'Not available')}")
    print(f"Software: {exif.get('Software', 'Not available')}")

def get_gps_data(exif):
    gps_ifd = exif.get_ifd(0x8825)
    
    if not gps_ifd:
        return None
    
    gps_data = {}
    for key, value in gps_ifd.items():
        tag_name = GPSTAGS.get(key, key)
        gps_data[tag_name] = value
    
    return gps_data

def convert_to_decimal(dms, direction):
    degrees, minutes, seconds = dms
    decimal = degrees + (minutes / 60) + (seconds / 3600)
    if direction in ["S", "W"]:
        decimal = -decimal
    return decimal

def print_gps_details(exif):
    gps = get_gps_data(exif)
    
    if not gps:
        print("\nNo GPS data found.")
        return
    
    try:
        lat = convert_to_decimal(gps["GPSLatitude"], gps["GPSLatitudeRef"])
        lon = convert_to_decimal(gps["GPSLongitude"], gps["GPSLongitudeRef"])
        print(f"\nGPS Coordinates: {lat:.6f}, {lon:.6f}")
        print(f"Google Maps: https://www.google.com/maps?q={lat},{lon}")
    except KeyError:
        print("\nGPS data present but incomplete.")

if __name__ == "__main__":
    img = get_basic_info("test.jpg")
    print("\nChecking for EXIF...")
    
    raw_exif = img.getexif()  # keep the raw object for GPS lookup
    exif = get_exif_data(img)  # readable dict for normal tags
    
    print(f"EXIF dict has {len(exif)} entries")
    if exif:
        print_key_details(exif)
        print_gps_details(raw_exif)  # pass raw_exif here, not exif
    else:
        print("Exif was empty, skipping key details.")
