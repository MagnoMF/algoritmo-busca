from VertorModules.VetorOrdenado import VetorOrdenado
import sqlite3
import os
import time

class DatabaseGrafos:

    def __init__(self, database_name="default_database.db", dir_database=os.getcwd()+"\\database", database_exemple=True):
        self.rota = []
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
        # print("executando:", sql)
        try:
            return self.cur.execute(sql)
        except Exception as e:
            self.database.rollback()
            print(e)
            exit(1)
        finally:
            self.database.commit()

    def connect_db(self):
        try:
            self.database = sqlite3.connect(self.database_path)
            self.cur = self.database.cursor()
        except Exception as e:
            raise ValueError("Erro ao conectar com o database", e)

    def buscar_no(self,no):
        if (type (no) == int):
            sql = "SELECT * FROM grafos WHERE cd_no = '{}';".format(no)
        elif type(no) == str: 
            sql = "SELECT * FROM grafos WHERE ds_no = '{}';".format(no.upper())
        self.execute(sql)
        return self.cur.fetchall()

    def buscar_adjacentes(self, cd_no):
        sql = "SELECT * FROM conexoes WHERE cd_no = {};".format(cd_no)
        self.execute(sql)
        return self.cur.fetchall()
    
    def adicionar_vertices(self, ds_pai, ds_filhos):
        for ds_filho in ds_filhos:
            if(ds_pai == ds_filho):
                print("O no {} e o no {} são o mesmo".format(ds_pai, ds_filho))
            no_pai = self.buscar_no(ds_pai)
            no_filho = self.buscar_no(ds_filho)
            print(no_pai, no_filho)
            self.execute('SELECT * FROM conexoes WHERE cd_no = {} AND cd_no_filho = {};'.format(no_pai[0][0], no_filho[0][0]))
            sn_existe = self.cur.fetchall()
            if(sn_existe):
                print("O no {} já é filho de {}".format(ds_filho.upper(), ds_pai.upper()))
            elif(ds_pai == ds_filho):
                print("O no {} não pode ser filho dele mesmo".format(ds_pai.upper(), ds_filho.upper()))
            else:
                sql = "INSERT INTO conexoes (cd_no, cd_no_filho) VALUES ({},{});".format(no_pai[0][0], no_filho[0][0])
                self.execute(sql)
                print("Adicionado {} como filho de {}".format(ds_filho.upper(), ds_pai.upper()))


    def inserir_no(self, nos):
        for no in nos:
            if(len(self.buscar_no(no[0])) > 0):
                print("O nó {}, ja existe !!".format(no[0]))
                continue
            sql = "INSERT INTO grafos (ds_no, nr_peso) VALUES ('{}',{});".format(no[0].upper(), no[1])
            self.execute(sql)
    
    def init(self):
        if(not(self.database_exists() or self.database_exemple)):
            raise ValueError("Database inexistente, defina database_exemple como True para criar um exemplo")
        self.connect_db()
        if(self.database_exemple):
            self.execute("CREATE TABLE IF NOT EXISTS grafos (cd_no INTEGER PRIMARY KEY AUTOINCREMENT, ds_no VARCAHR(100) NOT NULL, nr_peso INT NOT NULL);")
            self.execute("CREATE TABLE IF NOT EXISTS conexoes (cd_no INTEGER NOT NULL, cd_no_filho INETEGER NOT NULL);")
            self.inserir_no([('Arad', 366), ('Zerind', 374), ('Oradea', 380), ('Sibiu', 253), ('Timisoara', 329), ('Lugoj', 244), ('Mehadia', 241),
                              ('Dobreta', 242), ('Craiova', 160), ('Rimnicu', 193), ('Fagaras', 178), ('Pitesti', 98), ('Bucharest', 0), ('Giurgiu', 77)])
            self.adicionar_vertices("arad",["zerind", "sibiu", "timisoara"] )
            self.adicionar_vertices("zerind", ["arad", "oradea"])
            self.adicionar_vertices("oradea", ["zerind", "sibiu"])
            self.adicionar_vertices("sibiu", ["oradea","arad","fagaras","rimnicu"])
            self.adicionar_vertices("timisoara", [ "arad", "lugoj" ])
            self.adicionar_vertices("lugoj", ["timisoara", "mehadia"])
            self.adicionar_vertices("mehadia", ["lugoj", "dobreta"])
            self.adicionar_vertices("dobreta", ["mehadia", "craiova"])
            self.adicionar_vertices("craiova", ["dobreta", "pitesti", "rimnicu"])
            self.adicionar_vertices("rimnicu", ["craiova", "sibiu", "pitesti"])
            self.adicionar_vertices("fagaras", [ "sibiu", "bucharest"])
            self.adicionar_vertices("pitesti", ["rimnicu", "craiova", "bucharest"])
            self.adicionar_vertices("bucharest", ["fagaras", "pitesti", "giurgiu"])
    
    def buscar_gulosa(self, no_origem, no_destino):
        no_origem = no_origem.upper()
        no_destino = no_destino.upper()
        self.rota.append(no_origem)
        print("De: {} --> {}".format(no_origem, no_destino))
        time.sleep(1)
        if (no_origem == no_destino):
            print("Busca finalizada")
            return
        no_autal = self.buscar_no(no_origem)
        adj_no_atual = self.buscar_adjacentes(no_autal[0][0])
        if(len(adj_no_atual) == 0):
            print("Nenhum no adjacentes para: {}".format(no_origem))
            print("Rota sem saida")
            return
        vetor = VetorOrdenado(len(adj_no_atual))
        for adj in adj_no_atual:
            no = self.buscar_no(adj[1])
            vetor.insere(no[0])
        print("Vertices de: {} {}".format(no_origem, "-"*3) )
        vetor.imprime()
        no_atual = vetor.get_first()
        self.buscar_gulosa(no_atual[1], no_destino)


    def imprimir_rota(self):
        print("Rota: {}".format(" --> ".join(self.rota)))
    
    def imprimir_nos(self):
        sql = "SELECT ds_no FROM grafos;"
        self.execute(sql)
        return self.cur.fetchall()