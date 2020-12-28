from app.__init__ import create_app

def run(host= '127.0.0.1', port=4000):
	"""
	Run RESTful API Server
	"""

	#create the flask app
	app = create_app()
	
	# Return the app to the runner state so it geets actually loaded.
	return app.run(host=host, port=port)

if __name__ == '__main__':
	run()
