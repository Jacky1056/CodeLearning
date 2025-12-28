# import os
# import time

# print("程式完整路徑：", __file__)  # 顯示程式完整路徑
# print("當前目錄：", os.getcwd())   # 顯示當前vscode目錄 '.'為當前目錄
# print("程式當前資歷夾：", os.path.dirname(__file__))

# folder_path = os.chdir(os.path.dirname(__file__))   # 切換工作目錄到程式所在資料夾

# for i in range(5):
#     new_folder_name = f"new_data_{i}"
#     try:
#         os.mkdir(new_folder_name)
#         print(f"成功建立：{new_folder_name}")
#     except Exception:
#         print(f"跳過：{new_folder_name} 已經存在了")

# print("目前目錄下的全部資料：", os.listdir(folder_path))   #列出目前資料夾檔案

# time.sleep(5)
# # 取得當前目錄	os.getcwd()
# # 列出資料夾檔案	os.listdir(path)
# # 建立資料夾	os.mkdir(path)
# # 刪除資料夾	os.rmdir(path)
# # 檢查檔案是否存在	os.path.exists(path)
# # 改名檔案	os.rename(src, dst)
# # 刪除檔案	os.remove(path)
# # 路徑拼接	os.path.join(dir, filename)
# for i in range(5):
#     folder_name = f"new_data_{i}"
#     try:
#         os.rmdir(folder_name)   # 如果在(C:) 會出現存取被拒錯誤
#         print(f"成功刪除：{folder_name}")
#     except Exception:
#         print(f"跳過：{folder_name} 刪除失敗")

# import os
# import time

# os.chdir(os.path.dirname(__file__))  # 切換到程式所在資料夾
# os.makedirs("a/b/c/d/e")  # 建立多層資料夾
# time.sleep(3)
# os.removedirs("a/b/c/d/e")  # 刪除多層資料夾
# with open("text.txt", 'w') as f:
#     f.write("Hello World\n")
# time.sleep(3)
# os.rename("text.txt", "DeleteMe!!!.txt")  # 改名檔案
# time.sleep(3)
# os.remove("DeleteMe!!!.txt")

# path = os.path.join("folder", "subfolder", "file.txt")   # 跨平台路徑拼接


#練習 完成檔案樹狀結構的繪圖
#ex:
# 資料夾 'TestFolder' 中的內容：
# [資料夾] Projects
#     [檔案] proj1.txt
#     [檔案] proj2.txt
#     資料夾數量：0
#     檔案數量：2
# [資料夾] Docs
#     [檔案] readme.md
#     資料夾數量：0
#     檔案數量：1
# [資料夾] Images
#     [資料夾] Images
#         [檔案] img1.png
#         [檔案] img2.png
#         資料夾數量：0
#         檔案數量：2
#     [檔案] img1.png
#     [檔案] img2.png
#     資料夾數量：0
#     檔案數量：2
# [檔案] todo.txt

# 統計結果：
# 總共資料夾數量：4
# 總共檔案數量：8

import os

class Counter:
    dcounter = 0
    fcounter = 0

def print_picture(folder, level):
    f_counter = 0
    d_counter = 0
    
    items = os.listdir(folder)
    if not len(items) == 0:
        for i in items:
            full_path = os.path.join(folder, i)
            if os.path.isfile(full_path):
                d_counter += 1
                Counter.dcounter += 1
                print(f"{"\t"*level}[檔案] {i}")
            else:
                f_counter += 1
                Counter.fcounter += 1
                print(f"{"\t"*level}[資料夾] {i}")
                print_picture(full_path, level+1)
    print(f"{"\t"*level}資料夾數量：{f_counter}")
    print(f"{"\t"*level}檔案數量：：{d_counter}")



folder = input("輸入資料夾路徑：")
print_picture(folder, 0)
print()
print(f"總共資料夾數量：{Counter.fcounter}")
print(f"總共檔案數量：{Counter.dcounter}")


