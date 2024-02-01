from mysql.connector import connection, Error
from Wetterstation import Wetterstation
from Wetterstationsbeobachter import Wetterstationsbeobachter
from Innenbeobachter import Innenbeobachter
from Aussenbeobachter import Aussenbeobachter
from Autobeobachter import Autobeobachter
#HAllo
#mit SSH

def main():
    
    try:
        con = connection.MySQLConnection(user='pi', password='1234', host='localhost', database='wetterKiel')
        my_cursor = con.cursor()
        sql1 = 'SELECT * FROM wetterStation'
        my_cursor.execute(sql1)
        results = my_cursor.fetchall()
        #print("Verbindung zur Datenbank hergestellt")

        for result in results:
            id=result[0]
            stationsName=result[1]
            Stadt=result[2]
            Inhaber=result[3]
            con.close()

    except Error as exp:
        print("Verbindung fehlgeschlagen")
        con.close()

    try:
        con1 = connection.MySQLConnection(user='pi', password='1234', host='localhost', database='wetterKiel')
        my_cursor = con1.cursor()
        sql2 = 'SELECT * FROM beobachter'
        my_cursor.execute(sql2)
        results = my_cursor.fetchall()
        #print("Verbindung zur Datenbank hergestellt")
        beoName = list(results)
        beoStandort = list(results)
        con1.close()

    except Error as exp:
        print("Verbindung fehlgeschlagen")
        con1.close()

    wetterstation = Wetterstation(id, stationsName, Stadt, Inhaber)
    
    
    wetterstationsbeobachter1 = Innenbeobachter (wetterstation, beoName[0][0], beoStandort[0][1])
    wetterstation.add(wetterstationsbeobachter1)
    #print(wetterstationsbeobachter1.getName())
    

    wetterstationsbeobachter2 = Aussenbeobachter (wetterstation, beoName[1][0], beoStandort[1][1])
    wetterstation.add(wetterstationsbeobachter2)
    

    wetterstationsbeobachter3 = Autobeobachter (wetterstation, beoName[2][0], beoStandort[2][1])
    wetterstation.add(wetterstationsbeobachter3)
    

    wetterstation.benachrichtige()
    wetterstation.messen_zeigen()
    
    
if __name__ == "__main__":
    main()

