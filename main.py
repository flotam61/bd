import sqlalchemy
import psycopg2

db = 'postgresql://flores:zxc@localhost:5432/music'
engine = sqlalchemy.create_engine(db)
connection = engine.connect()

def name_album():
    list_musician = {"Elvis Presley": "Elvis Aaron Presley", "Jay-Z": "Shawn Corey Carter", "Michael Jackson": "Michael Joseph Jackson",
                     "Madonna": "Madonna Ciccone", "Beyonce": "Beyonce Giselle Knowles-Carter", "Eminem": "Marshall Bruce Mathers",
                     "Ozzy Osbourne": "John Michael Osbourne", "Bob Marley": " Robert Nesta Marley"}

    musician_name = list_musician.keys()

    for l2 in musician_name:
        l5 = list_musician[l2]
        connection.execute("""INSERT INTO musician(name, alias) VALUES(%s, %s);""", (l5, l2))

    list_albums = {"Elvis' Christmas Album": 1957, "American Gangster": 2007, "Invincible": 2001, "Hard Candy": 2008,
                   "Lemonade": 2016, "Kamikaze": 2018, "Under Cover": 2005, "Confrontation": 1983}

    albums_name = list_albums.keys()

    for x in list_albums:
        x1 = list_albums[x]
        connection.execute("""INSERT INTO albums(name_albums, date_year) VALUES(%s, %s);""", (x, x1))

    z = 1
    c = 1

    while z <= 8:
        connection.execute("""INSERT INTO albums_musician(id_musician, id_albums) VALUES(%s, %s);""", (z, c))
        z += 1
        c += 1

def genre_up():
    genre_name = ["Hip_Hop", "Pop", "RnB", "Rock", "Reggae"]
    for genre in genre_name:
        connection.execute("""INSERT INTO genre(genre_name) VALUES(%s);""", (genre))

    genre_hip_hop_id = [2, 6]
    for ghhid in genre_hip_hop_id:
        connection.execute("""INSERT INTO genre_musician(id_musician, id_genre) VALUES(%s, '1');""", (ghhid))
    genre_pop_id = [3, 4]
    for gpid in genre_pop_id:
        connection.execute("""INSERT INTO genre_musician(id_musician, id_genre) VALUES(%s, '2');""", (gpid))
    genre_rnb_id = 5
    connection.execute("""INSERT INTO genre_musician(id_musician, id_genre) VALUES(%s, '3');""", (genre_rnb_id))
    genre_rock_id = [1, 7]
    for grid in genre_rock_id:
        connection.execute("""INSERT INTO genre_musician(id_musician, id_genre) VALUES(%s, '4');""", (grid))
    genre_reggae_id = 8
    connection.execute("""INSERT INTO genre_musician(id_musician, id_genre) VALUES(%s, '5');""", (genre_reggae_id))

def track_on():
    connection.execute("""INSERT INTO track(name_track, id_albums, duration) VALUES('Peace in the Valley', '1', '3.22');""")
    connection.execute("""INSERT INTO track(name_track, id_albums, duration) VALUES('Take My Hand, Precious Lord', '1', '3.17');""")
    connection.execute("""INSERT INTO track(name_track, id_albums, duration) VALUES('Party Life', '2', '4.29');""")
    connection.execute("""INSERT INTO track(name_track, id_albums, duration) VALUES('Say Hello', '2', '5.26');""")
    connection.execute("""INSERT INTO track(name_track, id_albums, duration) VALUES('Break of Dawn', '3', '5.32');""")
    connection.execute("""INSERT INTO track(name_track, id_albums, duration) VALUES('Speechless', '3', '3.18');""")
    connection.execute("""INSERT INTO track(name_track, id_albums, duration) VALUES('Candy Shop', '4', '4.16');""")
    connection.execute("""INSERT INTO track(name_track, id_albums, duration) VALUES('Spanish Lesson', '4', '3.38');""")
    connection.execute("""INSERT INTO track(name_track, id_albums, duration) VALUES('Hold Up', '5', '3.41');""")
    connection.execute("""INSERT INTO track(name_track, id_albums, duration) VALUES('Love Drought', '5', '3.57');""")
    connection.execute("""INSERT INTO track(name_track, id_albums, duration) VALUES('Kamikaze', '6', '3.36');""")
    connection.execute("""INSERT INTO track(name_track, id_albums, duration) VALUES('Venom', '6', '4.29');""")
    connection.execute("""INSERT INTO track(name_track, id_albums, duration) VALUES('All the Young Dudes', '7', '4.36');""")
    connection.execute("""INSERT INTO track(name_track, id_albums, duration) VALUES('Sympathy for the Devil', '7', '7.12');""")
    connection.execute("""INSERT INTO track(name_track, id_albums, duration) VALUES('Give Thanks and Praises', '8', '3.15');""")
    connection.execute("""INSERT INTO track(name_track, id_albums, duration) VALUES('I Know', '8', '3.19');""")

def sbor_on():
    list_sbor = {"Modern songs": 2020, "Old songs": 2000, "In the car": 2015, "In the club": 2013, "Before bedtime": 2008,
                 "Sport": 2018, "Work": 2021, "MySbor": 2020}
    sbor_name = list_sbor.keys()

    for x in sbor_name:
        x1 = list_sbor[x]
        connection.execute("""INSERT INTO sbor(name_sbor, date_year) VALUES(%s, %s);""", (x, x1))

def sbor_up():
    modern_songs = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
    old_songs = [1, 2, 15, 16]
    in_the_car = [4, 7, 12, 15]
    in_the_club = [3, 4, 6, 7, 10, 11]
    before_bedtime = [1, 15, 16]
    sport = [11, 12]
    work = [3, 7, 10, 11, 15, 16]
    mysbor = [3, 4, 11, 12]

    for x in modern_songs:
        connection.execute("""INSERT INTO sbor_track(id_sbor, id_track) VALUES('1', %s);""", (x))
    for x1 in old_songs:
        connection.execute("""INSERT INTO sbor_track(id_sbor, id_track) VALUES('2', %s);""", (x1))
    for x2 in in_the_car:
        connection.execute("""INSERT INTO sbor_track(id_sbor, id_track) VALUES('3', %s);""", (x2))
    for x3 in in_the_club:
        connection.execute("""INSERT INTO sbor_track(id_sbor, id_track) VALUES('4', %s);""", (x3))
    for x4 in before_bedtime:
        connection.execute("""INSERT INTO sbor_track(id_sbor, id_track) VALUES('5', %s);""", (x4))
    for x5 in sport:
        connection.execute("""INSERT INTO sbor_track(id_sbor, id_track) VALUES('6', %s);""", (x5))
    for x6 in work:
        connection.execute("""INSERT INTO sbor_track(id_sbor, id_track) VALUES('7', %s);""", (x6))
    for x7 in mysbor:
        connection.execute("""INSERT INTO sbor_track(id_sbor, id_track) VALUES('8', %s);""", (x7))


connection.execute("""SELECT name_albums, date_year FROM albums
WHERE date_year = 2018;""").fetchall()

connection.execute("""SELECT name_track, duration FROM track
ORDER BY duration DESC;""").fetchone()

connection.execute("""SELECT name_track FROM track
WHERE duration > 3.5;""").fetchall()

connection.execute("""SELECT name_sbor FROM sbor
WHERE date_year BETWEEN 2018 and 2020;""").fetchall()

connection.execute("""SELECT alias FROM musician
WHERE NOT alias LIKE '%% %%';""").fetchall()

connection.execute("""SELECT name_track FROM track
WHERE name_track LIKE '%%My%%';""").fetchall()


