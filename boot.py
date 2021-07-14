from model_boot import ModelBoot
from flask_restful import Api, Resource

repository = "p208p2002/gpt2-squad-qg-hl"
app = ModelBoot(__name__, repository)
api = Api(app)

class GeneratedQuestion(Resource):
    def get(self): 
        return app.model.config.to_dict()

    def post(self, baseKnowledge): 
        return app.model.config.to_dict()

api.add_resource(GeneratedQuestion, "/qg")

if __name__ == "__main__":
    app.run(debug=True)
