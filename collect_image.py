import cv2
import os
import numpy as np
#采集物体4张曝光度不同的图像，然后旋20次，每次18°
def Collect_Datasets():
    # 创建文件夹
    if not os.path.exists('raw'):  #原始4张曝光度图片存放路径
        os.makedirs('raw')
    if not os.path.exists('out'):  #旋转后生成图片的路径
        os.makedirs('out')
    image_name = input("请输入物体名称：")  #给拍摄物体命名
    if not os.path.exists(image_name):
        os.makedirs(f'data/train/{image_name}')  #把物体数据集存放到data/tarin文件夹
#采集物体4张曝光度不同的图像        
    # 调用摄像头拍摄1张图片
    cap = cv2.VideoCapture(1)
    ret, frame = cap.read()
    cap.release()
    # 灰度化
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # 获取图像宽度和高度
    height, width = gray_frame.shape
    # 保存第一张灰度图片到raw文件夹
    cv2.imwrite('raw/exposure_1.jpg', gray_frame)
    # 生成其他3张曝光度不同的图片
    for i in range(3):
        exposure_adjusted = cv2.convertScaleAbs(gray_frame, alpha=(i+1)*0.65, beta=0)
        cv2.imwrite(f'raw/exposure_{i+2}.jpg', exposure_adjusted)  #其他3张不同曝光度的图片也存放到raw文件夹

#旋转图片
    for i in range(20):
        angle = i * 18  # 每次旋转18°
        for j in range(4):
            image_path = f'raw/exposure_{j+1}.jpg'  #给旋转的图片命名
            img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)  #读取raw文件夹内图片
            #cv2.getRotationMatrix2D()函数用于获取图像旋转的变换矩阵
            #获取一个变换矩阵 M，该矩阵可以将图像围绕 (width/2, height/2) 旋转 angle 度
            M = cv2.getRotationMatrix2D((width/2, height/2), angle, 1)
            rotated = cv2.warpAffine(img, M, (width, height))    #对图像进行旋转操作
            out_path = f'data/train/{image_name}/{image_name}_{i*4+j+1}.jpg'  #图片存放路径，存放到以你为物体命的名的文件夹
            cv2.imwrite(out_path, rotated)
#拍摄一张需要验证的物体图像，用于训练完验证时候使用
def Verify_Image():
    print("拍摄一张图片验证数据集！")
    cap = cv2.VideoCapture(1)
    ret, frame = cap.read()
    cv2.imshow("image", frame)
    print("关闭窗口即拍摄结束！")
    cv2.waitKey()# 等待按键触发
    cap.release()
    # 灰度化
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # 保存灰度图片
    cv2.imwrite('image/image.jpg', gray_frame)

if __name__ == "__main__":
    collect_picture = input("请输入数字：1.采集数据集 2.采集一张验证:")
    if collect_picture == "1":
        Collect_Datasets()  #制作数据集
    elif collect_picture == "2":
        Verify_Image()  #验证时采集一张图片的时候调用
