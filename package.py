import os

# build
os.system(r"pyinstaller.exe -wF --distpath .\bin\build --workpath .\bin\ -i .\images\Logo.ico .\main.py -n 字频频率统计")

if not os.path.exists("./bin/build/images"):
    os.makedirs("./bin/build/images")
os.system(r"copy .\images\Logo.ico .\bin\build\images\Logo.ico")