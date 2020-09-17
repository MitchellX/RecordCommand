# testImage
this repository is used to display image file on the remote server for client

# Git Command

## download：
    git clone https://github.com/MitchellX/testImage.git
    
无用的：
    mkdir yourFileName
    cd /yourFileName
    git init

## upload：
    git add .        （注：别忘记后面的.，此操作是把Test文件夹下面的文件都添加进来
    git commit  -m  "提交信息"  （注：“提交信息”里面换成你需要，如“first commit”）
    git push -u origin master   （注：此操作目的是把本地仓库push到github上面，此步骤需要你输入帐号和密码）

## update--(git强制覆盖)：
    git fetch --all
    git reset --hard origin/master
    git pull

## delete:
    git reset --hard HEAD^ 可以将本地的仓库回滚到上一次提交时的状态，HEAD^指的是上一次提交。

# git强制覆盖本地命令（单条执行）：

    git fetch --all && git reset --hard origin/master && git pull


 git 删除远程分支上的某次提交
    git revert HEAD
    git push origin master
    删除最后一次提交，但是查看git log 会有记录
    
# Linux Common Command
    mv A B      file/ folder rename文件重命名
    ctrl + z    退出当前进程
https://blog.csdn.net/u011630575/article/details/48288663

    fg          回到上一个进程
    bg          将一个在后台暂停的命令，变成继续执行。如果后台中有多个命令，可以用bg %jobnumber将选中的命令调出
    jobs -l     查看当前所有进程，并显示pid
    kill pid    杀死pid进程
    
## 监控GPU使用情况
    gpustat     最简单的
    watch -n 0.1 nvidia-smi   实时监控 -n设置间隔
    
## 释放GPU一直占用的显存
    fuser -v /dev/nvidia*   查看当前系统中GPU占用的线程
    nvidia-smi              也能查看pid
    kill -9 pid             结束进程
## pytorch查看tensor大小
    import sys
    sys.getsizeof(input.storage())      单位byte B
    
## pytorch查看Net model详情
    print('model.__len__(): %d layers' % model.__len__())
    print(f'model.__len__(): {model.__len__()} layers')

    # U-net(5, 64) memory usage
    param_count = sum(p.storage().size() for p in model.parameters())
    param_size = sum(p.storage().size() * p.storage().element_size() for p in model.parameters())
    param_scale = 2  # param + grad

    print(f'# of Model Parameters: {param_count:,}')
    print(f'Total Model Parameter Memory: {param_size * param_scale:,} Bytes')
    
## View继承nn.Module，这样即可放入nn.Sequential()中了
在接入全连接层前，一般都需要一个打平的操作放在nn.Sequential里面，因此需要自己写一个打平的类继承自nn.Module.以上便是代码，特记录之。

    class View(nn.Module):
    def __init__(self):
        super(View, self).__init__()
    def forward(self, x):
        return x.view(x.size[0], -1)
        
## Conda环境复制的方法
前提是，在本地的conda里已经有一个叫AAA的环境，我想创建一个新环境跟它一模一样的叫BBB，那么这样一句就搞定了：

    conda create -n BBB --clone AAA
但是如果是跨计算机呢。查询conda create命令的原来说明，是这样的：

    –clone ENV
    Path to (or name of) existing local environment.    
–clone这个参数后面的不仅可以是环境的名字，也可以是环境的路径。所以，很自然地，我们可以把原来电脑上目标conda环境的目录复制到新电脑上，然后再用：

    conda create -n BBB --clone ~/path




