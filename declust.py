'''
Programmed by: santosh kautwal
email- er.santoshkatuwal@gmail.com

Knopoff and Gardner
M       L(km)       T(days)
____________________________
2.5     19.5        6
3.0     22.5        11.5
3.5     26          22
4.0     30          42
4.5     35          83
5.0     40          155
5.5     47          290
6.0     54          510
6.5     61          790
7.0     70          915
7.5     81          960
8.0     94          985

Example, any earthquake within 510 days after a magnitude M = 6.0 earthquake,
and with epicenter within 54 km of the epicenter of the M = 6 shock, was
identified as an aftershock.

Limitations of the program
-all magnitude below 4.0 are considered as aftershock
-all magnitude above 8.0 are treated as main shock

'''

import pandas as pd
import datetime as dt
import numpy as np
import itertools
import os

cwd=os.getcwd()

data=pd.read_csv(cwd+'\\events.csv')

n=len(data)

Y=[]
M=[]
D=[]
mag=[]
N=[]
E=[]
date=[]
Events=[]
for i in range(0,n):
    Y_i=data.iloc[i,0]
    M_i=data.iloc[i,1]
    D_i=data.iloc[i,2]
    N_i=data.iloc[i,3]
    E_i=data.iloc[i,4]
    mag_i=data.iloc[i,5]
    date_i=dt.date(Y_i,M_i,D_i)
    date.append(date_i)
    mag.append(mag_i)
    N.append(N_i)
    E.append(E_i)
    
    i=i+1
#computing for M<2.5 magnitude
conv=111.194926644558 #1 degree= 111.194926644558 km

#Checking 8.0 magnitude is main shock or after shock
eight=[]
for i in range(0,n):
    if mag[i]>8:
        ind=[]
        for j in range(0,n):
            tdiff=abs(date[i]-date[j])
            T=tdiff.days
            L=np.sqrt((N[i]-N[j])**2+(E[i]-E[j])**2)*conv
            
            if (L>=94 and T>=985):
              ind.append(i)
              ind = list(dict.fromkeys(ind)) #to drop duplicate values
                
            j=j+1
        eight.append(ind)
    i=i+1
eight=list(itertools.chain.from_iterable(eight)) #to merge 2D list to 1D

#collecting main shocks of magnitudes 7.5-8
seven5=[]
for i in range(0,n):
    if mag[i]>7.5 and mag[i]<=8:
        ind=[]
        Seven5=[]
        for j in range(0,n):
            tdiff=abs(date[i]-date[j])
            T=tdiff.days
            L=np.sqrt((N[i]-N[j])**2+(E[i]-E[j])**2)*conv
            
            if (L>=81 and T>=960):
                ind.append(i)
                ind = list(dict.fromkeys(ind))  #to drop duplicate values
                
                
            j=j+1
        seven5.append(ind)
        
    i=i+1     
seven5=list(itertools.chain.from_iterable(seven5))

#collecting main shocks of magnitudes 7-7.5
seven=[]
for i in range(0,n):
    if mag[i]>7 and mag[i]<=7.5:
        ind=[]
        for j in range(0,n):
            tdiff=abs(date[i]-date[j])
            T=tdiff.days
            L=np.sqrt((N[i]-N[j])**2+(E[i]-E[j])**2)*conv
            
            if (L>=70 and T>=915):
                ind.append(i)
                ind = list(dict.fromkeys(ind))  #to drop duplicate values
                
                
            j=j+1
        seven.append(ind)
    i=i+1    
seven=list(itertools.chain.from_iterable(seven))

#collecting main shocks of magnitudes 6.5-7.0

six5=[]
for i in range(0,n):
    if mag[i]>6.5 and mag[i]<=7.0:
        ind=[]
        for j in range(0,n):
            tdiff=abs(date[i]-date[j])
            T=tdiff.days
            L=np.sqrt((N[i]-N[j])**2+(E[i]-E[j])**2)*conv
            
            if (L>=61 and T>=790):
                ind.append(i)
                ind = list(dict.fromkeys(ind))  #to drop duplicate values
                
                
            j=j+1
        six5.append(ind)
        
    i=i+1
six5=list(itertools.chain.from_iterable(six5))

