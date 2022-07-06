from http import server
from http.server import HTTPServer, BaseHTTPRequestHandler
from lib2to3.refactor import get_fixers_from_package

class helloHandler(BaseHTTPRequestHandler):
    def do_GET(self): #we creat get method
        # to send response , forexample status code (200 , ok) 
        self.send_response(200)
        #to display header on web page.
        self.send_header('content-type', 'text/html')
        #to close the header 
        self.end_headers()
        #to set content in our page 
        self.wfile.write('Hello Python developer , Welcome to my project and my web page :)'.encode()) #encode method using to convert unicode to encoding supported by python uses utf-8 encoding
        self.wfile.write(bytes("<html><head><title>https://tuwaiqacademy.edu.sa</title></head>", "utf-8"))
    
def main():
    PORT = 8080 #variable 
    server = HTTPServer(('', PORT), helloHandler)
     #take two argument: first take local host and port number, second argument: take tee request handler.
    print('Server running on port %s' % PORT)
    server.serve_forever()

# to sure the main function is run when we run the web server
if __name__ == '__main__':
    main()
