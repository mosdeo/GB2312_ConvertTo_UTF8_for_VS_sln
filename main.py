# 流程
# 1. 取得目標路徑下所有 *.cs
# 2. 以 GB 2132 讀入上一步的檔案
# 3. 轉換到 UTF-8 字串
# 4. 照原路徑覆蓋存檔

# -*- coding: utf-8 -*-
#範例程式 argv_samp.py
import sys
 
def main():
    #intValue = int(sys.argv[1])#如果要將變數搞成數字的話可以使用 int()來轉
    print sys.argv[1]
    print sys.argv[2]
    print sys.argv[3]
    print "==============="
    print len(sys.argv)#參數一共有幾個
    print "==============="
    for x in sys.argv:
        print x
 
if __name__ == "__main__":
    main()