import numpy as np
import tifffile as tiff
import os

def create_synthetic_image(width, height, color):
    """Create a synthetic image of the given size and color."""
    image = np.full((height, width, 3), color, dtype=np.uint8)
    return image

def create_image_grid(grid_shape, image_size, overlap_percentage=10):
    width, height = image_size
    overlap_width = int(width * overlap_percentage / 100)
    overlap_height = int(height * overlap_percentage / 100)
    
    images = []
    for i in range(grid_shape[0]):
        for j in range(grid_shape[1]):
            # Generate a different color for each image
            color = ((i * grid_shape[1] + j) * 50 % 256, (i * grid_shape[1] + j) * 80 % 256, (i * grid_shape[1] + j) * 110 % 256)
            image = create_synthetic_image(width, height, color)
            images.append(image)
    
    # Ensure the output directory exists
    output_dir = "synthetic_images"
    os.makedirs(output_dir, exist_ok=True)
    
    # Save images to disk
    for idx, img in enumerate(images):
        tiff.imwrite(os.path.join(output_dir, f'image_{idx + 1}.tif'), img)
    
    return images

# Example usage
grid_shape = (3, 3)  # 3x3 grid
image_size = (200, 200)  # Each image is 200x200 pixels
create_image_grid(grid_shape, image_size, overlap_percentage=10)

print(f"Synthetic images have been created and saved in the 'synthetic_images' directory.")
