from http.server import HTTPServer,BaseHTTPRequestHandler

content='''
<html>
    <body>
    My laptop configuration
     <table border="40" cellpadding="20" cellspacing="15">
        <tr>
            <th>System configuration</th>
            <th>Description</th>
        </tr>
        <tr>
            <td>Processor</td>
            <td>i5</td>
        </tr>
        <tr>
            <td>Primary Memory</td>
            <td>16 GB</td>
        </tr>
        <tr>
            <td>Secondary Memory</td>
            <td>512 GB</td>
        </tr>
        <tr>
            <td>OS</td>
            <td>Windows</td>
        </tr>
        <tr>
            <td>Graphics</td>
            <td>Intel Iris Xe</td>
        </tr>
     </table>
    </body>
</html>
'''

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        print("Get request received...")
        self.send_response(200) 
        self.send_header("content-type", "text/html")       
        self.end_headers()
        self.wfile.write(content.encode())

print("This is my webserver") 
server_address =('',8000)
httpd = HTTPServer(server_address,MyServer)
httpd.serve_forever()
