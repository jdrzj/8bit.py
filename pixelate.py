import numpy as np
from PIL import Image

class Pixelate:
    def run(self, input_path: str, output_path: str, pixel_size: int):
        image = Image.open(input_path)
        image_array = np.array(image)
        pixelate_image_array = self._pixelate(image_array, pixel_size)
        pixelate_image = Image.fromarray(pixelate_image_array)
        pixelate_image.save(output_path)
        return pixelate_image_array

    def _pixelate(self, image_array: np.array, pixel_size: int) -> np.array:
        (h, w, _) = image_array.shape
        parts_x = int(h / pixel_size) + 1
        parts_y = int(w / pixel_size) + 1

        for x in range(0, parts_x):
            for y in range(0, parts_y):
                x1 = x * pixel_size
                x2 = (x + 1) * pixel_size
                y1 = y * pixel_size
                y2 = (y + 1) * pixel_size
                box = image_array[x1:x2, y1:y2]
                avg = np.average(box, axis=(0, 1))
                image_array[x1:x2, y1:y2] = avg

        return image_array
