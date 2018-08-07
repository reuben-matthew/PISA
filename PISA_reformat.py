# -*- coding: utf-8 -*-
"""
Created on Tue Jul 17 11:04:15 2018

@author: mattr
"""

import pandas as pd
import os

while True:
    inputfolder=str(input('please enter the sample folder path : '))
    
    outputfolder=str(input('please enter the sample output folder path : '))
    
    for filenames in os.listdir(inputfolder):
        filepath=(inputfolder+'\\'+filenames)
        df=pd.read_excel(filepath)
        
        TFLineNo=[]
        for i in range(len(df['Forename'])):
            TFLineNo.append('')
        
        TFStuName=[]
        for i in range(len(df['Forename'])):
            TFStuName.append(df['Forename'][i]+' '+df['Surname'][i])
            
        TFGrade=[]
        for i in df['YearGroup']:
            TFGrade.append(i)
        
        TFMonthB=[]
        TFYearB=[]
        for i in df['DoB (dd/mm/yyyy)']:
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
        
        output_filename=(outputfolder+'\\'+filenames)
        outputdf.to_excel(output_filename,index=False)
    
    rerun=input(str('do you want to run this for another sample? (y/n): '))
    if rerun == 'n':
        break
    