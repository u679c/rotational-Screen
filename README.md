# rotational-Screen

### macOS 副屏旋转控制

使用python编写esp32固件向局域网设备发送信号，

屏幕控制核心原理是使用开源包==displayplacer==



### 使用步骤：

1. 首先修改boot.py中的这两个参数

<img src="/Users/u679c/Desktop/截屏2024-03-09 下午11.48.44.png" alt="截屏2024-03-09 下午11.48.44" style="zoom:30%;" /> 

2. 修改好后将boot.py烧录进esp32中的boot作为开机启动程序（烧录教程b站都有随便找一个跟着做即可）

3. 通过终端下载包 brew install jakehilborn/jakehilborn/displayplacer

   https://github.com/jakehilborn/displayplacer.git  <==  ==开源包地址里面有详细使用说明==

4. 在电脑上运行main.py

5. 也可使用==nohup python3.11 ./main.py > log.log 2>&1 &==在后台运行

6. 短接gnd和D4引脚即可发送socket信息，也可根据自己需求改代码改引脚

   <img src="/Users/u679c/Downloads/IMG_3720.jpg" alt="IMG_3720" style="zoom:10%;" /> 

7. 根据自己需求可以更改main.sh代码，屏幕控制指令在https://github.com/jakehilborn/displayplacer.git
