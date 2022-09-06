## 注意事项：
[1].默认不适用upx打包，因为使用upx打包后，win11系统打开软件明显缓慢！

[2].使用upx打包教程：

修改 `package.py` 的第4行 `use_upx = False` 改为 `use_upx = True`，第6行的upx目录手动修改为自己的upx目录！


## pyinstaller打包

`python package.py`

## 使用
`cd .\bin\build\`

`.\main.exe`