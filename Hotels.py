import sqlite3 as sq
hotels = [
    ("Ronda", "This is a hotel for the whole family right in the city center.", 3, 2100),
    ("France", "You will immerse yourself in the incredibly beautiful atmosphere of France", 5, 10000),
    ("Mikasa", "The hotel is built in oriental style and conveys the pure beauty of Asia", 4, 7500),
    ("Paprica", "Enjoy the culture of Spain in this beautiful hotel", 3, 3500)
]

rooms = [
    (1, 2, 5500),
    (1, 1, 2100),
    (1, 3, 7800),
    (2, 2, 15700),
    (2, 1, 10000),
    (2, 4, 24300),
    (3, 3, 15600),
    (3, 1, 7500),
    (3, 2, 12000),
    (4, 1, 3500),
    (4, 2, 6000),
    (4, 2, 7500)
]

clients = [
    (1, "Shawn Cook", 7955955, "01-04-2023", "01-07-2023"),
    (2, "Eric May", 4387489, "01-05-2023", "01-06-2023"),
    (2, "William Jackson", 4995348, "01-02-2023", "01-06-2023"),
    (3, "Fernando Sanchez", 5305108, "01-08-2023", "01-12-2023"),
    (4, "Joshua Garcia", 9459903, "01-14-2023", "01-18-2023"),
    (5, "Brian Wright", 3217013, "02-02-2023", "02-04-2023"),
    (6, "Donald Tucker", 1315790, "02-05-2023", "02-09-2023"),
    (7, "Lee Schwartz", 2184174, "02-08-2023", "02-17-2023"),
    (8, "Christopher Larson", 2901946, "02-15-2023", "02-19-2023"),
    (9, "Larry Jones", 7718953, "02-22-2023", "02-25-2023"),
    (10, "Anthony Bailey", 5474929, "02-26-2023", "02-30-2023"),
    (11, "Eric Dixon", 3337725, "02-11-2023", "02-12-2023"),
    (12, "Norman Smith", 9952757, "03-11-2023", "03-15-2023"),
    (12, "Martha Chavez", 3337725, "02-09-2023", "02-13-2023")

]


with sq.connect("hotels.db") as con:


    cur = con.cursor()

    cur.execute("""
                CREATE TABLE IF NOT EXISTS Hotels (
                    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    description TEXT NOT NULL,
                    stars INTEGER,
                    minimal_price REAL
                )    
            """)

    cur.execute("""
                CREATE TABLE IF NOT EXISTS Rooms (
                    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                    hotel_id INTEGER REFERENCES Hotel(id),
                    count_of_persons INTEGER,
                    price REAL
                )
                """)

    cur.execute("""
                CREATE TABLE IF NOT EXISTS Clients (
                    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                    room_id INTEGER REFERENCES Rooms(id),
                    full_name TEXT NOT NULL,
                    phone_number CHAR,
                    date_start DATE,
                    date_end DATE
                )
    
                """)

    cur.executemany("INSERT INTO Hotels VALUES(NULL, ?, ?, ?, ?)", hotels)
    cur.executemany("INSERT INTO Rooms VALUES(NULL,?, ?, ?)", rooms)
    cur.executemany("INSERT INTO Clients VALUES(NULL, ?, ?, ?, ?, ?)", clients)
    con.commit()
    con.close()


    