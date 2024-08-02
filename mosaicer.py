import tifffile as tiff
import numpy as np
import glob

def ensure_3d(image):
    """Ensure the image is 3D (for grayscale images, add a channel dimension)."""
    if len(image.shape) == 2:
        return image[:, :, np.newaxis]
    return image

def blend_images_horizontally(image1, image2, overlap_width):
    image1 = ensure_3d(image1)
    image2 = ensure_3d(image2)
    channels = image1.shape[2]
    
    # Create weight maps for horizontal blending
    weight_map1 = np.tile(np.linspace(1, 0, overlap_width).reshape(1, -1, 1), (image1.shape[0], 1, channels))
    weight_map2 = np.tile(np.linspace(0, 1, overlap_width).reshape(1, -1, 1), (image1.shape[0], 1, channels))
    
    # Extract the overlap regions
    overlap1 = image1[:, -overlap_width:]
    overlap2 = image2[:, :overlap_width]
    
    # Blend the overlap regions
    blended_overlap = (overlap1 * weight_map1 + overlap2 * weight_map2).astype(np.uint8)
    
    # Combine the non-overlapping regions with the blended overlap
    blended_image = np.hstack((image1[:, :-overlap_width], blended_overlap, image2[:, overlap_width:]))
    
    return blended_image

def blend_images_vertically(image1, image2, overlap_height):
    image1 = ensure_3d(image1)
    image2 = ensure_3d(image2)
    channels = image1.shape[2]
    
    # Create weight maps for vertical blending
    weight_map1 = np.tile(np.linspace(1, 0, overlap_height).reshape(-1, 1, 1), (1, image1.shape[1], channels))
    weight_map2 = np.tile(np.linspace(0, 1, overlap_height).reshape(-1, 1, 1), (1, image1.shape[1], channels))
    
    # Extract the overlap regions
    overlap1 = image1[-overlap_height:, :]
    overlap2 = image2[:overlap_height, :]
    
    # Blend the overlap regions
    blended_overlap = (overlap1 * weight_map1 + overlap2 * weight_map2).astype(np.uint8)
    
    # Combine the non-overlapping regions with the blended overlap
    blended_image = np.vstack((image1[:-overlap_height, :], blended_overlap, image2[overlap_height:, :]))
    
    return blended_image

def create_mosaic_grid(image_paths, grid_shape, overlap_percentage=10):
    # Read the images
    images = [tiff.imread(image_path) for image_path in image_paths]
    
    # Ensure all images have the same size
    heights = [img.shape[0] for img in images]
    widths = [img.shape[1] for img in images]
    if len(set(heights)) != 1 or len(set(widths)) != 1:
        raise ValueError("All images must have the same dimensions.")
    
    # Calculate the overlap width and height
    overlap_width = int(widths[0] * overlap_percentage / 100)
    overlap_height = int(heights[0] * overlap_percentage / 100)
    
    # Create an empty list to store rows
    rows = []
    
    # Process each row in the grid
    for i in range(grid_shape[0]):
        # Start with the first image in the row
        row_mosaic = ensure_3d(images[i * grid_shape[1]])
        
        # Blend each image with the previous one horizontally
        for j in range(1, grid_shape[1]):
            row_mosaic = blend_images_horizontally(row_mosaic, ensure_3d(images[i * grid_shape[1] + j]), overlap_width)
        
        rows.append(row_mosaic)
    
    # Start with the first row
    mosaic = rows[0]
    
    # Blend each row with the previous one vertically
    for i in range(1, len(rows)):
        mosaic = blend_images_vertically(mosaic, rows[i], overlap_height)
    
    # If the input images were grayscale, remove the extra dimension
    if mosaic.shape[2] == 1:
        mosaic = mosaic[:, :, 0]
    
    return mosaic

# Example usage
image_paths = glob.glob("synthetic_images/*.tif")  # Adjust the path and file extension as needed
grid_shape = (3, 3)  # For example, a 3x3 grid
mosaic = create_mosaic_grid(image_paths, grid_shape, overlap_percentage=10)
tiff.imwrite("mosaic.tif", mosaic)
