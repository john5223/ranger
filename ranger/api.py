import bottle

app = bottle.app()

from controllers import ranger_controller
from controllers import error_controller

if __name__ == '__main__':
    server = 'gevent'
    run_kwargs = {
        'app': app,
        'host': '127.0.0.1',
        'port': 8088,
        'server': 'gevent'
    }
    try:
        from gevent import monkey
        monkey.patch_all()
    except Exception as e:
        print e
        raise e
        run_kwargs.pop('server')

    bottle.run(**run_kwargs)

