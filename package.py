import os

# upx
use_upx = False
# https://upx.github.io/
upx_path = r"D:\Byxs20\Downloads\Compressed\upx-3.96-win64" # 填入下载的upx目录

# config
app_name = "字频频率统计"
dist_path = "./bin/build"
work_path = "./bin"
ico_ptah = "./images/Logo.ico"

# build
os.system(f"pyinstaller.exe -wF -n {app_name} --distpath {dist_path} --workpath {work_path} -i {ico_ptah} --upx-dir {upx_path} .\main.py") if use_upx else os.system(f"pyinstaller.exe -wF -n {app_name} --distpath {dist_path} --workpath {work_path} -i {ico_ptah} .\main.py")

# copy ico file
if not os.path.exists("./bin/build/images"):
    os.makedirs("./bin/build/images")
os.system(r"copy .\images\Logo.ico .\bin\build\images\Logo.ico")