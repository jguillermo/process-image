import numpy as np
import tensorflow as tf

from sdk import utils
from sdk.vgg import vgg16

img1 = utils.load_image("./images/preguntas.jpeg")[:, :, :3]
img2 = utils.load_image("./images/laptop.jpeg")[:, :, :3]

batch1 = img1.reshape((1, 224, 224, 3))
batch2 = img2.reshape((1, 224, 224, 3))
batch = np.concatenate((batch1, batch2), 0)

with tf.Session() as sess:
    images = tf.placeholder("float", [2, 224, 224, 3])
    feed_dict = {images: batch}

    vgg = vgg16.Vgg16()
    with tf.name_scope("content_vgg"):
        vgg.build(images)

    prob = sess.run(vgg.prob, feed_dict=feed_dict)
    utils.print_prob_all(prob, './result/synset.txt')