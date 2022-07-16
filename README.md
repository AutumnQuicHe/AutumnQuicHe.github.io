# hugo

不低于`v0.90.0`版本。

## 编译hugo

自己编译hugo以免出错。

获取代码：
> git clone https://github.com/gohugoio/hugo.git

编译hugo：
> go build

> ./hugo version

将`hugo`执行文件移到`/usr/local/bin/`或其他`${PATH}`中的目录。

## 编译执行工程
安装其他依赖：
> apt update && apt install npm && npm install -g sass

> pip3 install beautifulsoup4 lxml html5lib

编译：
> git clone https://github.com/AutumnQuicHe/AutumnQuicHe.github.io

> cd AutumnQuicHe.github.io && git submodule update --init

> ./build.sh

编完结果在`public`目录。

## 调试
> ./scripts/sass.py && hugo server

通过[http://localhost:1313/](http://localhost:1313/)访问。

调试时无法将<p>块中多余的换行删掉，所以看起来有点怪。建议挂一个nginx指向`public`目录，直接通过执行`build.sh`更新结果。

# sass

## 安装sass

> apt update && apt install npm

> npm install -g sass

## 生成css文件
> ./scripts/sass.py

# 其他脚本

`./scripts/remove_p_linebreaks.py`用于清除<p>块中多余的空行，这些空行默认会变成空格，影响中文展示。
