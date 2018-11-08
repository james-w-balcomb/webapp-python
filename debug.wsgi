import sys

def application(environ, start_response):
    status = "200 OK"
	
    output = \
	    "mod_wsgi.process_group = %s\n" % repr(environ["mod_wsgi.process_group"]) + \
	    "wsgi.multithread = %s\n" % repr(environ["wsgi.multithread"])
	
    response_headers = [("Content-type", "text/plain"), ("Content-Length", str(len(output)))]
	
    start_response(status, response_headers)
    
    return [bytes(output, "utf8")]

