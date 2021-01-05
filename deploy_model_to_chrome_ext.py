"""

"""
import argparse

import tensorflowjs as tfjs
import tensorflow as tf


def convert(input_path, output_path):
    model = tf.keras.models.load_model(input_path)
    tfjs.converters.save_keras_model(model, output_path)


if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('-l', '--input_file', help='The input file (where h5 model stored')
    ap.add_argument('-u', '--output_file', help='The output file (where to save model.js')
    args = ap.parse_args()
    convert(input_path=ap.input_file, output_path=ap.output_file)
