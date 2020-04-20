# some training parameters
EPOCHS = 40
BATCH_SIZE = 16
NUM_CLASSES = 20
IMAGE_WIDTH = 224
IMAGE_HEIGHT = 224
CHANNELS = 2
save_model_dir = "saved_model/"
save_every_n_epoch = 4
dataset_dir = "dataset/"
train_dir = dataset_dir + "train"
valid_dir = dataset_dir + "valid"
test_dir = dataset_dir + "test"
train_tfrecord = dataset_dir + "train.tfrecord"
valid_tfrecord = dataset_dir + "valid.tfrecord"
test_tfrecord = dataset_dir + "test.tfrecord"
TRAIN_SET_RATIO = 0.8
TEST_SET_RATIO = 0.2
# VALID_SET_RATIO = 1 - TRAIN_SET_RATIO - TEST_SET_RATIO
model_index = 1