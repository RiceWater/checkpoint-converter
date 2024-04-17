#==================#
#    HOW TO USE    #
#==================#
- create folders for storign checkpoints and results to prevent messy structure
- Go to Neptune AI and download the model.keras file
- Go to the platform where it was trained
- Upload the model
- Load it using  tf.keras.models.load_model("PATH_TO_MODEL.keras")
- Use model.save_weights()
- Zip the weights
- Put it in the corresponding folder in this venv

#===============#
#    PURPOSE    #
#===============#

This venv is for converting checkpoints into keras models our API can use. Due to the libraries and packages on Kaggle,
as well as its OS (Linux), it cannot directly load keras models that were created in the Kaggle notebook. After delving why,
it is because tensorflow cannot load models, keras; h5, in different versions. 

After researching, I tried to save the weights of the model, zipped it, downloaded it, and loaded it in this venv which has
the same libraries as the Flask API. Thankfully, the SavedModel format was backward-compatible with the specific versions I had
and the versions Kaggle has.


#===============#
#    SOURCES    #
#===============#

- https://www.tensorflow.org/tutorials/keras/save_and_load#manually_save_weights 
- https://colab.research.google.com/github/tensorflow/docs/blob/master/site/en/tutorials/keras/save_and_load.ipynb
- https://www.tensorflow.org/guide/versions#compatibility_of_savedmodels_graphs_and_checkpoints
- https://stackoverflow.com/questions/77353981/layer-conv2d-11-expected-2-variables-but-received-0-variables-during-loading
