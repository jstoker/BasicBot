import asynchat,asyncore,socket
class asynchat_bot(asynchat.async_chat):
	def __init__(self, host, port):
		asynchat.async_chat.__init__(self)
		self.create_socket(socket.AF_INET,socket.SOCK_STREAM)
		self.set_terminator('\r\n')
		self.data=''
		self.remote=(host,port)
		self.connect(self.remote)
	
	def handle_connect(self):
		self.push('USER BasicBot 8 %s :BasicBot! http://github.com/jstoker/BasicBot\r\nNICK testbot\r\n' % self.remote[0])
	
	def get_data(self):
		r=self.data
		self.data=''
		return r
	def collect_incoming_data(self, data):
		self.data+=data
	def found_terminator(self):
		data=self.get_data()
		if data[:4] == 'PING':
			self.push('PONG %s' % data[5:]+'\r\n')
		if '001' in data:
			self.push('JOIN #bots\r\n')
		if '~hi' in data:
			self.push('PRIVMSG #bots :hi.\r\n')
if __name__ == '__main__':
	asynchat_bot('127.0.0.1',16667)
	asyncore.loop()
