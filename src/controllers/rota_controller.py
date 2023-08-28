from flask.views import MethodView
from flask import jsonify, make_response
from src.app import app


class listarRotas(MethodView):
        def get(self):
            try:
                routes = []

                for rule in app.url_map.iter_rules():
                    route = {
                        'endpoint': rule.endpoint,
                        'methods': ','.join(sorted(rule.methods)),
                        'route': rule.rule,
                        'request_type': 'GET'
                    }
                    routes.append(route)

                return make_response(jsonify(routes), 200)
            
            except:
                return make_response(
                jsonify(message="Algo não saiu como esperado!"), 500
                 )

        def post(self):
            try:
                routes = []

                for rule in app.url_map.iter_rules():
                    route = {
                        'endpoint': rule.endpoint,
                        'methods': ','.join(sorted(rule.methods)),
                        'route': rule.rule,
                        'request_type': 'POST'
                    }
                    routes.append(route)

                return make_response(jsonify(routes), 200)
            
            except:
                return make_response(
                jsonify(message="Algo não saiu como esperado!"), 500
                 )
