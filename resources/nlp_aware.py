from flask_restful import Resource

class NLPAwareResource(Resource):
    def __init__(self, nlp):
        self.nlp = nlp
