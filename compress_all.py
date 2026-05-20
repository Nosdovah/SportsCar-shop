import os
from PIL import Image

def optimize_images(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.lower().endswith(('.png', '.jpg', '.jpeg')):
                path = os.path.join(root, file)
                
                try:
                    with Image.open(path) as img:
                        # Convert to WebP format
                        webp_path = os.path.splitext(path)[0] + '.webp'
                        
                        # Max width for hero images is 1600, for others 1200
                        max_width = 1600 if 'hero' in file.lower() else 1200
                        
                        if img.width > max_width:
                            ratio = max_width / img.width
                            new_size = (max_width, int(img.height * ratio))
                            img = img.resize(new_size, Image.Resampling.LANCZOS)
                        
                        img.save(webp_path, 'webp', quality=85)
                        print(f"Compressed {file} -> {os.path.basename(webp_path)}")
                        
                except Exception as e:
                    print(f"Error compressing {path}: {e}")

optimize_images('images')
