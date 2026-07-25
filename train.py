import os
import time
import torch
import torchvision
from torchvision import datasets, models, transforms
import matplotlib.pyplot as plt
import numpy as np
import copy
import glob
import shutil
import torch.nn as nn
import torch.optim as optim
from torch.optim import lr_scheduler


# 数据集存放路径
path = './data/'



# 数据集保存在百度网盘通过网盘分享的文件：数据集
# 链接: https://pan.baidu.com/s/1jxibI8Ydia2EWQpxg2-gDA 提取码: ei4w
#
#
#
#

# 遍历数据集
#将训练集数据中的数据随机抽取作为验证集数据，并将验证集数据复制到新建的文件夹中，以便于后续的模型训练和评估
for folder in os.listdir('./data/train'):
    # 图片格式为.jpg或.png
    jpg_files = glob.glob(os.path.join(path,"train", folder, "*.jpg"))
    png_files = glob.glob(os.path.join(path,"train", folder, "*.png"))
    files = jpg_files + png_files
    # 统计训练集数据
    num_of_img = len(files)
    print("Total number of {} image is {}".format(folder, num_of_img))
    # 从训练集里面抽取100%作为验证集,将训练集中的所有数据进行随机打乱，并计算出需要抽取的数据数量
    shuffle = np.random.permutation(num_of_img)
    percent = int(num_of_img * 1)
    print("Select {} img as valid image".format(percent) )
    # 新建val文件夹存放验证集数据
    path_val = os.path.join(path,"val",folder)
    if not os.path.exists(path_val):
        os.makedirs(path_val)
    # 把训练集里面抽取100%的数据复制到val文件夹
    # shuffle()方法将序列的所有元素随机排序
    for i in shuffle[:percent]:
        print("copy file {} ing".format(files[i].split('\\')[-1]))
        shutil.copy(files[i], path_val)

# 数据增强与变换

data_transforms = {
    # 训练集
    'train':transforms.Compose([
        transforms.Resize((224,224)),                                                                                           #调整输入图像的大小,以适应模型的输入尺寸
        transforms.Grayscale(3),                                                                                                #将输入图像转换为三通道的灰度图像，以便于在RGB模型上进行训练
        transforms.RandomRotation(5),   #对输入图像随机进行旋转
        transforms.RandomVerticalFlip(0.5),                                                                                     #对输入图像进行垂直翻转，增加模型对镜像变换的鲁棒性
        transforms.RandomHorizontalFlip(0.5),                                                                                   #对输入图像进行水平翻转，增加模型对镜像变换的鲁棒性
        transforms.ToTensor(),                                                                                                   #将输入图像转换为PyTorch张量
        transforms.Normalize([0.5,0.5,0.5], [0.5,0.5,0.5]) #对输入图像进行标准化处理 
    ]),
    # 测试集，同上
    'val':transforms.Compose([
        transforms.Resize((224,224)),
        transforms.Grayscale(3),
        transforms.RandomRotation(5),
        transforms.RandomVerticalFlip(0.5),
        transforms.RandomHorizontalFlip(0.5),
        transforms.ToTensor(), 
        transforms.Normalize([0.5,0.5,0.5], [0.5,0.5,0.5])  
    ])
}

# 加载数据
data_dir = './data/'
# 使用datasets.ImageFolder()方法加载数据集，并对训练集和验证集分别进行数据增强和变换操作
image_datasets = {x: datasets.ImageFolder(os.path.join(data_dir, x), data_transforms[x]) for x in ['train','val'] }
print(image_datasets)
# 使用torch.utils.data.DataLoader()方法构建训练集和验证集的数据迭代器
dataloaders = {x: torch.utils.data.DataLoader(image_datasets[x], 
                                              batch_size=len(os.listdir('./data/train')),  #batch_size参数表示每个批次的样本数量
                                              shuffle=True,  #shuffle参数表示是否对数据进行打乱
                                              num_workers=0) for x in ['train', 'val'] } #num_workers参数表示数据加载的并行数
print(dataloaders)
# 统计训练集和验证集的数据集大小
dataset_sizes = {x:len(image_datasets[x]) for x in ['train', 'val']}
print(dataset_sizes)
# 获取数据集的类别信息
class_names = image_datasets['train'].classes  
print(class_names)

# 判断GPU是否可用,如果当前计算机支持GPU，则使用GPU作为计算设备；否则使用CPU作为计算设备
device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
print(device)

# 通用训练模型函数,参数说明：模型、损失函数、优化器、学习率调度器、可选的训练轮数

