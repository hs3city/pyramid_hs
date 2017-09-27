def includeme(config):
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('index', '/')
    config.add_route('add_todo', '/add'),
    config.add_route('display_todo', '/{pk:\d+}'),
