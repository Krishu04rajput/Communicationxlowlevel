#!/usr/bin/env python3
import logging
from app import app
import routes  # noqa: F401
import socket_events  # noqa: F401
try:
    from advanced_routes import advanced
    app.register_blueprint(advanced, url_prefix='/api/advanced')
except Exception as e:
    logging.warning('Advanced routes unavailable: %s', e)
try:
    from tools_routes import tools
    app.register_blueprint(tools, url_prefix='/tools')
except Exception as e:
    logging.warning('Tools routes unavailable: %s', e)

if __name__ == '__main__':
    with app.app_context():
        from app import db
        db.create_all()
    print('CommunicationX running at http://127.0.0.1:5000')
    app.run(host='0.0.0.0', port=5000, debug=False, threaded=True, use_reloader=False)
