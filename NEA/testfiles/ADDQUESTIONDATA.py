# -*- coding: utf-8 -*-
"""
Created on Mon Mar 28 23:06:53 2022

@author: natha
"""
import sqlite3
IDs = ['AudDar150806',
'BenPla020111',
'ChrDen151049',
'CinBed030225',
'FarPra060956',
'GerPol290129',
'IdaVau020338',
'JohJoh070234',
'MicLin011019',
'NatRit020634',
'ShaBil130804',
'SidYea200355',
'admin']
for ID in IDs:
    for i in range(4):
        try:
            sqliteConnection = sqlite3.connect('StudyCS.db')
            cursor = sqliteConnection.cursor()
            query = """INSERT INTO questionsuccess VALUES ('"""+ID+"','"+str(i+1)+"',"+'0'+","+'0'+","+"'False')"
            print(query)
            cursor.execute(query)
            sqliteConnection.commit()
            cursor.close()
    
        except sqlite3.Error as error:
            print("Failed to insert data into sqlite table", error)