# -*- coding: utf-8 -*-
"""
Created on Thu Mar 24 14:20:50 2022

@author: natha
"""
import sqlite3
a = [['1', 'mlinger0', '6BwpToQYV', 'Michaelina', 'Linger', '2021-10-01 03:02:19'],
['2', 'sbillett1', '3ujEEFqT', 'Shamus', 'Billett', '2021-08-13 01:41:04'],
['3', 'ivaud2', 'XoW0bXy', 'Idalia', 'Vaud', '2022-03-02 09:40:38'],
['4', 'cdenny3', 'fsZz0Oecxdj1', 'Chrissie', 'Denny', '2021-10-15 01:57:49'],
['5', 'bplanke4', '55d2pAm2A9h', 'Benny', 'Planke', '2022-01-02 00:43:11'],
['6', 'cbedome5', 'nxHteK5', 'Cinderella', 'Bedome', '2022-02-03 11:46:25'],
['7', 'gpoltun6', '5Aq1jmCL9Xu', 'Gerti', 'Poltun', '2022-01-29 14:44:29'],
['8', 'syearns7', 'jm0fG0YTmr', 'Sid', 'Yearns', '2022-03-20 02:51:55'],
['9', 'fprandin8', '4DsVtDFWe', 'Farah', 'Prandin', '2021-09-06 08:41:56'],
['10', 'adarracott9', '4wlwHFcxRyNy', 'Audy', 'Darracott', '2021-08-15 00:04:06']]
for line in a:
    first = line[3]
    sur = line[4]
    now = line[5]
    newnow = ''
    newnow+= now[8:10]
    newnow+= now[5:7]
    newnow+= now[17:19]
    ID = (first[0:3]).title()+ (sur[0:3]).title()+newnow
    line[0] = ID
for line in a:
    sqliteConnection = sqlite3.connect('StudyCS.db')
    cursor = sqliteConnection.cursor()
    query = """INSERT INTO accounts VALUES ('"""+line[0]+"','"+line[1]+"','"+line[2]+"','"+line[3]+"','"+line[4]+"','"+line[5]+"')"
    print(query)
    count = cursor.execute(query)
    sqliteConnection.commit()
    cursor.close()

