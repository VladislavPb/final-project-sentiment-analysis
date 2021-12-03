from flask import Flask, request
from flask_restful import Api, Resource
from sentiment_classifier import SentimentClassifier


app = Flask(__name__)
api = Api(app)


cls = SentimentClassifier()

class Users(Resource):

    @app.route('/reviews', methods=['GET'])
    def foo(text='', prediction=''):
        if request.data:
            text = request.data
            prediction = cls.get_prediction_message(text.lower())

        return prediction



if __name__ == '__main__':
    app.run()
