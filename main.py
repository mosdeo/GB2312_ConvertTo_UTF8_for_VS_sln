# -*- coding: utf-8 -*-
import sys

# 流程
# 1. 取得目標路徑下所有 *.cs
# 2. 以 GB 2132 讀入上一步的檔案
# 3. 轉換到 UTF-8 字串
# 4. 照原路徑覆蓋存檔

# 取得特定附檔名的完整路徑清單
def Get_FullPath_List_Of_files(folder,type=''):
    from os import walk
    list_of_fullpath = []

    # 遞迴列出所有子目錄與檔案
    for root, dirs, files in walk(folder):
        for file in files:
            if file[-3:] == "."+type:
                list_of_fullpath.append(root+'/'+file)

    return list_of_fullpath

# 轉換編碼覆蓋存檔
def Encode_Convert_Save(target_files, src_type, dst_type):
    count = 0
    for target_file in target_files:
        try: #能夠直接用目標編碼 read() 就不需要轉換
            file_ptr = open(target_file, encoding=dst_type, mode='r')
            file_ptr.read()
            file_ptr.close()
        except:
            print("Target file {} can't open with {} ...".format(target_file, dst_type))
            content = open(target_file, encoding=src_type, mode='r').read() # 以 GB2312 讀取內容
            file_ptr = open(target_file, encoding=dst_type, mode='w') # 以 UTF-8 打開檔案指標
            file_ptr.write(content) # 寫入存檔
            file_ptr.close()
            # print("Convert a file done.")
            count += 1

    print("Convert {} files done.".format(count))         
        # except:
        #     print("the file not known encoding.")

        
def main():
    #intValue = int(sys.argv[1])#如果要將變數搞成數字的話可以使用 int()來轉
    folder = sys.argv[1]
    print("target folder: "+folder)
    Encode_Convert_Save(
        [path for path in Get_FullPath_List_Of_files(folder,"cs")],
        'GB2312', 'UTF-8')

if __name__ == "__main__":
    main()