#!/usr/bin/env python3

import connexion

from swagger_server import encoder


def main():
    app = connexion.App(__name__, specification_dir='./swagger/')
    app.app.json_encoder = encoder.JSONEncoder
    app.add_api('swagger.yaml', arguments={'title': 'Billogram DiscountCode API'}, pythonic_params=True)  # noqa: E501

    @app.route("/")
    def roottest():
        return '</br>'+'</br>'.join(map(str, app.app.url_map.iter_rules()))

    app.run(port=8080)


if __name__ == '__main__':
    main()
