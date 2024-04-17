import tensorflow as tf
from functions import convert_checkpoint

# Function:
# convert_checkpoint(params, checkpoint_path, model_name)

params = {
    "lr": 0.001,
    "epochs": 25,
    "batch_size": 8}

model_name="NAME-VERSION"

REMINDER = """ Update Model Structure first in the functions file!  
               Update Model Structure first in the functions file! 
               Update Model Structure first in the functions file! """

convert_checkpoint()




# OLD - no function to simplify code. Will use if there is an error with the latest update

# from functions import make_model, convert_checkpoint
# params = {
#     "lr": 0.001,
#     "epochs": 25,
#     "batch_size": 8}

# model = make_model(params)

# model_name = "Colab-Model-3CLS-NB"
# model.load_weights(f"colab_checkpoints\\test\\checkpoints\\test_model")

# model.summary()

# model.save("./{name}-converted.keras".format(name = model_name))




# OLDEST. Tried to use the same Tensorflow version and it's dependencies just like on Kaggle
# It did not work

# sm = tf.keras.models.load_model("C:\\Users\\user\\Documents\\Machine-Learning-Hub-1\\Tensorflow\\Final-B4_1_3.keras")
# Removed
# tensorflow-io-gcs-filesystem==0.35.0
# Can't find


# Trying
# tensorflow-io==0.35.0
# Can't find

# Trying to install available tensorflow-io version
# Found 0.31.0
# Did not work