#collecting main shocks of magnitudes 6.0-6.5

six=[]
for i in range(0,n):
    if mag[i]>6.0 and mag[i]<=6.5:
        ind=[]
        for j in range(0,n):
            tdiff=abs(date[i]-date[j])
            T=tdiff.days
            L=np.sqrt((N[i]-N[j])**2+(E[i]-E[j])**2)*conv
            
            if (L>=54 and T>=510):
                ind.append(i)
                ind = list(dict.fromkeys(ind))  #to drop duplicate values
                
                
            j=j+1
        six.append(ind)
        
    i=i+1
six=list(itertools.chain.from_iterable(six))

#collecting main shocks of magnitudes 5.5 to 6

five5=[]
for i in range(0,n):
    if mag[i]>5.5 and mag[i]<=6.0:
        ind=[]
        for j in range(0,n):
            tdiff=abs(date[i]-date[j])
            T=tdiff.days
            L=np.sqrt((N[i]-N[j])**2+(E[i]-E[j])**2)*conv
            
            if (L>=47 and T>=290):
                ind.append(i)
                ind = list(dict.fromkeys(ind))  #to drop duplicate values
                
                
            j=j+1
        five5.append(ind)
        
    i=i+1
five5=list(itertools.chain.from_iterable(five5))

#collecting main shocks of magnitudes 5.0 to 5.5

five=[]
for i in range(0,n):
    if mag[i]>5.0 and mag[i]<=5.5:
        ind=[]
        for j in range(0,n):
            tdiff=abs(date[i]-date[j])
            T=tdiff.days
            L=np.sqrt((N[i]-N[j])**2+(E[i]-E[j])**2)*conv
            
            if (L>=40 and T>=155):
                ind.append(i)
                ind = list(dict.fromkeys(ind))  #to drop duplicate values
                
                
            j=j+1
        five.append(ind)
        
    i=i+1
five=list(itertools.chain.from_iterable(five))

#collecting main shocks of magnitudes 4.5 to 5.0

four5=[]
for i in range(0,n):
    if mag[i]>4.5 and mag[i]<=5.0:
        ind=[]
        for j in range(0,n):
            tdiff=abs(date[i]-date[j])
            T=tdiff.days
            L=np.sqrt((N[i]-N[j])**2+(E[i]-E[j])**2)*conv
            
            if (L>=35 and T>=83):
                ind.append(i)
                ind = list(dict.fromkeys(ind))  #to drop duplicate values
                
                
            j=j+1
        four5.append(ind)
        
    i=i+1
four5=list(itertools.chain.from_iterable(four5))

#collecting main shocks of magnitudes 4.0 to 4.5

four=[]
for i in range(0,n):
    if mag[i]>4.0 and mag[i]<=4.5:
        ind=[]
        for j in range(0,n):
            tdiff=abs(date[i]-date[j])
            T=tdiff.days
            L=np.sqrt((N[i]-N[j])**2+(E[i]-E[j])**2)*conv
            
            if (L>=30 and T>=42):
                ind.append(i)
                ind = list(dict.fromkeys(ind))  #to drop duplicate values
                
                
            j=j+1
        four.append(ind)
        
    i=i+1
four=list(itertools.chain.from_iterable(four))

#removing repeated aftershocks
len8=len(eight)
len7_5=len(seven5)
len7=len(seven)
len6_5=len(six5)
len6=len(six)
len5_5=len(five5)
len5=len(five)
len4_5=len(four5)
len4=len(four)

