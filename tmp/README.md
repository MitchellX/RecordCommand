## 人脸解析Face Parsing Python API

### requirements
    python 2.7 (or 3.6)
    pytorch==0.4.1
    Pillow > 5.3.0


### 1. 目录结构
    prds/  主要代码
    assets/ 
        models/ 模型文件
        configs/  配置文件
    test/  离线测试脚本 + Flask client/server + 测试图片list
    images/  输入测试图片
    results/  输出结果:　masked的脸部图片 


### 2. 使用方法

#### 2.1 第一次需要build dependency
```
cd ./prds/modules
sh build.sh
python build.py
```


#### 2.2 offline test
    代码:
        test_offline_FaceParser.py
    输入Parameter: 
        list_file: a file contains images list
        img_dir: the path of the test image
        res_folder: the result directory

#### 2.3 HTTP Flask test
    server端:
        test_server.py
    client端:
        test_client.py
    输入Parameter: 
        list_file: a file contains images list
        img_dir: the path of the test image
        res_folder: the result directory
        batch_size: how many images in a batch


#### 2.4 Docker test
     Docker 下载:
		```docker pull ai-image.jd.com/nzhang/cuda9.0_caffe_tf_gpu:pytorch0.4.1_ning```
     Docker 启动:
		```
		docker run -it --gpus all --rm -p 5000:5000 --user "$(id -u):$(id -g)" -v /home/nzhang/CV_api_online/face_parser_py_api/:/home/nzhang ai-image.jd.com/nzhang/cuda9.0_caffe_tf_gpu:pytorch0.4.1_ning /bin/bash
		```
     Docker端:
		python test_server.py
     clinet端:	
		python test_client.py  
### 3. 内部算法逻辑
    现有模型支持两种人脸解析方式，调用在config->MIRROR:
        True: 输入图片会进行左右翻转的处理，与原图一起进行前置inference. 因为本算法在pixel-level上的segmentation,
        　　　　使用MIRROR, 会增强parsing的准确度
        False:　输入图片无左右翻转,单图进行前置inference.
    
### 4. sdk返回结果
    结果返回为两个与input输入image相同大小的(1)Mask图 (2)着色后效果图:
        image.png: Mask图，将分割出的人脸各个部分以此表代码形式存储于Mask图中。Mask词表见下.
        image_vis.png: 利用固定调色盘颜色进行人脸各个部分Mask图的调色。调色盘(palette)见下.
    如果input输入图不符合规范无法进行decode，　结果返回为ERROR_image.txt:
        ERROR_image.txt: 文档内会给出错误原因


### 5. 评估用法及使用范围
    1. 为获得最优分割效果，场景为单人头像，而且头部需在输入图片的中间部分，并占比至少50%以上。
    2. 多人头像或占比较低的场景效果不能保证最优.如有需要可以考虑与脸部检测(Face Detection)联合使用。

### 6. 人脸各个部分对应Mask及其调色盘(palette)
| Mask Index |  Face Parts    | Palette RGB  |
|:----------:| ------------- |:---------------:|
0　| 'background'|[0, 0, 0]
1 | 'face_skin' | [0, 153, 255]
2 | 'left_eyebrow' |[102, 255, 153]
3 | 'right_eyebrow' | [0, 204, 153]
4 | 'left_eye' | [255, 255, 102]
5 | 'right_eye' | [255, 255, 204]
6 | 'nose' | [255, 153, 0]
7 | 'upper_lip' | [255, 204, 255]
8 | 'inner_mouth' | [102, 0, 51]
9 | 'lower_lip' | [255, 102, 255]
10| 'hair' | [255, 0, 102]

