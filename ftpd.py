import yaml
from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer

with open("ftpd.yaml") as cf:
	config=yaml.safe_load(cf)

authorizer = DummyAuthorizer()
for u in config['users']:
	authorizer.add_user(u['name'], u['pass'], config['ftpdir'], perm="elradfmw")
if config['anonymous']:
	authorizer.add_anonymous(config['ftpdir'])

handler = FTPHandler
handler.authorizer = authorizer

server = FTPServer(("0.0.0.0", 8121), handler)
server.serve_forever()
