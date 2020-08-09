## Installation

    git clone --recursive git@gitlab.com:joejeffcock/deepsort_pytorch.git
    pip install torch torchvision future numpy filterpy pillow
    apt-get install python-skimage

Download the weights and place them in the root folder `deepsort_pytorch`

## Weights

Download at: https://leeds365-my.sharepoint.com/:f:/g/personal/sc18j3j_leeds_ac_uk/EoD0zTa-R4xOo5OBoveM6PsBHthDbDxDPHQG3tJPT2GUqA?e=HqnNl1

## Results

Both the original SORT algorithm and the added deep appearance metric were tested using max_age=30 on the 2DMOT2015 benchmark, with the results tabulated below.

ID switching was reduced by approximately 23% as a result of the deep appearance metric, along with a slight increase in accuracy and precision.

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
|ADL-Rundle-6  |44.0%|50.8%|38.8%|57.8%|75.8%| 24|  6| 16|  2| 924| 2112| 49|  109|38.4%|0.251| 31| 17|  3|
|ETH-Sunnyday  |74.1%|74.9%|73.3%|78.5%|80.2%| 30| 10| 17|  3| 359|  400| 14|   61|58.4%|0.260|  9|  9|  4|
|TUD-Campus    |75.8%|89.4%|65.7%|69.1%|93.9%|  8|  5|  3|  0|  16|  111|  1|   14|64.3%|0.261|  1|  1|  1|
|ADL-Rundle-8  |32.6%|43.7%|26.0%|44.9%|75.4%| 28|  7| 16|  5| 993| 3740| 90|  240|28.9%|0.291| 37| 52| 10|
|PETS09-S2L1   |55.7%|59.8%|52.1%|76.2%|87.4%| 19|  9| 10|  0| 491| 1067| 50|  190|64.1%|0.322| 16| 24|  1|
|TUD-Stadtmitte|80.1%|92.3%|70.8%|74.6%|97.3%| 10|  6|  4|  0|  24|  294|  7|   15|71.9%|0.247|  3|  5|  1|
|KITTI-13      |52.2%|64.0%|44.1%|46.8%|67.9%| 42|  2| 32|  8| 156|  375| 13|   30|22.8%|0.324|  8|  9|  5|
|Venice-2      |42.4%|53.4%|35.1%|42.6%|64.7%| 26|  8| 11|  7|1656| 4100| 32|  114|18.9%|0.264| 11| 21|  4|
|ETH-Pedcross2 |57.8%|78.0%|45.9%|52.1%|88.4%|133| 16| 63| 54| 426| 3002| 70|  126|44.1%|0.253| 49| 35| 25|
|KITTI-17      |72.2%|85.3%|62.7%|67.3%|91.6%|  9|  2|  7|  0|  42|  223|  8|   17|60.0%|0.277|  3|  5|  1|
|ETH-Bahnhof   |56.3%|60.5%|52.6%|65.2%|75.0%|171| 47| 71| 53|1179| 1887| 65|  172|42.2%|0.260| 83| 29| 60|
|OVERALL       |50.8%|60.5%|43.7%|56.6%|78.2%|500|118|250|132|6266|17311|399| 1088|39.8%|0.273|251|207|115|

## Webcam test
### Requirements

- OpenCV minimum version 4.0.0
- YOLOv3 COCO .weights, .cfg and classes.txt from https://pjreddie.com/darknet/yolo/

### Setup
    cd webcam-test
    mkdir YOLOv3
    cd YOLOv3
    ln -s <path to yolov3.weights, yolov3.cfg, classes.txt>/* ./