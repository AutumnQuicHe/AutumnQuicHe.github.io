# hugo

不低于`v0.90.0`版本。

## 编译

自己编译hugo以免出错。

获取代码：
> git clone https://github.com/gohugoio/hugo.git

编译：
> go build

> ./hugo version

将`hugo`执行文件移到`/usr/local/bin/`或其他`${PATH}`中的目录。

## 编译执行工程

> git submodule update --init

> ./build.sh

调试：
> ./scripts/sass.py && hugo server

通过[http://localhost:1313/](http://localhost:1313/)访问。

# sass

## 安装sass

> apt update && apt install npm

> npm install -g sass

## 生成css文件
> ./scripts/sass.py
