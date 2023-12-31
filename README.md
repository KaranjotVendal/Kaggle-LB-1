
# RSNA-MICCAI Brain Tumor Radiogenomic Classification

## Hardware/OS used for the competiion
- CPU: Intel i9-12900K
- GPU: RTX 3060
- RAM: 64GB
- OS: Windows 10

## Kaggle resources

[The Kaggle competition link](https://www.kaggle.com/c/rsna-miccai-brain-tumor-radiogenomic-classification)

[Competition data](https://www.kaggle.com/c/rsna-miccai-brain-tumor-radiogenomic-classification/data)

[Solution Kaggle discussion](https://www.kaggle.com/c/rsna-miccai-brain-tumor-radiogenomic-classification/discussion/281347)

[Inference notebook](https://www.kaggle.com/rinnqd/monai-simple-prediction-from-flair)

## Training steps

To train the model using the competition data, please follow these steps:
 
1. Clone this repo
2. Install dependencies via `pip install -r requirements.txt`
3. Download the competition data from [here](https://drive.google.com/file/d/1b1cbJojNYjCLrxbz0KG8ca3tiYPt_3B0/view?usp=sharing) and place the downloaded files in the `input` folder.
   - [train labels](https://drive.google.com/file/d/1rCqwfbEKd9ICnRhwwq5H81ZHfYos0Yex/view?usp=drive_link)
4. Set the configuration file `working/config.py`. It is recommended to use the default values.

    * TRAINING_BATCH_SIZE: The training batch size
    * TEST_BATCH_SIZE: The testing/validation batch size
    * IMAGE_SIZE: The image size used during the training/infernece
    * N_EPOCHS: The number of the training epochs
    * NUM_IMAGES_3D: Number of the images/scans used to build the 3D images.
    * do_valid: bool that indicates if we want to save the model weights based on the validation score
    * n_workers: Number of workers used during the training

5. In case you want to use the pretrained weights from the final kaggle solution please skip the training step (next step). You will find the pretrained weights in `weights/`
6. Run training script `python ./working/train.py`

If you have any questions, please don't hestiate to reach out to me on this email: karanjotvendal@gmail.com

## ORIGINAL Authors

- [@FirsaBaba](https://github.com/FirasBaba/rsna-resnet10)
firas.baba96@gmail.com