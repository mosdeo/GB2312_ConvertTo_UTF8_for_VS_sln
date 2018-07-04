# 流程
# 1. 取得目標路徑下所有 *.cs
# 2. 以 GB 2132 讀入上一步的檔案
# 3. 轉換到 UTF-8 字串
# 4. 照原路徑覆蓋存檔

# -*- coding: utf-8 -*-
import sys

def Get_List_Of_CS_file(folder):
    from os import walk
    # 遞迴列出所有子目錄與檔案
    for root, dirs, files in walk(folder):
        # print(root)
        # print(dirs)
        for file in files:
            print(file[-3:])
            print(file[-3:-1])
            if file[-3:-1] is ".cs":
                print(root+file)
    print("-----------------------------------\n")
        
def main():
    #intValue = int(sys.argv[1])#如果要將變數搞成數字的話可以使用 int()來轉
    folder = sys.argv[1]
    print("target folder: "+folder)
    Get_List_Of_CS_file(folder)

if __name__ == "__main__":
    main()