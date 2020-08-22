import sqlite3

class Model:
    def __init__(self):
        self.song_dict={}
        self.db_status=True
        self.conn=None
        self.cur=None
        try:
            self.conn=sqlite3.connect("music.db")
            print("Connection open")
            self.cur=self.conn.cursor()
            print("Curser opened")
            self.cur.execute("CREATE TABLE IF NOT EXISTS myfavourites(song_id INT,song_name TEXT,song_path TEXT)")
        except sqlite3.DatabaseError as ex:
            print("DB Errorr:",ex)
            self.db_status=False
    def get_db_status(self):
        return self.db_status
    def close_db_connection(self):
        if self.cur is not None:
            self.cur.close()
            print("Curser Closed!!")
        if self.conn is not None:
            self.conn.close()
            print("Connection Closed")
    def add_song(self,song_name,song_path):
        self.song_dict[song_name]=song_path
        print("Song added:",self.song_dict[song_name])

    def get_song_path(self,song_name):
        return self.song_dict[song_name]

    def remove_song(self,song_name):
        print("Song removed",self.song_dict.pop(song_name))

    def search_song_in_favourites(self,song_name):
        self.cur.execute("select song_name from myfavourites where song_name=:1",(song_name,))
        song_tuple=self.cur.fetchone()
        if song_tuple is None:
            return False
        else:
            return True

    def add_song_to_favourites(self,song_name,song_path):
        is_song_present=self.search_song_in_favourites(song_name)
        if is_song_present:
            return "song already present in the favourites!"
        self.cur.execute("select max(song_id) from myfavourites")
        last_song_id=self.cur.fetchone()[0]
        next_song_id=1
        if last_song_id is not None:
            next_song_id=last_song_id+1
        self.cur.execute("insert into myfavourites values(:1,:2,:3)",(next_song_id,song_name,song_path))
        self.conn.commit()
        return "song added to your favourites!"

    def load_songs_from_favourites(self):
        self.cur.execute("select song_name,song_path from myfavourites")
        songs_present=False
        for song_name,song_path in self.cur:
            self.song_dict[song_name]=song_path
            songs_present=True
        if songs_present==True:
            return "List populated from favourites!"
        else:
            return "No songs present in favourites!"

    def remove_song_from_favourites(self,song_name):
        self.cur.execute("delete from myfavourites where song_name=:1",(song_name,))
        if self.cur.rowcount==0:
            return "Song not present in favourites"
        else:
            self.song_dict.pop(song_name)
            self.conn.commit()
            return "Song deleted from your favourites"





