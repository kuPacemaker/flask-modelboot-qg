from model_boot import ModelBoot
from flask_restful import Api, Resource

repository = "danyaljj/gpt2_question_generation_given_paragraph_answer"
app = ModelBoot(__name__, repository)
api = Api(app)

class GeneratedQuestionDto(Resource):
    def get(self, baseKnowledge): 
        generated = app.offer(baseKnowledge)
        return {"generated": generated}

class ModelConfigDto(Resource):
    def get(self):
        return app.model.config.to_dict()

api.add_resource(GeneratedQuestionDto, "/qg/<string:baseKnowledge>")
api.add_resource(ModelConfigDto, "/qg/config")

if __name__ == "__main__":
    app.run(debug=True)
