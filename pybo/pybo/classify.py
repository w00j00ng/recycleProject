import tensorflow.keras
from PIL import Image, ImageOps
import numpy as np
from pybo.config import homedir

def clf(fdir):
    categori=['cardboard', 'glass', 'metal', 'paper', 'plastic', 'trash']
    np.set_printoptions(suppress=True)

    model = tensorflow.keras.models.load_model(homedir + '/static/keras_model.h5')

    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

    image = Image.open(fdir)

    size = (224, 224)
    image = ImageOps.fit(image, size, Image.ANTIALIAS)

    image_array = np.asarray(image)

    normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1

    # Load the image into the array
    data[0] = normalized_image_array

    # run the inference
    prediction = model.predict(data)
    arg_result = np.argmax(prediction, axis = -1)
    print(categori[int(arg_result)])

    return categori[int(arg_result)]
