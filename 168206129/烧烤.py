ba_tai = dict.fromkeys(range(20),1)
shao_kao_jia = dict.fromkeys(range(8),1)
Btfood_time = 0 
Skjfood_time = 0  
batai_wait_time = 0
skj_wait_time = 0
def Sktime(pleNum):
    global  shao_kao_jia,Skjfood_time,skj_wait_time
    gu_ke = dict.fromkeys(range(pleNum),5)
    if pleNum == 1:
        skj_wait_time = 0
        Skjfood_time = 3*60
    else:
        for i in gu_ke:
            for j in shao_kao_jia:
                if gu_ke[i] > 0: 
                    if shao_kao_jia[j] == 1: 
                        shao_kao_jia[j] = 0 
                        gu_ke[i] -= 1
                    else:
                        continue
                else:
                    continue
            if i>=1:
                skj_wait_time += 180*(i-1)
            Skjfood_time += 180
            if gu_ke[i] > 0:
                Skjfood_time += 180
                i -= 1
            if shao_kao_jia[7] == 0:
                for k in shao_kao_jia:
                    shao_kao_jia[k] = 1
    Skjfood_time /= pleNum
    skj_wait_time /= pleNum


def BtTime(pleNum):
    global Btfood_time,batai_wait_time
    rank = pleNum/20
    if rank >= 0 and rank <= 1:
        batai_wait_time = 0
    elif rank > 1 and rank <= 2:
        batai_wait_time = 10
    elif rank > 2 and rank <= 3:
        batai_wait_time = 30
    elif rank >3 and rank <= 4:
        batai_wait_time = 60
    elif rank >4 and rank <= 5:
        batai_wait_time = 100
    Btfood_time = 10 * pleNum + batai_wait_time
    Btfood_time /= pleNum
    batai_wait_time /= pleNum
    Sktime(pleNum)
#Test-----------------------------
ple = 8
BtTime(ple)
print("平均 %d 位顾客的餐食准备时间为：" %ple,Btfood_time+Skjfood_time,"秒")
print("吧台的平均等待时间为：",batai_wait_time,"秒")
print("烧烤架的平均等待时间为：",skj_wait_time,"秒")
