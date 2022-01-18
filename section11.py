# section11
# 파이썬 외부 파일 처리
# 파이썬 Excel, CSV 파일 읽기 및 쓰기

# CSV : MIME - text/csv
import csv
# ex1
with open('./resource/sample1.csv','r') as f:
    reader = csv.reader(f)
    # next(reader) # Header 스킵
    # 확인
    print(reader)
    print(type(reader))
    print(dir(reader)) # 메소드 확인
    print()

    for c in reader:
        print(c)


# ex2
with open('./resource/sample2.csv','r') as f:
    reader = csv.reader(f, delimiter='|') # 나누는 것 알려주는 옵션
    # next(reader) # Header 스킵
    # 확인
    print(reader)
    print(type(reader))
    print(dir(reader)) # 메소드 확인
    print()

    for c in reader:
        print(c)


# ex3 (Dict 변환)
with open('./resource/sample1.csv','r') as f:
    reader = csv.DictReader(f) # 첫번째 raw를 key로 사용 하겠다.

    for c in reader:
        for k, v in c.items():
            print(k, v)
        print('---------------------')


# ex4
w = [[1,2,3,],[4,5,6],[7,8,9],[10,11,12],[13,14,15],[16,17,18]]

with open('./resource/sample3.csv','w',newline='') as f: # 줄바꿈 x 옵션
    wt = csv.writer(f)

    for v in w:
        wt.writerow(v)


# ex5
with open('./resource/sample4.csv','w',newline='') as f:
    wt = csv.writer(f)
    wt.writerows(w)

# XSL, XLSX 
# openpyxl, xlsxwriter, xlrd, xlwt, xlutils
# pandas를 주로 사용(openpyxl, xlrd 를 내부적으로 사용)
# pip install xlrd
# pip install openpyxl
# pip install pandas

import pandas as pd

# sheetname='시트 명' 또는 숫자, header = 숫자, skiprow= 숫자(행 스킵)
xlsx = pd.read_excel('./resource/sample.xlsx')

# 상위 데이터 확인
print(xlsx.head()) # 처음 5개만 보여줌
print()

# 데이터 확인
print(xlsx.tail())

# 데이터 확인
print(xlsx.shape) # 행, 열

# 엑셀 or CSV 다시 쓰기
xlsx.to_excel('./resource/result.xlsx', index=False)
xlsx.to_csv('./resource/result.csv', index=False)






