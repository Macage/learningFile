#coding:utf-8
import pandas as pd
import matplotlib.pyplot as plt
def get_info(filename):
    data = pd.read_excel(filename)
    df = pd.DataFrame(data)
    need1 = []
    need2 = []
    need3 = []
    need4 = []
    need5 = []
    need6 = []
    need7 = []
    need8 = []
    for line in df['needMoney']:
        if line <= 1000:
            info = df[df['needMoney'] == line]['raiseRate']
            for lin in info:
                need1.append(lin)
    print(sum(list(set(need1))))

    for line in df['needMoney']:
        if line > 1000 and line <= 5000:
            info = df[df['needMoney'] == line]['raiseRate']
            for lin in info:
                need2.append(lin)
    print(sum(list(set(need2))))

    for line in df['needMoney']:
        if line > 5000 and line <= 10000:
            info = df[df['needMoney'] == line]['raiseRate']
            for lin in info:
                need3.append(lin)
    print(sum(list(set(need3))))

    for line in df['needMoney']:
        if line > 10000 and line <= 20000:
            info = df[df['needMoney'] == line]['raiseRate']
            for lin in info:
                need4.append(lin)
    print(sum(list(set(need4))))

    for line in df['needMoney']:
        if line > 20000 and line <= 50000:
            info = df[df['needMoney'] == line]['raiseRate']
            for lin in info:
                need5.append(lin)
    print(sum(list(set(need5))))

    for line in df['needMoney']:
        if line > 50000 and line <= 100000:
            info = df[df['needMoney'] == line]['raiseRate']
            for lin in info:
                need6.append(lin)
    print(sum(list(set(need6))))

    for line in df['needMoney']:
        if line > 100000 and line <= 300000:
            info = df[df['needMoney'] == line]['raiseRate']
            for lin in info:
                need7.append(lin)
    print(sum(list(set(need7))))

    for line in df['needMoney']:
        if line > 300000:
            info = df[df['needMoney'] == line]['raiseRate']
            for lin in info:
                need8.append(lin)
    print(sum(list(set(need8))))
          
#get_info('lejuan.xlsx')

def plot():
    x = [1.189917473,0.94237148,0.750433704,0.551794508,0.557924838,0.313584674,0.150743423,0.072200781]
    y = [1, 2, 3, 4, 5, 6, 7, 8]
    plt.plot(y, x)
    plt.show()
plot()
