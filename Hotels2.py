import sqlite3 as sq

conn = sq.connect("hotels.db")
cur = conn.cursor()
#вывод самого дешёвого отеля
cur.execute("""SELECT MIN(minimal_price) FROM Hotels""")
cheapest_room = cur.fetchone()
print(f"Самый дешевый номер среди все отелей - {cheapest_room[0]}")

#список отелей по убыванию цены
cur.execute("""SELECT name FROM Hotels ORDER BY minimal_price DESC""")
sorted_hotels = cur.fetchall()
print(f"Список отелей по убыванию цены:")
for hotel in sorted_hotels:
    print(hotel[0])

#список клиентов по увеличению цены комнаты
cur.execute("""SELECT Clients.full_name, Hotels.name FROM Clients
                JOIN Rooms ON Clients.room_id=Rooms.id
                 JOIN Hotels ON Rooms.hotel_id=Hotels.id
                 ORDER BY Rooms.price""")

sorted_clients = cur.fetchall()
print(f"Список клиентов по увеличению цены комнаты:")
for client in sorted_clients:
    print(f"Клиент: {client[0]}; Отель: {client[1]}")

#самый первый клиент каждого отеля
cur.execute("""SELECT Clients.full_name, Hotels.name FROM Hotels
                JOIN Rooms ON Clients.room_id=Rooms.id
                JOIN Hotels""")