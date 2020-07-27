from __future__ import absolute_import, division, print_function, unicode_literals
import os
import sys


if sys.version_info < (3, 0):
    sys.exit(0)
else:
    sys.path.append(os.path.dirname(os.path.abspath(__file__)))
    sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'vendor'))

from cps import create_app
from cps import web_server
from cps.opds import opds
from cps.web import web
from cps.jinjia import jinjia
from cps.about import about
from cps.shelf import shelf
from cps.admin import admi
from cps.gdrive import gdrive
from cps.editbooks import editbook

try:
    from cps.kobo import kobo, get_kobo_activated
    from cps.kobo_auth import kobo_auth
    kobo_available = get_kobo_activated()
except ImportError:
    kobo_available = False

try:
    from cps.oauth_bb import oauth
    oauth_available = True
except ImportError:
    oauth_available = False


def main():
    app = create_app()
    app.register_blueprint(web)
    app.register_blueprint(opds)
    app.register_blueprint(jinjia)
    app.register_blueprint(about)
    app.register_blueprint(shelf)
    app.register_blueprint(admi)
    app.register_blueprint(gdrive)
    app.register_blueprint(editbook)
    if kobo_available:
        app.register_blueprint(kobo)
        app.register_blueprint(kobo_auth)
    if oauth_available:
        app.register_blueprint(oauth)
    print('Running on http://127.0.0.1:8083 (Press CTRL+C to quit)')
    success = web_server.start()
    sys.exit(0 if success else 1)


if __name__ == '__main__':
    main()
