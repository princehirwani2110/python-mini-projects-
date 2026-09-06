from PIL import Image
from PIL.ExifTags import TAGS


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

if __name__ == "__main__":
    img = get_basic_info("test.jpg")
    print("\nChecking for EXIF...")
    exif = get_exif_data(img)
    print(f"EXIF dict has {len(exif)} entries")
    if exif:
        print_key_details(exif)
    else:
        print("Exif was empty, skipping key details.")
        
