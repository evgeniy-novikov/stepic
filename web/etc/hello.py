#! /usr/bin/python

from cgi import parse_qs

def app(environ, start_responce):
    start _responce('200 OK', [('Content-Type', 'text/plain')])
    qs = parse_qs(enveron['QUERY_STRING'])
    return ['%s=%s<br>' % (k, qs[k][0]) for k in qs]