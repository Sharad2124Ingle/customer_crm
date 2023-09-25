import http.server
import ssl

certfile = "path/to/certificate.pem"
keyfile = "path/to/private_key.pem"

context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
context.load_cert_chain(certfile, keyfile)

httpd = http.server.HTTPServer(('localhost', 443),
                               http.server.SimpleHTTPRequestHandler)

httpd.socket = context.wrap_socket(httpd.socket, server_side=True)

print("Server started at https://localhost:443")
httpd.serve_forever()



#http://192.168.0.142:8000/accounts/sha_011_01_rli_2023/