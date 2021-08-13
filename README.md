# Transfer Learning on Object Detection Models
Creating an object detector with Transfer Learning on a pre-trained model Using TensorFlow's Object Detection API

## Training Examples
* Example:- Transfer learning on ssd_mobilenet_v2_640x640 model to detect Mask, Face Sheild, Full Cover, Gloves, Goggles (using TF's Object Detection API)  
  I got a total loss < 0.25 after 4k steps (2 hrs of training).  
  
  
  PPE kit detector (ssd_mobilenet_v2):- [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/sid4sal/transfer-learning-on-object-detection-models/blob/main/Transfer_Learning_on_ssd_mobilenet_v2_ppe_dataset.ipynb)  
  * Total Loss plot:-  
    ![loss_ppe](https://github.com/sid4sal/images/blob/master/total_loss_ppe.png)
  * Predictions:-  
    ![ppe_detect1](https://github.com/sid4sal/images/blob/master/detect_img1.jpg)

* Example:- Transfer learning on ssd_mobilenet_v1_640x640 model to detect Guns (using TF's Object Detection API) | 4k steps (2 hrs of training).  

  Guns detector (ssd_mobilenet_v1):- [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/sid4sal/transfer-learning-on-object-detection-models/blob/main/Transfer_Learning_on_ssd_mobilenet_v1_guns_dataset.ipynb)  
  * Total Loss plot:-  
    ![loss_guns](https://github.com/sid4sal/images/blob/master/total_loss_guns.png)
  * Predictions:-  
    ![guns_detect2](https://github.com/sid4sal/images/blob/master/detect_2.jpg)  
    ![guns_detect3](https://github.com/sid4sal/images/blob/master/detect_3.jpg)  


## Layer Freezing Example
I trained the SSD_MobileNet_V1 model on the Guns dataset, with and without freezing the layers, and compared the results.

1) **no freeze 1** : without freezing the layers (Test 1)
2) **no freeze 2** : without freezing the layers (Test 2)
3) **4 freeze** : freezing first 4 FeatureExtractor Layers (up to Conv2d_4 block)
4) **8 freeze** : freezing first 8 FeatureExtractor Layers (up to Conv2d_8 block)
5) **all freeze** : freezing all the FeatureExtractor Layers
* **Layers :-**
```
'FeatureExtractor/MobilenetV1/MobilenetV1/Conv2d_0/add_fold',           #0
'FeatureExtractor/MobilenetV1/MobilenetV1/Conv2d_1_depthwise/add_fold', #1
'FeatureExtractor/MobilenetV1/MobilenetV1/Conv2d_1_pointwise/add_fold', #1
'FeatureExtractor/MobilenetV1/MobilenetV1/Conv2d_2_depthwise/add_fold', #2
'FeatureExtractor/MobilenetV1/MobilenetV1/Conv2d_2_pointwise/add_fold', #2
'FeatureExtractor/MobilenetV1/MobilenetV1/Conv2d_3_depthwise/add_fold', #3
'FeatureExtractor/MobilenetV1/MobilenetV1/Conv2d_3_pointwise/add_fold', #3
'FeatureExtractor/MobilenetV1/MobilenetV1/Conv2d_4_depthwise/add_fold', #4
'FeatureExtractor/MobilenetV1/MobilenetV1/Conv2d_4_pointwise/add_fold', #4  <--(4 freeze)
'FeatureExtractor/MobilenetV1/MobilenetV1/Conv2d_5_depthwise/add_fold', #5
'FeatureExtractor/MobilenetV1/MobilenetV1/Conv2d_5_pointwise/add_fold', #5
'FeatureExtractor/MobilenetV1/MobilenetV1/Conv2d_6_depthwise/add_fold', #6
'FeatureExtractor/MobilenetV1/MobilenetV1/Conv2d_6_pointwise/add_fold', #6
'FeatureExtractor/MobilenetV1/MobilenetV1/Conv2d_7_depthwise/add_fold', #7
'FeatureExtractor/MobilenetV1/MobilenetV1/Conv2d_7_pointwise/add_fold', #7
'FeatureExtractor/MobilenetV1/MobilenetV1/Conv2d_8_depthwise/add_fold', #8
'FeatureExtractor/MobilenetV1/MobilenetV1/Conv2d_8_pointwise/add_fold'  #8  <--(8 freeze)
```

### Average Per-step time :-  
  1) no freeze 1 :- 1.88 sec
  2) no freeze 2 :- 1.805 sec
  3) 4 freeze :- 0.828 sec
  4) 8 freeze :- 0.844 sec
  5) all freeze :- 0.845 sec

### Freezing 4 layers vs freezing 8 layers :-  
  ![4_freeze_vs_8_freeze](https://github.com/sid4sal/images/blob/master/4%20freeze%20vs%208%20freeze.png)  
  The graph is almost similar but the average per-step time is slightly lower for '4 freeze'.  
  Hence 'freeze 4' is slightly better than 'freeze 8'.

### Loss Vs Time Plot :-  
  ![Loss_vs_Time_Plot](https://github.com/sid4sal/images/blob/master/Loss%20vs%20Time%20Plot.png)  
  From the graph, we can conclude that 'freeze 4' is the best and 'no freeze 2' is the worst method.

### Best Vs Worst :-  
  ![best_vs_worst](https://github.com/sid4sal/images/blob/master/best%20vs%20worst.png)  

**Result : While Training SSD_MobileNet_V1 model on the Guns dataset, Freezing first 4 to 8 FeatureExtractor Layers performs best.**

* Data :- [![Open in Google Sheets](https://img.shields.io/badge/Freez_vs_No_Freez_Data-Google_Sheets-<COLOR>.svg)](https://docs.google.com/spreadsheets/d/1-4oCDiqYI8WThltOqmsLwxmmlTLOkSjCAZMhnsODoak/edit?usp=sharing)
* Github :- [![Open Github](https://img.shields.io/badge/Transfer_Learning_on_Object_Detection_Models-Github-<COLOR>.svg)](https://github.com/sid4sal/transfer-learning-on-object-detection-models)
