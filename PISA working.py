# -*- coding: utf-8 -*-
"""
Created on Thu Jul 19 09:35:41 2018

@author: mattr
"""

import pandas as pd

df=pd.read_excel(r'K:\PSUK\RO\Main Study 2018\Portal\pupil data\11106\11106-82714001-PupilDataForm.xlsx')
df=df.drop(df[(pd.isnull(df['Forename']))&(pd.isnull(df['Forename\nAmend']))].index)

TFLineNo=[]
for i in range(len(df['Forename'])):
    TFLineNo.append(str(i).zfill(5))

TFStuName=[]  
for index,i in enumerate(df['Forename\nAmend']):
    if pd.isnull(i):
        forename=df['Forename'].iloc[index]
    else:
        forename=i
    if pd.isnull(df['Surname\nAmend'].iloc[index]):
        surname=df['Surname'].iloc[index]
    else:
        surname=df['Surname\nAmend'].iloc[index]
    TFStuName.append(((forename+' '+surname).lower()).title())
    
TFGrade=[]
for index,i in enumerate(df['Year Group\nAmend']):
    if pd.isnull(i):
        TFGrade.append(df['Year\nGroup'].iloc[index])
    else:
        TFGrade.append(i)

TFMonthB=[]
TFYearB=[]
for index,i in enumerate(df['DoB Amend\n(dd/mm/yyyy)']):
    if pd.isnull(i):   
        if '/' in str(df['DoB \n(dd/mm/yyyy)'].iloc[index]):
            TFMonthB.append(str(df['DoB \n(dd/mm/yyyy)'].iloc[index]).split('/')[1])
            TFYearB.append(str(df['DoB \n(dd/mm/yyyy)'].iloc[index]).split('/')[2])
        if '-' in str(df['DoB \n(dd/mm/yyyy)'].iloc[index]):
            TFMonthB.append(str(df['DoB \n(dd/mm/yyyy)'].iloc[index]).split('-')[1])
            TFYearB.append(str(df['DoB \n(dd/mm/yyyy)'].iloc[index]).split('-')[0])
    else:
        if '/' in str(i):
            TFMonthB.append(str(i).split('/')[1])
            TFYearB.append(str(i).split('/')[2])
        if '-' in str(i):
            TFMonthB.append(str(i).split('-')[1])
            TFYearB.append(str(i).split('-')[0])

TFStudyProg=[]
for i in range(len(df['Forename'])):
    TFStudyProg.append(99)
    
TFSEN=[]
for i in range(len(df['Forename'])):
    TFSEN.append(0)
    
TFEACs=[]
for i in range(len(df['Forename'])):
    TFEACs.append(999)
    
TFEAComm=[]
for i in range(len(df['Forename'])):
    TFEAComm.append('')
    
outputdf=pd.DataFrame({'TFLineNo':TFLineNo,'TFStuName':TFStuName,'TFGrade':TFGrade,'TFMonthB':TFMonthB,'TFYearB':TFYearB,
                       'TFStudyProg':TFStudyProg,'TFSEN':TFSEN,'TFEACs':TFEACs,'TFEAComm':TFEAComm})
outputdf=outputdf[['TFLineNo','TFStuName','TFGrade','TFMonthB','TFYearB','TFStudyProg','TFSEN','TFEACs','TFEAComm']]