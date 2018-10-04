import keras
from keras.models import load_model
import tensorflowjs as tfjs

overall_model = load_model('./tl_iminet_keras_version.h5')
tfjs.converters.save_keras_model(overall_model, './tl-iminet/')
print('Done!')