## Installation

    git clone --recursive git@gitlab.com:joejeffcock/deepsort_pytorch.git
    pip install torch torchvision future numpy filterpy pillow
    apt-get install python-skimage

Download the weights and place them in the root folder `deepsort_pytorch`

## Weights

Download at: https://leeds365-my.sharepoint.com/:f:/g/personal/sc18j3j_leeds_ac_uk/EoD0zTa-R4xOo5OBoveM6PsBHthDbDxDPHQG3tJPT2GUqA?e=HqnNl1

ONNX model included for use with OpenCV DNN.

## Results

Both the original SORT algorithm and the added deep appearance metric were tested using max_age=30 on the 2DMOT2015 benchmark, with the results tabulated below.

ID switching was reduced by approximately 30% as a result of the deep appearance metric, along with a slight increase in accuracy and precision.

### Original SORT algorithm results

|              | IDF1|  IDP|  IDR| Rcll| Prcn| GT| MT| PT| ML|  FP|   FN|IDs|   FM| MOTA| MOTP|IDt|IDa|IDm|
| ---          | --- | --- | --- | --- | --- |---|---|---|---| ---| --- |---| --- | --- | --- |---|---|---|
|ADL-Rundle-6  |46.5%|54.4%|40.5%|56.5%|75.8%| 24|  6| 16|  2| 903| 2180| 64|  111|37.2%|0.250| 31| 30|  2|
|ETH-Sunnyday  |73.2%|75.4%|71.0%|76.7%|81.4%| 30| 10| 17|  3| 326|  433| 20|   61|58.1%|0.258|  8| 14|  2|
|TUD-Campus    |71.7%|85.4%|61.8%|68.0%|93.8%|  8|  5|  3|  0|  16|  115|  2|   15|63.0%|0.261|  1|  2|  1|
|ADL-Rundle-8  |34.6%|47.9%|27.1%|43.0%|75.9%| 28|  5| 15|  8| 928| 3867|106|  248|27.7%|0.289| 39| 63|  7|
|PETS09-S2L1   |42.2%|45.8%|39.0%|74.8%|87.9%| 19|  6| 13|  0| 462| 1127| 77|  198|62.8%|0.323| 21| 49|  1|
|TUD-Stadtmitte|79.9%|92.4%|70.4%|74.3%|97.5%| 10|  6|  4|  0|  22|  297| 11|   19|71.5%|0.249|  4|  7|  1|
|KITTI-13      |36.3%|53.2%|27.5%|34.6%|66.9%| 42|  1| 23| 18| 109|  416| 25|   27|13.5%|0.319|  8| 20|  4|
|Venice-2      |41.1%|52.6%|33.8%|42.4%|66.0%| 26|  8| 10|  8|1559| 4115| 45|  118|19.9%|0.264| 12| 33|  5|
|ETH-Pedcross2 |55.0%|76.3%|43.0%|50.9%|90.4%|133| 16| 60| 57| 337| 3074| 82|  133|44.2%|0.251| 39| 49| 19|
|KITTI-17      |71.7%|86.2%|61.3%|66.3%|93.2%|  9|  1|  8|  0|  33|  230|  8|   16|60.3%|0.276|  4|  5|  1|
|ETH-Bahnhof   |54.9%|60.6%|50.1%|63.3%|76.5%|171| 44| 71| 56|1053| 1989| 81|  177|42.3%|0.258| 72| 43| 46|
|OVERALL       |48.6%|59.2%|41.2%|55.1%|79.2%|500|108|240|152|5748|17843|521| 1123|39.4%|0.271|239|315| 89|

### My bootleg Deep SORT results

|              | IDF1|  IDP|  IDR| Rcll| Prcn| GT| MT| PT| ML|  FP|   FN|IDs|   FM| MOTA| MOTP|IDt|IDa|IDm|
| ---          | --- | --- | --- | --- | --- |---|---|---|---| ---| --- |---| --- | --- | --- |---|---|---|
|ADL-Rundle-6  |44.0%|50.9%|38.7%|57.6%|75.8%| 24|  6| 16|  2| 921| 2126| 46|  107|38.3%|0.251| 30| 17|  3|
|ETH-Sunnyday  |76.0%|77.0%|75.1%|78.8%|80.8%| 30| 12| 15|  3| 348|  394| 12|   52|59.4%|0.258|  5|  9|  3|
|TUD-Campus    |74.4%|88.8%|64.1%|67.4%|93.4%|  8|  3|  5|  0|  17|  117|  1|   16|62.4%|0.259|  1|  1|  1|
|ADL-Rundle-8  |37.0%|49.5%|29.6%|45.0%|75.3%| 28|  9| 14|  5| 999| 3733| 72|  233|29.2%|0.289| 31| 39|  8|
|PETS09-S2L1   |55.3%|59.3%|51.7%|76.0%|87.1%| 19|  9| 10|  0| 502| 1075| 56|  190|63.5%|0.322| 21| 27|  1|
|TUD-Stadtmitte|78.1%|90.1%|68.9%|74.6%|97.4%| 10|  6|  4|  0|  23|  294|  8|   15|71.9%|0.248|  4|  5|  1|
|KITTI-13      |52.1%|64.6%|43.7%|47.7%|70.5%| 42|  2| 32|  8| 140|  366|  8|   24|26.6%|0.324|  5|  7|  4|
|Venice-2      |44.8%|56.2%|37.2%|42.8%|64.8%| 26|  8| 10|  8|1662| 4083| 32|  116|19.1%|0.265| 13| 20|  4|
|ETH-Pedcross2 |57.7%|78.4%|45.7%|51.9%|89.0%|133| 16| 61| 56| 400| 3014| 66|  127|44.4%|0.253| 45| 30| 22|
|KITTI-17      |73.3%|87.3%|63.3%|67.3%|92.9%|  9|  1|  8|  0|  35|  223|  7|   18|61.2%|0.280|  4|  3|  1|
|ETH-Bahnhof   |55.5%|60.1%|51.7%|64.9%|75.4%|171| 52| 67| 52|1144| 1900| 55|  165|42.8%|0.260| 74| 26| 53|
|OVERALL       |51.7%|61.8%|44.5%|56.5%|78.4%|500|124|242|134|6191|17325|363| 1063|40.1%|0.273|233|184|101|

## Webcam test
### Requirements

- OpenCV minimum version 4.0.0
- YOLOv3 COCO .weights, .cfg and classes.txt from https://pjreddie.com/darknet/yolo/

### Setup
    cd webcam-test
    mkdir YOLOv3
    cd YOLOv3
    ln -s <path to yolov3.weights, yolov3.cfg, classes.txt>/* ./