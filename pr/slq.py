import string
import sqlite3

conn = sqlite3.connect('charcount.sqlite')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Counts')
cur.execute('CREATE TABLE Counts(char TEXT, count INTEGER)')

fh = input('Enter file name: ')
if len(fh)<1 : fh = 'romeo.txt'
fname = open(fh)
for line in fname :
    line = line.translate(str.maketrans("","",string.punctuation))
    line = line.upper()
    for words in line :
        for char in line :
            cur.execute('SELECT count FROM Counts WHERE char = ?',(char,))
            row = cur.fetchone()
            if row is None :
                cur.execute('INSERT INTO Counts(char,count) VALUES(?,1)',(char,))
            else :
                cur.execute('UPDATE Counts SET count = count + 1 WHERE char=?',(char,))
    conn.commit()
charstr = ('SELECT char,count FROM Counts  ORDER BY char')
for row in cur.execute(charstr):
    print(row[0], row[1])
cur.close()