#*******************************************************************
#dropping repeated aftershocks of magnitude 4
#*******************************************************************
i=0
j=0
FOUR=[]
for i in range(0,len4):
    for j in range(0,len8):
        try:
            No=eight[j]
            t=date[No]
            last_day=date[No]+dt.timedelta(985)
            
            if date[four[i]]>date[No] and date[four[i]]<last_day:
                del four[i]
 
        except:
            pass
        j=j+1
        
    #*************************************************
    for j in range(0,len7_5):
        try:
            No=seven5[j]
            t=date[No]
            last_day=date[No]+dt.timedelta(960)
            
            if date[four[i]]>date[No] and date[four[i]]<last_day:
                del four[i]
 
        except:
            pass

        j=j+1
    #************************************************
    for j in range(0,len7):
        try:
            No=seven[j]
            t=date[No]
            last_day=date[No]+dt.timedelta(915)
            
            if date[four[i]]>date[No] and date[four[i]]<last_day:
                del four[i]
 
        except:
            pass

        j=j+1
    #************************************************
    for j in range(0,len6_5):
        try:
            No=six5[j]
            t=date[No]
            last_day=date[No]+dt.timedelta(790)
            
            if date[four[i]]>date[No] and date[four[i]]<last_day:
                del four[i]
 
        except:
            pass

        j=j+1
    #************************************************
    for j in range(0,len6):
        try:
            No=six[j]
            t=date[No]
            last_day=date[No]+dt.timedelta(510)
            
            if date[four[i]]>date[No] and date[four[i]]<last_day:
                del four[i]
 
        except:
            pass

        j=j+1
    #************************************************
    for j in range(0,len5_5):
        try:
            No=five5[j]
            t=date[No]
            last_day=date[No]+dt.timedelta(290)
            
            if date[four[i]]>date[No] and date[four[i]]<last_day:
                del four[i]
 
        except:
            pass

        j=j+1
    #************************************************ 
    for j in range(0,len5):
        try:
            No=five[j]
            t=date[No]
            last_day=date[No]+dt.timedelta(155)
            
            if date[four[i]]>date[No] and date[four[i]]<last_day:
                del four[i]
 
        except:
            pass

        j=j+1
    #************************************************ 
    for j in range(0,len4_5):
        try:
            No=four5[j]
            t=date[No]
            last_day=date[No]+dt.timedelta(83)
            
            if date[four[i]]>date[No] and date[four[i]]<last_day:
                del four[i]
 
        except:
            pass

        j=j+1
    
    i=i+1

#*******************************************************************
#dropping repeated aftershocks of magnitude 4.5-5.0
#*******************************************************************
i=0
j=0
for i in range(0,len4_5):
    for j in range(0,len8):
        try:
            No=eight[j]
            t=date[No]
            last_day=date[No]+dt.timedelta(985)
            
            if date[four5[i]]>date[No] and date[four5[i]]<last_day:
                del four5[i]
 
        except:
            pass
        j=j+1
        
    #*************************************************
    for j in range(0,len7_5):
        try:
            No=seven5[j]
            t=date[No]
            last_day=date[No]+dt.timedelta(960)
            
            if date[four5[i]]>date[No] and date[four5[i]]<last_day:
                del four5[i]
 
        except:
            pass

        j=j+1
    #************************************************
    for j in range(0,len7):
        try:
            No=seven[j]
            t=date[No]
            last_day=date[No]+dt.timedelta(915)
            
            if date[four5[i]]>date[No] and date[four5[i]]<last_day:
                del four5[i]
 
        except:
            pass

        j=j+1
    #************************************************
    for j in range(0,len6_5):
        try:
            No=six5[j]
            t=date[No]
            last_day=date[No]+dt.timedelta(790)
            
            if date[four5[i]]>date[No] and date[four5[i]]<last_day:
                del four5[i]
 
        except:
            pass

        j=j+1
    #************************************************
    for j in range(0,len6):
        try:
            No=six[j]
            t=date[No]
            last_day=date[No]+dt.timedelta(510)
            
            if date[four5[i]]>date[No] and date[four5[i]]<last_day:
                del four5[i]
 
        except:
            pass

        j=j+1
    #************************************************
    for j in range(0,len5_5):
        try:
            No=five5[j]
            t=date[No]
            last_day=date[No]+dt.timedelta(290)
            
            if date[four5[i]]>date[No] and date[four5[i]]<last_day:
                del four5[i]
 
        except:
            pass

        j=j+1
    #************************************************ 
    for j in range(0,len5):
        try:
            No=five[j]
            t=date[No]
            last_day=date[No]+dt.timedelta(155)
            
            if date[four5[i]]>date[No] and date[four5[i]]<last_day:
                del four5[i]
 
        except:
            pass

        j=j+1
    
    i=i+1

