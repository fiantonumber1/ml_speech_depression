import io, requests
import numpy as np
import cv2
from tensorflow.keras.preprocessing.image import img_to_array

url = "https://images.pexels.com/photos/236047/pexels-photo-236047.jpeg"
img_stream = io.BytesIO(requests.get(url).content)
image = cv2.imdecode(np.frombuffer(img_stream.read(), np.uint8), 1)
image = cv2.resize(image, (512, 512))
image = image.astype("float") / 255.0
image = img_to_array(image)
image = np.expand_dims(image, axis=0)

print(image)