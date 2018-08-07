# -*- coding: utf-8 -*-
"""
Created on Tue Jul 17 11:04:15 2018

@author: mattr
"""
from datetime import datetime
import pandas as pd
import numpy as np
import os

months={'January':'01','February':'02','March':'03','April':'04','May':'05','June':'06','July':'07','August':'08','September':'09','October':'10','November':'11','December':'12'}


while True:
    inputfolder=str(input('please enter the sample folder path : '))
    
    outputfolder=str(input('please enter the sample output folder path : '))
    
    for filenames in os.listdir(inputfolder):
        if (('.xlsx') and ('C_C')) in filenames:
            filepath=(inputfolder+'\\'+filenames)
            df=pd.read_excel(filepath)   
            df=df.drop(df[(pd.isnull(df['Forename']))&(pd.isnull(df['Forename\nAmend']))].index)
            
            TFLineNo=[]
            TFMonthB=[]
            TFYearB=[]
            TFStuName=[]
            TFGrade=[]
            TFStudyProg=[]
            TFSEN=[]
            TFEACs=[]
            TFEAComm=[]
            
            for index in range(len(df['Forename'])):
                dob=df['DoB Amend\n(dd/mm/yyyy)'].iloc[index]
                if ((type(dob)==pd._libs.tslib.Timestamp) or (type(dob)==str)):
                    if '/' in str(dob):
                        month=(str(dob).split('/')[1])
                        year=(str(dob).split('/')[2])
                    elif '-' in str(dob):
                        month=(str(dob).split('-')[1])
                        year=(str(dob).split('-')[0])
                    elif ' ' in str(dob):
                        month=months[str(dob.split(' ')[1])]
                        year=str(dob).split(' ')[2]
                elif (pd.isnull(dob) or type(dob)==np.float64) :   
                    if '/' in str(df['DoB \n(dd/mm/yyyy)'].iloc[index]):
                        month=(str(df['DoB \n(dd/mm/yyyy)'].iloc[index]).split('/')[1])
                        year=(str(df['DoB \n(dd/mm/yyyy)'].iloc[index]).split('/')[2])
                    if '-' in str(df['DoB \n(dd/mm/yyyy)'].iloc[index]):
                        month=(str(df['DoB \n(dd/mm/yyyy)'].iloc[index]).split('-')[1])
                        year=(str(df['DoB \n(dd/mm/yyyy)'].iloc[index]).split('-')[0])
                
                if (month<'09' and year<'2002') or (month>'07' and year>'2003'):
                    print('out of range date: ',filenames,'-',index)
                    continue
                
                if df['Pupil Still \non Roll (Y/N)'].iloc[index] == 'N':
                    continue
                
                
                TFLineNo.append(str(index).zfill(5))
                TFMonthB.append(month)
                TFYearB.append(year)
            
                
                forename=(df['Forename\nAmend']).iloc[index]
                if (type(forename)==str) and (pd.notnull(forename)):
                    surname=df['Surname\nAmend'].iloc[index]
                    if (type(surname)==str) and (pd.notnull(surname)):
                        TFStuName.append(((forename+' '+surname).lower()).title())
                    else:
                       surname=df['Surname'].iloc[index]
                       TFStuName.append(((forename+' '+surname).lower()).title())
                else:
                    forename=df['Forename'].iloc[index]
                    surname=df['Surname\nAmend'].iloc[index]
                    if (type(surname)==str) and (pd.notnull(surname)):
                        TFStuName.append(((forename+' '+surname).lower()).title())
                    else:
                        surname=df['Surname'].iloc[index]
                        TFStuName.append(((forename+' '+surname).lower()).title())
               
                    
                year=df['Year Group\nAmend'].iloc[index]
                if (type(year)!=str) or (pd.isnull(year)):
                    TFGrade.append(df['Year\nGroup'].iloc[index])
                else:
                    TFGrade.append(year)
            
        
                TFStudyProg.append(99)
                
                TFSEN.append(0)
                
                TFEACs.append(999)
                
                TFEAComm.append('')
                
            outputdf=pd.DataFrame({'TFLineNo':TFLineNo,'TFStuName':TFStuName,'TFGrade':TFGrade,'TFMonthB':TFMonthB,'TFYearB':TFYearB,
                                   'TFStudyProg':TFStudyProg,'TFSEN':TFSEN,'TFEACs':TFEACs,'TFEAComm':TFEAComm})
            outputdf=outputdf[['TFLineNo','TFStuName','TFGrade','TFMonthB','TFYearB','TFStudyProg','TFSEN','TFEACs','TFEAComm']]
                
            output_filename=(outputfolder+'\\'+filenames)
            outputdf.to_excel(output_filename,index=False)
            
    rerun=input(str('do you want to run this for another sample? (y/n): '))
    if rerun == 'n':
        break
