from flask import Flask, Response
from flask_restful import Resource, Api
import json
from json2html import *


app = Flask(__name__)
api = Api(app)

def getdata():
	fileread = open("jsonfile.txt", "r")
	rawdata = json.load(fileread)[0]
	return rawdata["data"]

class Link(Resource):
	def get(self):
		content = "<html><body><a href='/data'>Click Here</a></body></html>"
		return Response(content, mimetype="text/html")
		# return "<html><body><a href='/data'>Click Here</a></body></html>"

class Table(Resource):
	def get(self):
		datas = getdata()
		content = json2html.convert(json = datas)
		return Response(content, mimetype="text/html")

class Table_Sorted(Resource):
	def get(self, path):
		data = getdata()
		mimetypes = {
			".css": "https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css",
			".html": "text/html",
		}
		# complete_path = os.path.join(root_dir(), path)
		# ext = os.path.splitext(path)[1]
		mimetype = mimetypes.get(".html", "text/html")
		# print(path)
		datas = sorted(data, key=lambda x:x[path])
		content = json2html.convert(json = datas)
		return Response(content, mimetype=mimetype)

api.add_resource(Link, '/')
api.add_resource(Table, '/data')
api.add_resource(Table_Sorted, r'/<path:path>')

if __name__ == 	'__main__':
	app.run(debug=True)