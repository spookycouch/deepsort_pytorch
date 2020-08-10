## Installation

    git clone --recursive git@gitlab.com:joejeffcock/deepsort_pytorch.git
    pip install torch torchvision future numpy filterpy pillow
    apt-get install python-skimage

Download the weights and place them in the root folder `deepsort_pytorch`

## Weights

Download at: https://leeds365-my.sharepoint.com/:f:/g/personal/sc18j3j_leeds_ac_uk/EoD0zTa-R4xOo5OBoveM6PsBHthDbDxDPHQG3tJPT2GUqA?e=HqnNl1

## Results

Both the original SORT algorithm and the added deep appearance metric were tested using max_age=30 on the 2DMOT2015 benchmark, with the results tabulated below.

ID switching was reduced by approximately 26% as a result of the deep appearance metric, along with a slight increase in accuracy and precision.

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
|ADL-Rundle-6  |47.8%|55.4%|42.0%|57.5%|75.7%| 24|  6| 16|  2| 925| 2131| 46|  106|38.1%|0.251| 25| 21|  4|
|ETH-Sunnyday  |75.9%|76.7%|75.0%|79.2%|81.0%| 30| 12| 15|  3| 346|  387| 11|   52|60.0%|0.258|  6|  7|  3|
|TUD-Campus    |75.3%|89.6%|64.9%|68.2%|94.2%|  8|  4|  4|  0|  15|  114|  1|   15|63.8%|0.261|  1|  1|  1|
|ADL-Rundle-8  |37.1%|50.1%|29.5%|44.9%|76.2%| 28|  8| 14|  6| 952| 3738| 72|  236|29.8%|0.291| 22| 50|  8|
|PETS09-S2L1   |52.5%|56.6%|49.0%|75.7%|87.4%| 19|  9| 10|  0| 488| 1088| 63|  196|63.4%|0.322| 20| 33|  1|
|TUD-Stadtmitte|79.9%|92.3%|70.5%|74.3%|97.3%| 10|  6|  4|  0|  24|  297|  9|   18|71.5%|0.248|  4|  5|  1|
|KITTI-13      |46.4%|56.6%|39.3%|46.3%|66.7%| 42|  2| 31|  9| 165|  382| 18|   37|20.6%|0.329| 13| 11|  6|
|Venice-2      |43.5%|54.6%|36.2%|43.0%|64.9%| 26|  8| 11|  7|1659| 4072| 33|  116|19.3%|0.266| 13| 21|  5|
|ETH-Pedcross2 |55.9%|75.6%|44.3%|52.0%|88.7%|133| 17| 60| 56| 415| 3008| 64|  133|44.3%|0.256| 49| 27| 23|
|KITTI-17      |70.9%|83.8%|61.5%|67.3%|91.8%|  9|  2|  7|  0|  41|  223|  6|   15|60.5%|0.276|  3|  4|  1|
|ETH-Bahnhof   |54.9%|59.2%|51.2%|65.7%|75.8%|171| 49| 66| 56|1133| 1857| 60|  165|43.7%|0.261| 82| 20| 56|
|OVERALL       |51.3%|61.2%|44.1%|56.6%|78.5%|500|123|238|139|6163|17297|383| 1089|40.2%|0.273|238|200|109|

## Webcam test
### Requirements

- OpenCV minimum version 4.0.0
- YOLOv3 COCO .weights, .cfg and classes.txt from https://pjreddie.com/darknet/yolo/

### Setup
    cd webcam-test
    mkdir YOLOv3
    cd YOLOv3
    ln -s <path to yolov3.weights, yolov3.cfg, classes.txt>/* ./