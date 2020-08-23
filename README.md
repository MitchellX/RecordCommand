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

git强制覆盖本地命令（单条执行）：

    git fetch --all && git reset --hard origin/master && git pull


## git 删除远程分支上的某次提交
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
    kill -9 pid             结束进程
