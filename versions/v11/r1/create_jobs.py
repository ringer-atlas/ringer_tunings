
from saphyra import *
import tensorflow as tf
from tensorflow.keras import layers



input  = layers.Input(shape=(1,), name = 'Input')
output = layers.Dense(1)(input)
model  = tf.keras.Model(input, output, name = "dummy")

create_jobs( models = [model],
        nInits        = 10,
        nInitsPerJob  = 1,
        sortBounds    = 10,
        nSortsPerJob  = 1,
        nModelsPerJob = 1,
        outputFolder  = 'job_config.Zee_v11.10sorts.10inits.r1' )

