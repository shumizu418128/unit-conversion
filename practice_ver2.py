import random, datetime
from decimal import Decimal
import numpy as np



print("\n")
today = str(datetime.date.today())
month_today = int(today[5:7])
if month_today < 10:
    month_today = int(today[6:7])
day_today = int(today[8:10])
if day_today < 10:
    day_today = int(today[9:10])
print(str(month_today) + "/" + str(day_today) + " 単位変換演習")



#問1　長さの問題 length
random_le = random.randint(1,2)
q3_le = random_le+2
while q3_le == random_le+2:
    q_le = np.arange(random_le,random_le+3)
    np.random.shuffle(q_le)
    q1_le = q_le[0]
    q2_le = q_le[1]
    q3_le = q_le[2]
km = str(random.uniform(0.1,9))[:4] #これはstr
mm = random.randint(10,900) * 10
m = random.randint(1,90) * 10
cm = random.randint(1,900) * 100
if random_le == 2:
    m = str(random.uniform(0.1,9))[:4]
    cm = random.randint(10,900)
length = {1:km,2:m,3:cm,4:mm}
unit_length = {1:"km",2:"m",3:"cm",4:"mm"}


#問2　重さの問題 weight
q_we = np.arange(1,4)
np.random.shuffle(q_we)
q1_we = q_we[0]
q2_we = q_we[1]
q3_we = q_we[2]
t = str(random.uniform(0.01,0.9))[:4]
kg = str(random.uniform(10,99))[:4] #これはstr
g = random.randint(1,90) * 10000
weight = {1:t,2:kg,3:g}
unit_weight = {1:"t",2:"kg",3:"g"}


#問3　容積の問題 volume
random_vo = random.randint(1,2)
q_vo = np.arange(random_vo,random_vo+3)
np.random.shuffle(q_vo)
q1_vo = q_vo[0]
q2_vo = q_vo[1]
q3_vo = q_vo[2]
l = str(random.uniform(0.1,9))[:4] #これはstr
dl = random.randint(1,90)
ml = random.randint(10,900) * 10
volume = {1:ml,2:l,3:dl,4:ml}
unit_volume = {1:"cm3",2:"L",3:"dL",4:"mL"}


#問4　面積の問題 area
random_ar = random.randint(1,3)
q1_ar, q2_ar, q3_ar = 0,random_ar+1,random_ar+1
while q1_ar == q3_ar or q2_ar == q3_ar:
    q_ar = np.arange(random_ar,random_ar+3)
    np.random.shuffle(q_ar)
    q1_ar = q_ar[0]
    q2_ar = q_ar[1]
km2 = str(random.uniform(0.1,9))[:3] #これはstr
ha = str(random.uniform(0.1,9))[:3] #これはstr
m2 = random.randint(10,900) * 100
cm2 = random.randint(10,900) * 10000
a = km2
if random_ar == 1:
    a = m2
area = {1:km2,2:ha,3:a,4:m2,5:cm2}
unit_area = {1:"km2",2:"ha",3:"a",4:"m2",5:"cm2"}


#問5　体積の問題 bulk
q3_bu = random.randint(1,2)
m3 = str(random.uniform(0.01,0.9))[:4]
cm3 = random.randint(10,900)*1000
unit_bu = {1:"m3",2:"cm3"}


#問6　速度の問題
random_sp = random.randint(1,3)
q1_sp = 3
q2_sp = 1
q3_sp = 2
if random_sp < 3:
    q_sp = np.arange(random_sp,random_sp+2)
    np.random.shuffle(q_sp)
    q1_sp = q_sp[0]
    q2_sp = q_sp[1]
    q3_sp = 1
speed = random.randint(1,20)*30
unit_sp1 = {1:"時速",2:"分速",3:"秒速"}
unit_sp2 = {1:"m",2:"km"}



#出力　設問
print("問1　" + str(length[q1_le]) + " " + unit_length[q1_le] + " + " +
str(length[q2_le]) + " " + unit_length[q2_le] + " = __________ " + unit_length[q3_le] +"\n")
print("問2　" + str(weight[q1_we]) + " " + unit_weight[q1_we] + " + " +
str(weight[q2_we]) + " " + unit_weight[q2_we] + " = __________ " + unit_weight[q3_we] +"\n")
print("問3　" + str(volume[q1_vo]) + " " + unit_volume[q1_vo] + " + " +
str(volume[q2_vo]) + " " + unit_volume[q2_vo] + " = __________ " + unit_volume[q3_vo] +"\n")
print("問4　" + str(area[q1_ar]) + " " + unit_area[q1_ar] + " + " +
str(area[q2_ar]) + " " + unit_area[q2_ar] + " = __________ " + unit_area[q3_ar] +"\n")
print("問5　" + str(m3) + " m3 + " + str(cm3) + " cm3 = __________ " + unit_bu[q3_bu] +"\n")
print("問6　" + str(unit_sp1[q1_sp]) + " " + str(speed) + " m = " + str(unit_sp1[q2_sp]) + 
" __________ " + str(unit_sp2[q3_sp]) +"\n")
print("＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿\n指数を小さくする")



#問1　解答
unit_cal = {1:1,2:10}
length = {1:Decimal(str(km))*Decimal("100000"),2:Decimal(str(m))*Decimal(str(unit_cal[random_le]*100)),3:cm*unit_cal[random_le],4:mm}
cal_le = {1:"100000",2:str(100*unit_cal[random_le]),3:str(unit_cal[random_le]),4:"1"}
answer_le = (Decimal(str(length[q1_le])) + Decimal(str(length[q2_le]))) / Decimal(cal_le[q3_le])


#問2　解答
weight = {1:Decimal(str(t)) * Decimal("1000000"),2:Decimal(str(kg)) * Decimal("1000"),3:g}
cal_we = {1:"1000000",2:"1000",3:"1"}
answer_we = (Decimal(str(weight[q1_we])) + Decimal(str(weight[q2_we]))) / Decimal(cal_we[q3_we])


#問3　解答
volume = {1:ml,2:Decimal(str(l))*Decimal("1000"),3:dl*100,4:ml}
cal_vo = {1:"1",2:"1000",3:"100",4:"1"}
answer_vo = (Decimal(str(volume[q1_vo])) + Decimal(str(volume[q2_vo]))) / Decimal(cal_vo[q3_vo])


#問4　解答
area = {1:Decimal(str(km2))*Decimal("10000000000"),2:Decimal(str(ha))*Decimal("100000000"),3:Decimal(str(a))*Decimal("1000000"),4:m2*10000,5:cm2}
cal_ar = {2:"100000000",3:"1000000",4:"10000"}
answer_ar = (Decimal(str(area[q1_ar])) + Decimal(str(area[q2_ar]))) / Decimal(cal_ar[q3_ar])


#問5　解答
m3 = Decimal(m3) * Decimal("1000000")
cal_bu = {1:"1000000",2:"1"}
answer_bu = (Decimal(str(m3)) + Decimal(str(cm3))) / Decimal(cal_bu[q3_bu])


#問6　解答
cal_sp1 = int(abs(q1_sp - q2_sp))
cal_sp2 = {1:"1",2:"1000"}
cal_sp3 = {1:"1",2:"60"}
answer_sp = speed / 60
if q1_sp > q2_sp:
    answer_sp = Decimal(str(speed)) * Decimal("60") * Decimal(cal_sp3[cal_sp1]) / Decimal(cal_sp2[q3_sp])


#出力　解答
print("解答\n問1:",answer_le,"\n問2:",answer_we,"\n問3:",answer_vo,"\n問4:",answer_ar,"\n問5:",answer_bu,"\n問6:",answer_sp)