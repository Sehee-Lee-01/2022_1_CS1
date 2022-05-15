from cgi import parse_qs
from template import html

def application(environ, start_response):
    d = parse_qs(environ['QUERY_STRING'])
    a = d.get('a', [''])[0]
    b = d.get('b', [''])[0]
    if '' not in [a, b]:
        a, b = int(a), int(b)
        x = a+b
        y = a*b
        file = open("/var/www/html/text/file.txt", "w")
        file.write("The sum of two numbers is "+ str(x) + ".\n")
        file.write("The product of two numbers is "+ str(y) + ".\n")
        file.close()
    response_body = html
    start_response('200 OK', [
        ('Content-Type', 'text/html'),
        ('Content-Length', str(len(response_body)))
    ])
    return [response_body]

