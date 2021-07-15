from flask_restful import Api, Resource
from boot import ModelBootApp, ModelConfig

repository = "valhalla/t5-small-qg-prepend"
app = ModelBootApp(__name__, repository)
api = Api(app)

class GeneratedQuestionDto(Resource):
    def get(self, baseKnowledge): 
        generated = app.offer(baseKnowledge + " </s>")
        return {"input": baseKnowledge, "generated": generated}

class ModelConfigDto(Resource):
    def get(self):
        return app.model.config.to_dict()

api.add_resource(GeneratedQuestionDto, "/qg/<string:baseKnowledge>")
api.add_resource(ModelConfigDto, "/qg/config")

if __name__ == "__main__":
    app.run(debug=True)
