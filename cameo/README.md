### Cameo

All code is from the book 《Learning OpenCV 3 Computer Vision with Python》second Edition.

run on ubutnu16.0,raspberrypi3B+/python3.x/opencv3.x

#### Function:

- capture camera's frame
- filter the frame
- show the result
- screenshot/screencast
-
#### 修改后的功能和使用方法

**安装依赖**
```shell
pip3 install opencv-python
pip3 install numpy
python3 cameo.py
```

**功能**

> 可以用来在户外进行图像数据采集，默认每5帧记录一张图片，按编号保存在工作目录。
> ctrl+z暂停;fg继续执行
> tab 开始/停止记录视频
> space空格键截屏
> esc 退出