#*******************************************************************
#dropping repeated aftershocks of magnitude 5.0-5.5
#*******************************************************************
i=0
j=0
for i in range(0,len5):
    for j in range(0,len8):
        try:
            No=eight[j]
            t=date[No]
            last_day=date[No]+dt.timedelta(985)
            
            if date[five[i]]>date[No] and date[five[i]]<last_day:
                del five[i]
 
        except:
            pass
        j=j+1
        
    #*************************************************
    for j in range(0,len7_5):
        try:
            No=seven5[j]
            t=date[No]
            last_day=date[No]+dt.timedelta(960)
            
            if date[five[i]]>date[No] and date[five[i]]<last_day:
                del five[i]
 
        except:
            pass

        j=j+1
    #************************************************
    for j in range(0,len7):
        try:
            No=seven[j]
            t=date[No]
            last_day=date[No]+dt.timedelta(915)
            
            if date[five[i]]>date[No] and date[five[i]]<last_day:
                del five[i]
 
        except:
            pass

        j=j+1
    #************************************************
    for j in range(0,len6_5):
        try:
            No=six5[j]
            t=date[No]
            last_day=date[No]+dt.timedelta(790)
            
            if date[five[i]]>date[No] and date[five[i]]<last_day:
                del five[i]
 
        except:
            pass

        j=j+1
    #************************************************
    for j in range(0,len6):
        try:
            No=six[j]
            t=date[No]
            last_day=date[No]+dt.timedelta(510)
            
            if date[five[i]]>date[No] and date[five[i]]<last_day:
                del five[i]
 
        except:
            pass

        j=j+1
    #************************************************
    for j in range(0,len5_5):
        try:
            No=five5[j]
            t=date[No]
            last_day=date[No]+dt.timedelta(290)
            
            if date[five[i]]>date[No] and date[five[i]]<last_day:
                del five[i]
 
        except:
            pass

        j=j+1
   
    i=i+1

#*******************************************************************
#dropping repeated aftershocks of magnitude 5.5-6.0
#*******************************************************************
i=0
j=0
for i in range(0,len5_5):
    for j in range(0,len8):
        try:
            No=eight[j]
            t=date[No]
            last_day=date[No]+dt.timedelta(985)
            
            if date[five5[i]]>date[No] and date[five5[i]]<last_day:
                del five5[i]
 
        except:
            pass
        j=j+1
        
    #*************************************************
    for j in range(0,len7_5):
        try:
            No=seven5[j]
            t=date[No]
            last_day=date[No]+dt.timedelta(960)
            
            if date[five5[i]]>date[No] and date[five5[i]]<last_day:
                del five5[i]
 
        except:
            pass

        j=j+1
    #************************************************
    for j in range(0,len7):
        try:
            No=seven[j]
            t=date[No]
            last_day=date[No]+dt.timedelta(915)
            
            if date[five5[i]]>date[No] and date[five5[i]]<last_day:
                del five5[i]
 
        except:
            pass

        j=j+1
    #************************************************
    for j in range(0,len6_5):
        try:
            No=six5[j]
            t=date[No]
            last_day=date[No]+dt.timedelta(790)
            
            if date[five5[i]]>date[No] and date[five5[i]]<last_day:
                del five5[i]
 
        except:
            pass

        j=j+1
    #************************************************
    for j in range(0,len6):
        try:
            No=six[j]
            t=date[No]
            last_day=date[No]+dt.timedelta(510)
            
            if date[five5[i]]>date[No] and date[five5[i]]<last_day:
                del five5[i]
 
        except:
            pass

        j=j+1
#*******************************************************************
#dropping repeated aftershocks of magnitude 6.0 -6.5
#*******************************************************************
i=0
j=0
for i in range(0,len6):
    for j in range(0,len8):
        try:
            No=eight[j]
            t=date[No]
            last_day=date[No]+dt.timedelta(985)
            
            if date[six[i]]>date[No] and date[six[i]]<last_day:
                del six[i]
 
        except:
            pass
        j=j+1
        
    #*************************************************
    for j in range(0,len7_5):
        try:
            No=seven5[j]
            t=date[No]
            last_day=date[No]+dt.timedelta(960)
            
            if date[six[i]]>date[No] and date[six[i]]<last_day:
                del six[i]
 
        except:
            pass

        j=j+1
    #************************************************
    for j in range(0,len7):
        try:
            No=seven[j]
            t=date[No]
            last_day=date[No]+dt.timedelta(915)
            
            if date[six[i]]>date[No] and date[six[i]]<last_day:
                del six[i]
 
        except:
            pass

        j=j+1
    #************************************************
    for j in range(0,len6_5):
        try:
            No=six5[j]
            t=date[No]
            last_day=date[No]+dt.timedelta(790)
            
            if date[six[i]]>date[No] and date[six[i]]<last_day:
                del six[i]
 
        except:
            pass

        j=j+1
