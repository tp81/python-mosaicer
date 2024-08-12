# Mosaic Image Generator
This script creates a mosaic from a grid of images with a specified overlap percentage using linear blending in the overlap regions. The script supports both grayscale and RGB images.

## Requirements
  - Python 3.x
  - tifffile

You can install the required Python packages using pip:
```
pip install tifffile numpy
```

## Usage
```
python create_mosaic.py <image_folder> <grid_shape> <output_path> [--overlap_percentage <overlap_percentage>]
```

### Parameters
  - `image_folder`: The folder containing the input images.
  - `grid_shape`: The shape of the grid in the format `NxM` (e.g., `3x3`).
  - `output_path`: The path to save the output mosaic image.
  - `--overlap_percentage <overlap_percentage>`: (Optional) The overlap percentage (default is 10%).

### Example
```
python create_mosaic.py synthetic_images 3x3 mosaic.tif --overlap_percentage 10
```
This example creates a 3x3 mosaic with 10% overlap from images in the `synthetic_images` folder and saves it as `mosaic.tif`. The images are sorted based on the numbers extracted from their filenames before creating the mosaic.

## How It Works
  - *Image Reading and Sorting*: The script reads all `.tif` images from the specified folder and sorts them based on the numbers extracted from their filenames.
  - *Blending*: It blends overlapping regions of adjacent images both horizontally and vertically using linear blending.
  - *Mosaic Creation*: It assembles the images into a mosaic based on the specified grid shape and overlap percentage.


### Functions
  - `ensure_3d`: Ensures the image is 3D (for grayscale images, adds a channel dimension).
  - `blend_images_horizontally(image1, image2, overlap_width)`: Blends two images horizontally with a specified overlap width.
  - `blend_images_vertically(image1, image2, overlap_height)`: Blends two images vertically with a specified overlap height.
  - `extract_number_from_filename(filename)`: Extracts the first number found in the filename.
  - `create_mosaic_grid(image_paths, grid_shape, overlap_percentage)`: Creates a mosaic from a grid of images with overlap blending.

## Synthetic Image Generator
The script also includes a function to generate synthetic images for testing purposes.

### Usage
```
python generate_synthetic_images.py <output_folder> <grid_shape> <width> <height>
```
### Parameters
  - `output_folder`: The folder to save the generated images.
  - `grid_shape`: The shape of the grid in the format `NxM` (e.g., `3x3`).
  - `width`: The width of each synthetic image.
  - `height`: The height of each synthetic image.

### Example
```
python generate_synthetic_images.py synthetic_images 3x3 200 200
```
This example generates a 3x3 grid of synthetic images, each with a width and height of 200 pixels, and saves them in the `synthetic_images` folder.

### How It Works
  - The script generates synthetic images with random colors.
  - The images are saved in the specified output folder with filenames that include their position in the grid.

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.

## Acknowledgments
This script uses the `tifffile` and `numpy` libraries.
