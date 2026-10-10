"""
Convert .webp images to .png format for Printify API compatibility.
"""
import os
import glob
from PIL import Image

def convert_directory(directory_path):
    """Convert all .webp files in a directory to .png"""
    search_pattern = os.path.join(directory_path, '*.webp')
    webp_files = glob.glob(search_pattern)
    
    if not webp_files:
        print(f"No .webp files found in {directory_path}")
        return
        
    print(f"Found {len(webp_files)} .webp files. Converting...")
    
    for webp_file in webp_files:
        png_file = webp_file.rsplit('.', 1)[0] + '.png'
        try:
            img = Image.open(webp_file)
            img.save(png_file, 'PNG')
            print(f"✅ Converted: {os.path.basename(webp_file)} -> {os.path.basename(png_file)}")
        except Exception as e:
            print(f"❌ Failed to convert {os.path.basename(webp_file)}: {e}")

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        target_dir = sys.argv[1]
        if os.path.isdir(target_dir):
            convert_directory(target_dir)
        else:
            print(f"Error: Directory not found: {target_dir}")
    else:
        print("Usage: python convert_webp_to_png.py <directory_path>")