def train_model(model, criterion, optimizer, scheduler, num_epochs=25):
    since = time.time() # 返回当前时间的时间戳
    # deepcopy为深拷贝,即创建一个新的对象，完全复制原始对象及其所有子对象。
    # model.state_dict是PyTorch中的一个方法，返回一个字典对象，将模型的所有参数映射到它们的张量值
    best_model_wts = copy.deepcopy(model.state_dict())
    best_acc = 0.0
    # 显示当前的训练进度
    for epoch in range(num_epochs):
        print('Epoch {}/{}'.format(epoch, num_epochs - 1)) # 输出训练进度
        print('-' * 10)
        # 每个epoch都有一个训练和验证阶段
        for phase in ['train', 'val']:
            if phase == 'train':
                # PyTorch中用于更新优化器的学习率
                scheduler.step()
                model.train()  # 设置模型的工作模式：训练模式，模型会更新参数
            else:
                model.eval()   # 设置模型的工作模式：评估模式，模型不会更新参数
            running_loss = 0.0  # 用于记录当前epoch的累计损失
            running_corrects = 0 # 用于记录当前正确分类的数量
            # 迭代数据
            for inputs, labels in dataloaders[phase]:
                # GPU加速,inputs、labels用于将输入数据和标签数据移动到指定的设备上，例如CPU或GPU
                inputs = inputs.to(device)
                labels = labels.to(device)
                # 清空梯度，在每次优化前都需要进行此操作
                optimizer.zero_grad()
                # torch.set_grad_enabled在训练模式下启用梯度计算，而在评估模式下禁用梯度计算
                with torch.set_grad_enabled(phase == 'train'):
                    outputs = model(inputs) 
                    _, preds = torch.max(outputs, 1) # 返回输入张量在指定维度上的最大值及其对应的索引
                    loss = criterion(outputs, labels)
                    # 后向 + 仅在训练阶段进行优化
                    if phase == 'train':
                        # 反向传播：根据模型的参数计算loss的梯度
                        loss.backward()
                        # 调用Optimizer的step函数使它所有参数更新
                        optimizer.step()
                running_loss += loss.item() * inputs.size(0) # 获取损失值和输入数据的数量
                running_corrects += torch.sum(preds == labels.data) # 记录当前epoch中正确分类的数量
            # dataset_sizes[phase]：该变量用于获取数据集在当前阶段中的大小
            epoch_loss = running_loss / dataset_sizes[phase]  #当前epoch的平均损失
            epoch_acc = running_corrects.double() / dataset_sizes[phase]  # 当前epoch的准确率
            # 打印当前epoch的损失和准确率，以实时监控模型的训练状态
            print('{} Loss: {:.4f} Acc: {:.4f}'.format(
                  phase, epoch_loss, epoch_acc)) # 前阶段的名称、当前epoch的平均损失、当前epoch的准确率
            if phase == 'val' and epoch_acc > best_acc:  #更新最佳模型参数
                best_acc = epoch_acc
                best_model_wts = copy.deepcopy(model.state_dict())
        print()
    time_elapsed = time.time() - since
    # 输出整个训练过程的时间
    print('Training complete in {:.0f}m {:.0f}s'.format(
        time_elapsed // 60, time_elapsed % 60))
    # 用于输出最佳验证准确率,best_acc是训练过程中被更新为模型在验证集上的最佳准确率
    print('Best val Acc: {:4f}'.format(best_acc))
    # 用于加载模型的状态字典，即将最佳模型的参数设置为给定的参数字典
    model.load_state_dict(best_model_wts)
    return model

# 主程序入口使用ResNet-18模型对图像进行分类，并训练模型并保存模型参数。		
if __name__ == "__main__":
    # 用于初始化ResNet-18 模型
    model_ft = torchvision.models.resnet18(pretrained=False)
    # 加载resnet18网络参数
    model_ft.load_state_dict(torch.load('./model/resnet18.pth'))
    # 提取fc层中固定的参数
    num_ftrs = model_ft.fc.in_features
    # 重写全连接层的分类
    model_ft.fc = nn.Linear(num_ftrs, len(os.listdir('./data/train')))
    model_ft = model_ft.to(device)
    # 这里使用分类交叉熵Cross-Entropy作为损失函数，动量SGD作为优化器
    criterion = nn.CrossEntropyLoss()
    # 初始化优化器
    optimizer_ft = optim.SGD(model_ft.parameters(), lr=0.001, momentum=0.9)
    # 每7个epochs衰减LR通过设置gamma = 0.1
    exp_lr_scheduler = lr_scheduler.StepLR(optimizer_ft, step_size=7, gamma=0.1)
    #调用通用训练模型的函数，返回训练得到的最佳模型


    model_ft = train_model(model_ft, criterion, optimizer_ft, exp_lr_scheduler, num_epochs=2)
    # 保存模型
    torch.save(model_ft.state_dict(), 'model/zhongyao.pkl')
