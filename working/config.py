import torch

WANDB = True
NUM_IMAGES_3D = 64
TRAINING_BATCH_SIZE = 8
TEST_BATCH_SIZE = 8
IMAGE_SIZE = 112
N_EPOCHS = 15
do_valid = True
n_workers = 0
NFOLDS = 5
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")