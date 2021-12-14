from flask import Flask, request
from flask_restful import Api, Resource
from review import Review

app = Flask(__name__)
api = Api(app)

cls = Review()

class Phones(Resource):

    @app.route('/phone', methods=['GET'])
    def foo(text='', review='Empty input. Please type something!'):
        if request.data:
            text = request.data
            review = cls.prediction(text)
        return review, 200
            
if __name__ == '__main__':
    app.run()
