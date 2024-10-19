# hugo

不低于`v0.120.0`版本。

## 编译hugo

自己编译hugo以免出错。
编译hugo前需要安装golang，请自行解决。
注意，应该升级golang到`1.21`及以上版本。

获取代码：
> git clone https://github.com/gohugoio/hugo.git -b master --depth=10

编译hugo：
> go build

> ./hugo version

将`hugo`执行文件移到`/usr/local/bin/`或其他`${PATH}`中的目录，或者使用go命令只接安装到go环境中：
> go install

## 编译执行工程
安装其他依赖：
> apt update && apt install npm && npm install -g sass

> pip3 install beautifulsoup4 lxml html5lib

编译：
> git clone https://github.com/AutumnQuicHe/AutumnQuicHe.github.io

> cd AutumnQuicHe.github.io && git submodule update --init

> ./build.sh

编完结果在`public`目录。

## 将编译结果提交到github.io站点并发布

由于github.io站点不是通过额外的仓库发布，而是以`gh-pages`分支发布，所以要将结果提交到该分支。
> mkdir public

> cd public

> git init && git remote add origin git@github.com:AutumnQuicHe/AutumnQuicHe.github.io.git

> git fetch origin gh-pages:gh-pacges --depth=10

> git checkout gh-pages

如此，就将`public`目录改造成能提交`gh-pages`分支的仓库了。如果`public`目录不空，则可能切分支这一步过不了。可以先执行`rm -rf *`清空目录再切分支。

> cd ..

> ./build.sh

> cd public

> git add *

> git commit -m "publish"

> git push origin gh-pages

## 调试
> ./scripts/sass.py && hugo server

通过[http://localhost:1313/](http://localhost:1313/)访问。

调试时无法将\<p\>块中多余的换行删掉，所以看起来有点怪。建议挂一个nginx指向`public`目录，直接通过执行`build.sh`更新结果。

# sass

## 安装sass

> apt update && apt install npm

> npm install -g sass

## 生成css文件
> ./scripts/sass.py

# 其他脚本

`./scripts/remove_p_linebreaks.py`用于清除\<p\>块中多余的空行，这些空行默认会变成空格，影响中文展示。
