from src.controllers.pagina_controller import *
from src.controllers.rota_controller import *
from src.controllers.jogo_controller import *

app.add_url_rule('/', view_func=carregarIndex.as_view('index'))
app.add_url_rule('/listarRotas', view_func=listarRotas.as_view('listar_rotas'))
app.add_url_rule('/escolher', view_func=escolher.as_view('escolher'))