<h1>Mosaic Image Generator</h1>
<p>This script creates a mosaic from a grid of images with a specified overlap percentage using linear blending in the overlap regions. The script supports both grayscale and RGB images.</p>

<h2>Requirements</h2>
<p>Python 3.x</p>
<p>tifffile</p>
<p>numpy</p>
<p>You can install the required Python packages using pip:</p>
<pre><code>pip install tifffile numpy</code></pre>

<h2>Usage</h2>
<pre><code>python create_mosaic.py &lt;image_folder&gt; &lt;grid_shape&gt; &lt;output_path&gt; [--overlap_percentage]</code></pre>

<h3>Parameters</h3>
<ul>
    <li><code>image_folder</code>: The folder containing the input images.</li>
    <li><code>grid_shape</code>: The shape of the grid in the format <code>NxM</code> (e.g., <code>3x3</code>).</li>
    <li><code>output_path</code>: The path to save the output mosaic image.</li>
    <li><code>--overlap_percentage</code>: (Optional) The overlap percentage (default is 10%).</li>
</ul>

<h3>Example</h3>
<pre><code>python create_mosaic.py synthetic_images 3x3 mosaic.tif --overlap_percentage 10</code></pre>
<p>This example creates a 3x3 mosaic with 10% overlap from images in the <code>synthetic_images</code> folder and saves it as <code>mosaic.tif</code>. The images are sorted based on the numbers extracted from their filenames before creating the mosaic.</p>

<h2>How It Works</h2>
<ol>
    <li><strong>Image Reading and Sorting</strong>: The script reads all <code>.tif</code> images from the specified folder and sorts them based on the numbers extracted from their filenames.</li>
    <li><strong>Blending</strong>: It blends overlapping regions of adjacent images both horizontally and vertically using linear blending.</li>
    <li><strong>Mosaic Creation</strong>: It assembles the images into a mosaic based on the specified grid shape and overlap percentage.</li>
</ol>

<h3>Functions</h3>
<ul>
    <li><code>ensure_3d(image)</code>: Ensures the image is 3D (for grayscale images, adds a channel dimension).</li>
    <li><code>blend_images_horizontally(image1, image2, overlap_width)</code>: Blends two images horizontally with a specified overlap width.</li>
    <li><code>blend_images_vertically(image1, image2, overlap_height)</code>: Blends two images vertically with a specified overlap height.</li>
    <li><code>extract_number_from_filename(filename)</code>: Extracts the first number found in the filename.</li>
    <li><code>create_mosaic_grid(image_paths, grid_shape, overlap_percentage)</code>: Creates a mosaic from a grid of images with overlap blending.</li>
</ul>

<h2>License</h2>
<p>This project is licensed under the MIT License. See the <code>LICENSE</code> file for details.</p>

<h2>Acknowledgments</h2>
<p>This script uses the <code>tifffile</code> and <code>numpy</code> libraries.</p>
