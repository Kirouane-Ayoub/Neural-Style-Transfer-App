import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2' 
import tensorflow as tf
import numpy as np
import cv2

class NST() : 
    def __init__(self):
        super().__init__()

    def load_image(self , img_path):
        img = tf.io.read_file(img_path)
        img = tf.image.decode_image(img, channels=3)
        img = tf.image.convert_image_dtype(img, tf.float32)
        img = img[tf.newaxis, :]
        return img


    def transfer(self , content , style):
        model_path = "magenta_arbitrary-image-stylization-v1-256_2"
        model = tf.saved_model.load(model_path , tags=None , options=None)
        content_image = self.load_image(content)
        style_image = self.load_image(style)
        stylized_image = model(tf.constant(content_image), tf.constant(style_image))[0]
        return stylized_image


    def save_img(self , stylized_image , save_name) : 
        cv2.imwrite(f'results/{save_name}.jpg', cv2.cvtColor(np.squeeze(stylized_image)*255, cv2.COLOR_BGR2RGB))