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

## update:
    git pull --rebase origin master   把最新的远程库同步到本地库

## delete:
    git reset --hard HEAD^ 可以将本地的仓库回滚到上一次提交时的状态，HEAD^指的是上一次提交。

## git强制覆盖：
    git fetch --all
    git reset --hard origin/master
    git pull

git强制覆盖本地命令（单条执行）：

    git fetch --all && git reset --hard origin/master && git pull


## git 删除远程分支上的某次提交
    git revert HEAD
    git push origin master
    删除最后一次提交，但是查看git log 会有记录
    
# Common Command
file/ folder rename:
    mv A B
