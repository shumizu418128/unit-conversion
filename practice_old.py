import random, datetime, docx
from decimal import Decimal
import numpy as np




print("")
today = str(datetime.date.today())
month_today = int(today[5:7])
if month_today < 10:
    month_today = int(today[6:7])
day_today = int(today[8:10])
if day_today < 10:
    day_today = int(today[9:10])
print(str(month_today) + "/" + str(day_today) + " 単位変換演習")



#問１　長さの問題 length
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
if random_le == 1:
    m = random.randint(1,90) * 10
    cm = random.randint(1,900) * 100
elif random_le == 2:
    m = str(random.uniform(0.1,9))[:4]
    cm = random.randint(10,900)
length = {1:km,2:m,3:cm,4:mm}
unit_length = {1:"km",2:"m",3:"cm",4:"mm"}


#問２　重さの問題 weight
q3_we = 3
while q3_we == 3:
    q_we = np.arange(1,4)
    np.random.shuffle(q_we)
    q1_we = q_we[0]
    q2_we = q_we[1]
    q3_we = q_we[2]
kg = str(random.uniform(0.1,9))[:4] #これはstr
g = random.randint(10,900) * 10
if q3_we == 1:
    mg = random.randint(1,900) * 10000
elif q3_we == 2:
    mg = random.randint(10,90) * 1000
weight = {1:kg,2:g,3:mg}
unit_weight = {1:"kg",2:"g",3:"mg"}


#問３　容積の問題 volume
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


#問４　面積の問題 area
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
if random_ar == 1:
    a = m2
else:
    a = km2
area = {1:km2,2:ha,3:a,4:m2,5:cm2}
unit_area = {1:"km2",2:"ha",3:"a",4:"m2",5:"cm2"}



#出力　設問
print("問１　" + str(length[q1_le]) + " " + unit_length[q1_le] + " + " +
str(length[q2_le]) + " " + unit_length[q2_le] + " = __________ " + unit_length[q3_le])
print("")
print("")
print("問２　" + str(weight[q1_we]) + " " + unit_weight[q1_we] + " + " +
str(weight[q2_we]) + " " + unit_weight[q2_we] + " = __________ " + unit_weight[q3_we])
print("")
print("")
print("問３　" + str(volume[q1_vo]) + " " + unit_volume[q1_vo] + " + " +
str(volume[q2_vo]) + " " + unit_volume[q2_vo] + " = __________ " + unit_volume[q3_vo])
print("")
print("")
print("問４　" + str(area[q1_ar]) + " " + unit_area[q1_ar] + " + " +
str(area[q2_ar]) + " " + unit_area[q2_ar] + " = __________ " + unit_area[q3_ar])


print("")
print("")
print("＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿")
print("")
print("解答")



#問１　解答
km = Decimal(str(km))* Decimal("100000")
if random_le == 1:
    m *= 100
    answer_m = (Decimal(str(cm)) + Decimal(str(km))) / Decimal("100")
elif random_le == 2:
    cm *= 10
    m = Decimal(m) * Decimal("1000")
    answer_m = (Decimal(str(cm)) + Decimal(str(mm))) / Decimal("1000")
answer_km = (Decimal(str(m)) + Decimal(str(cm))) / Decimal("100000")
answer_cm = (Decimal(str(m)) + Decimal(str(mm))) / Decimal("10")
answer_length = {1:answer_km,2:answer_m,3:answer_cm}


#問２　解答
kg = Decimal(str(kg)) * Decimal("1000000")
g *= 1000
answer_kg = (Decimal(str(g)) + Decimal(str(mg))) / Decimal("1000000")
answer_g = (Decimal(str(kg)) + Decimal(str(mg))) / Decimal("1000")
answer_weight = {1:answer_kg,2:answer_g}


#問３　解答
l = Decimal(str(l)) * Decimal("1000")
dl *= 100
answer_L = (Decimal(str(dl)) + Decimal(str(ml))) / Decimal("1000")
answer_dL = (Decimal(str(l)) + Decimal(str(ml))) / Decimal("100")
answer_mL = Decimal(str(l)) + Decimal(str(dl))
answer_volume = {1:answer_mL,2:answer_L,3:answer_dL,4:answer_mL}


#問４　解答
km2 = Decimal(str(km2)) * Decimal("10000000000")
ha = Decimal(str(ha)) * Decimal("100000000")
a = Decimal(str(a)) * Decimal("1000000")
m2 *= 10000
answer_ha = (Decimal(str(km2)) + Decimal(str(a))) / Decimal("100000000")
answer_a = (Decimal(str(ha)) + Decimal(str(m2))) / Decimal("1000000")
answer_m2 = (Decimal(str(a)) + Decimal(str(cm2))) / Decimal("10000")
answer_area = {2:answer_ha,3:answer_a,4:answer_m2}



print("問１："+ str(answer_length[q3_le]) + " " + unit_length[q3_le])
print("問２："+  str(answer_weight[q3_we]) + " " + unit_weight[q3_we])
print("問３："+  str(answer_volume[q3_vo]) + " " + unit_volume[q3_vo])
print("問４："+  str(answer_area[q3_ar]) + " " + unit_area[q3_ar])




#km - m .00(mm時はなし) cm .0
#kg - g .00
#L - dL .0 mL .0
#面積　不明