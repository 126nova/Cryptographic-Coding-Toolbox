# Cryptographic Coding Toolbox（加密编码工具箱）
你可以在这个小工具中将一些常见的加密编码进行加密与解密

---

## 支持的加密编码包含：
| 编码昵称/支持功能 | 加密 | 解密 |
| :---------------: | :--: | :--: |
|      base16       |  √   |  √   |
|      base32       |  √   |  √   |
|      base64       |  √   |  √   |
|      base85       |  √   |  √   |
|        BIN        |  √   |  √   |
|        OCT        |  √   |  √   |
|        HEX        |  √   |  √   |
|      Caesar       |  √   |  √   |

## 支持的语言有：
zh-cn（简体中文）

zh-hk（繁体中文）

## 打包教程：

###### tips：请使用python3或以上版本

### 方法1：

#### 使用[“cx_Freeze”]([cx-Freeze · PyPI](https://pypi.org/project/cx-Freeze/))库进行打包python文件，在命令提示符（cmd）中输入：

```
pip install cx_Freeze
```
#### 接着输入用cd定位到项目位置

```
cd 项目位置
```

#### 最后输入打包指令并把依赖文件复制到打包文件夹里

```
python setup.py build
```

### 方法2：

可以直接运行`build.bat`文件进行快捷打包，但是要把复制依赖文件的路劲改成自己打包到的文件夹

（你还可以通过更改”setup.py“文件来更改打包文件的参数）

## 工具特色

- 简洁ui界面

- 可自由选择加密编码
- 多功能

## 联系方式

如果出现bug，请发邮件给***silver03@qq.com***邮箱:)

欢迎关注[作者的哔哩哔哩]([Silver03_的个人空间_哔哩哔哩_bilibili](https://space.bilibili.com/2043795963))！
