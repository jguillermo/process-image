import skimage
import skimage.io
import skimage.transform
import numpy as np
import tensorflow as tf
from sdk.vgg import vgg16


class ProcessImage:

    def __init__(self, image):
        self.image_path = image
        self.description_path = '/app/sdk/synset.txt'

    def process(self, top=3):
        img1 = self.load_image()[:, :, :3]
        batch = img1.reshape((1, 224, 224, 3))
        with tf.Session() as sess:
            images = tf.placeholder("float", [1, 224, 224, 3])
            feed_dict = {images: batch}
            vgg = vgg16.Vgg16()
            with tf.name_scope("content_vgg"):
                vgg.build(images)
            prob = sess.run(vgg.prob, feed_dict=feed_dict)
        return self.print_prob_all(prob, top)

    def load_image(self, scale=255, xrange=[0, 1]):
        # load image
        img = skimage.io.imread(self.image_path)
        img = img / scale
        assert (xrange[0] <= img).all() and (img <= xrange[1]).all()
        # print "Original Image Shape: ", img.shape
        # we crop image from center
        short_edge = min(img.shape[:2])
        yy = int((img.shape[0] - short_edge) / 2)
        xx = int((img.shape[1] - short_edge) / 2)
        crop_img = img[yy: yy + short_edge, xx: xx + short_edge]
        # resize to 224, 224
        resized_img = skimage.transform.resize(crop_img, (224, 224), mode='constant')
        return resized_img

    def print_prob_all(self, prob, top):
        synset = [l.strip() for l in open(self.description_path).readlines()]
        for i in range(len(prob)):

            _prob = prob[i]
            pred = np.argsort(_prob)[::-1]

            data = []
            if top > 0:
                for i in range(top):
                    data.append({
                        'item': synset[pred[i]][10:],
                        'percent': round(_prob[pred[i]] * 100, 2)
                    })
            return {
                'item': data[0]['item'],
                'list': data
            }