#*******************************************************************
#dropping repeated aftershocks of magnitude 6.5 -7.0
#*******************************************************************
i=0
j=0
for i in range(0,len6_5):
    for j in range(0,len8):
        try:
            No=eight[j]
            t=date[No]
            last_day=date[No]+dt.timedelta(985)
            
            if date[six5[i]]>date[No] and date[six5[i]]<last_day:
                del six5[i]
 
        except:
            pass
        j=j+1
        
    #*************************************************
    for j in range(0,len7_5):
        try:
            No=seven5[j]
            t=date[No]
            last_day=date[No]+dt.timedelta(960)
            
            if date[six5[i]]>date[No] and date[six5[i]]<last_day:
                del six5[i]
 
        except:
            pass

        j=j+1
    #************************************************
    for j in range(0,len7):
        try:
            No=seven[j]
            t=date[No]
            last_day=date[No]+dt.timedelta(915)
            
            if date[six5[i]]>date[No] and date[six5[i]]<last_day:
                del six5[i]
 
        except:
            pass

        j=j+1


    i=i+1

#*******************************************************************
#dropping repeated aftershocks of magnitude 7.0 -7.5
#*******************************************************************
i=0
j=0
for i in range(0,len7):
    for j in range(0,len8):
        try:
            No=eight[j]
            t=date[No]
            last_day=date[No]+dt.timedelta(985)
            
            if date[seven[i]]>date[No] and date[seven[i]]<last_day:
                del seven[i]
 
        except:
            pass
        j=j+1
        
    #*************************************************
    for j in range(0,len7_5):
        try:
            No=seven5[j]
            t=date[No]
            last_day=date[No]+dt.timedelta(960)
            
            if date[seven[i]]>date[No] and date[seven[i]]<last_day:
                del seven[i]
 
        except:
            pass

        j=j+1
#*******************************************************************
#dropping repeated aftershocks of magnitude 7.5- 8.0
#*******************************************************************
i=0
j=0
for i in range(0,len7_5):
    for j in range(0,len8):
        try:
            No=eight[j]
            t=date[No]
            last_day=date[No]+dt.timedelta(985)
            
            if date[seven5[i]]>date[No] and date[seven5[i]]<last_day:
                del seven5[i]
 
        except:
            pass
        j=j+1

    i=i+1

df4=pd.DataFrame(four)
df4_5=pd.DataFrame(four5)
df5=pd.DataFrame(five)
df5_5=pd.DataFrame(five5)
df6=pd.DataFrame(six)
df6_5=pd.DataFrame(six5)
df7=pd.DataFrame(seven)
df7_5=pd.DataFrame(seven5)
df8=pd.DataFrame(eight)

DF=df4.append(df4_5)
DF=DF.append(df5)
DF=DF.append(df5_5)
DF=DF.append(df6)
DF=DF.append(df6_5)
DF=DF.append(df7)
DF=DF.append(df7_5)
DF=DF.append(df8)

DF=DF.values.tolist()
df=list(itertools.chain.from_iterable(DF))

num=len(df)
DATE=[]
NORTHING=[]
EASTING=[]
MAG=[]

for i in range(0,num):
    DATE_i=date[df[i]]
    NORTHING_i=N[df[i]]
    EASTING_i=E[df[i]]
    MAG_i=mag[df[i]]
    
    DATE.append(DATE_i)
    NORTHING.append(NORTHING_i)
    EASTING.append(EASTING_i)
    MAG.append(MAG_i)
    
    i=i+1

exported=pd.DataFrame({'Date':DATE,'Northing':NORTHING,'Easting':EASTING,'Mag':MAG })

exported.to_csv(cwd+'\\mainshock_only.csv', index = False)

#print(exported)


