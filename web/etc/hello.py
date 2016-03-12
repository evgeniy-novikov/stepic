#from cgi import parse_qs

#def app(environ, start_responce):
#    start_responce('200 OK', [('Content-Type', 'text/plain')])
#    qs = parse_qs(environ['QUERY_STRING'])
#    return ['%s=%s<br>' % (k, qs[k][0]) for k in qs]
bind="0.0.0.0:8080"

def app (environ, start_response):
    status = '200 OK'
    response_headers = [('Content-type','text/plain')]
    start_response(status, response_headers)
    options = '\r\n'.join(environ['QUERY_STRING'].split("&"))
    return [options]
