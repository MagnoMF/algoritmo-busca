from DatabaseModules.DatabaseGrafos import DatabaseGrafos
from FrameModules.Frame import Frame

database = DatabaseGrafos(database_name="grafos.db", database_exemple=False)
# database.init();
# database.buscar_gulosa("arad", "bucharest")
# database.imprimir_rota()

frame = Frame()
frame.run()