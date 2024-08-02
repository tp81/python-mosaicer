import numpy as np
import tifffile as tiff
import os
import sys

def generate_synthetic_images(output_folder, grid_shape, width, height):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    grid_rows, grid_cols = map(int, grid_shape.split('x'))
    
    for i in range(grid_rows):
        for j in range(grid_cols):
            # Create a synthetic image with random colors
            image = np.random.rand(height, width, 3).astype(np.float32)
            
            # Construct the filename based on the grid position
            filename = f'image_{i * grid_cols + j + 1:03d}.tif'
            filepath = os.path.join(output_folder, filename)
            
            # Save the image
            tiff.imwrite(filepath, image)
    
    print(f'Generated {grid_rows * grid_cols} synthetic images in {output_folder}')

if __name__ == '__main__':
    if len(sys.argv) != 5:
        print('Usage: python generate_synthetic_images.py <output_folder> <grid_shape> <width> <height>')
        print('Example: python generate_synthetic_images.py synthetic_images 3x3 200 200')
        sys.exit(1)
    
    output_folder = sys.argv[1]
    grid_shape = sys.argv[2]
    width = int(sys.argv[3])
    height = int(sys.argv[4])
    
    generate_synthetic_images(output_folder, grid_shape, width, height)
