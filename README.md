In this example, you will get used to a lot of techniques, from training a model 
(Text Detection) to implement an ML service with cache, preloaded model, along with callback and websocket architectural styles.

## Training CRAFT

In this section, you will train a text detection model, which will be used further as a component in EasyOCR, which is an end-to-end OCR pipeline. 

The dataset used for training was taken from [this](https://github.com/manhph2211/BKAI-Challenge-Vietnamese-OCR/tree/main#chu%E1%BA%A9n-b%E1%BB%8B-d%E1%BB%AF-li%E1%BB%87u) awesome github repository.

To start training, you will run the following commands:
```shell
cd craft
CUDA_VISIBLE_DEVICES=0 python3 train.py --yaml=custom_data_train
```

**Note:** 
- Remember to install all the necessary libraries before training.
- This code requires GPU for training, you can make use of https://colab.google/ for this.

## Serving models

The model after being trained, i.e, `craft_mlt_25k.pth` should be saved in to `./model_storage/model` due to EasyOCR configuration,
after that, you can start your server as usual by running the following commands:

```shell
uvicorn main:app --host 0.0.0.0 --port 8081
```

or these commands for preloaded model
```shell
uvicorn main_preloaded:app --host 0.0.0.0 --port 8081
```