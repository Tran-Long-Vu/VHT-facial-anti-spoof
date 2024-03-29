BATCH_SIZE = 8
LOSS = ""
LEARNING_RATE = 0.001
NO_EPOCHS = 50
DROPOUT = False
OPTIMIZER = "adam"
MODEL_BACKBONE= "rn18"
MODEL_NAME = 'rn18fas'
ATTACK_TYPE = 'printing'
a = 'data/datasets/CVPR23/train/living/000001/000001.jpg'
INFERENCE_DEVICE = 'CUDA'
TRAINING_DEVICE = 'CUDA'

TRAIN_DATASET = 'CVPR23'
VAL_DATASET = 'CVPR23'
TEST_DATASET = 'HAND_CRAWL'

PATH_TO_IMAGES = ''
PATH_TO_VIDEOS = ''
PATH_TO_SINGLE_VIDEO = ''
PATH_TO_TRAIN_DATASET = 'data/datasets/CVPR23/train/'
PATH_TO_TEST_DATASET = 'data/datasets/crawl_test/images/'
PATH_TO_VAL_DATASET = 'data/datasets/CVPR23/val/'
PATH_TO_STATE_DICT = 'model/rn18-fas-ckp.pth'
PATH_TO_SAVE_CHECKPOINT = 'checkpoints/'



PATH_TO_FAS_MODEL = './model/rn18-fas.onnx'
PATH_TO_FD_MODEL ='./model/scrfd.onnx'


