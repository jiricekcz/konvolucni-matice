import matplotlib.image as mpimg
import numpy as np
import sys
from os import path
import json


OPTIONS_PATH = path.join(path.dirname(path.abspath(__file__)), "../resources/kernel.json")
def convolution(image: np.ndarray, kernel: np.ndarray, image_channel_limit: int=4) -> np.ndarray:
    """
    Convolve an image with a kernel.
    image_channel_limit: The number of channels to convolve. If the image has more channels than this, the extra channels will be copied over without convolution.
    """
    # Saves values describing the image and kernel
    kernel_size = kernel.shape[0]
    kernel_radius = kernel_size // 2
    image_height = image.shape[0]
    image_width = image.shape[1]
    image_channels = image.shape[2]
    # Creates a new image to store the convolved image
    result = np.zeros((image_height, image_width, image_channels), dtype=np.float32)

    # Loops through each pixel in the image
    for y in range(image_height):
        for x in range(image_width):
            # Loops through each channel in the image
            for c in range(image_channels):
                # If the channel is greater than the channel limit, copy the pixel over without convolution
                if (c >= image_channel_limit):
                    result[y, x, c] = image[y, x, c]
                    continue
                # Loops through each pixel in the kernel
                for ky in range(kernel_size):
                    for kx in range(kernel_size):
                        # Calculates the coordinates of the pixel in the image that the kernel pixel is currently over
                        iy = y + ky - kernel_radius
                        ix = x + kx - kernel_radius
                        # If the pixel is outside the image, skip it
                        if (iy < 0 or iy >= image_height or ix < 0 or ix >= image_width):
                            continue
                        # Adds the weighted pixel value to the result
                        result[y, x, c] += image[iy, ix, c] * kernel[ky, kx]
                # Clamps the result pixel value between 0 and 1
                result[y, x, c] = max(0, min(1, result[y, x, c]))

    return result


def main() -> None:
    # Saves the arguments count
    arg_count = len(sys.argv)
    # If input path is not provided as an argument, exit with error
    if (arg_count < 2):
        print("Please specify source path")
        exit(1)
    source_path = sys.argv[1]
    # If output path is not provided as an argument set it to the default value
    if (arg_count < 3):
        save_path = ".".join(source_path.split(".")[0:-1]) + "_new.png"
        print(f"Save path not specified, using {save_path}")
    else:
        save_path = sys.argv[2]
    
    # Loads the image
    img = mpimg.imread(source_path)
    # Loads options
    with open(OPTIONS_PATH) as f:
        options = json.load(f)
        kernel = np.array(options["kernel"])
        limit = options["channel_limit"]
    # Convolve the image
    img_new = convolution(img, kernel, image_channel_limit=limit)

    # Saves the image
    mpimg.imsave(save_path, img_new) 
if __name__ == "__main__":
    main()

