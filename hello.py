def app(environ, start_response):
    data = environ['QUERY_STRING'].replace('&', '\n')
    start_response('200 OK', [('Content-Type', 'text/plain')])
    return data