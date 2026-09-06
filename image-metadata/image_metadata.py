from PIL import Image

def get_basic_info(image_path):
    img = Image.open(image_path)
    print(f"Filename: {image_path}")
    print(f"Format: {img.format}")
    print(f"Size: {img.size}")
    print(f"Mode: {img.mode}")

if __name__ == "__main__":
    get_basic_info("test.jpg")