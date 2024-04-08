from DatabaseModules.DatabaseGrafos import DatabaseGrafos
from FrameModules.Frame import Frame

database = DatabaseGrafos(database_name="grafos.db", database_exemple=False)
database.init();
frame = Frame(database.buscar_gulosa, database.imprimir_nos())
frame.run()