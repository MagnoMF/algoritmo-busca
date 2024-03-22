import sqlite3
import os

class DatabaseGrafos:

    def __init__(self, database_name="default_database.db", dir_database=os.getcwd()+"\\database", database_exemple=True):
        if(database_name.endswith(".db") == False):
            raise ValueError("Nome da database não termina com '.db'")
        self.database = None
        self.cur = None
        self.database_name = database_name
        self.dir_database = dir_database
        self.database_path = dir_database + "\\" + database_name
        self.database_exemple = database_exemple

    def database_exists(self):
        return os.path.exists(self.database_path)

    def execute(self, sql):
        try:
            self.cur.execute(sql)
        except Exception as e:
            self.database.rollback()
            print(e)
        finally:
            self.database.commit()

    def connect_db(self):
        try:
            self.database = sqlite3.connect(self.database_path)
            self.cur = self.database.cursor()
        except Exception as e:
            raise ValueError("Erro ao conectar com o database", e)

    def inserir_no(self, no):
        sql = "INSERT INTO grafos (ds_no) VALUES ('{}')".format(no)
        self.execute(sql)

    def init(self):
        if(not(self.database_exists() or self.database_exemple)):
            raise ValueError("Database inexistente, defina database_exemple como True para criar um exemplo")
        self.connect_db()
        if(self.database_exemple):
            print("Criando database exemplo")
            self.execute("CREATE TABLE IF NOT EXISTS grafos (cd_no INTEGER PRIMARY KEY AUTOINCREMENT, ds_no VARCAHR(100))")
            self.execute("CREATE TABLE IF NOT EXISTS conexoes (cd_no INTEGER NOT NULL, cd_no_filho INETEGER NOT NULL, nr_custo INT NOT NULL)")
            self.inserir_no
