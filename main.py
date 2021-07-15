from flask_restful import Api, Resource
from boot import ModelBootApp, ModelConfig
from resources import GeneratedQuestionDto, BatchGeneratedQuestionDto, ModelConfigDto

repository = "valhalla/t5-small-qg-prepend"
app = ModelBootApp(__name__, repository)
api = Api(app)

api.add_resource(
    GeneratedQuestionDto, 
    "/qg/<string:baseKnowledge>", 
    resource_class_kwargs={
        'nlp': app.service
    }
)

api.add_resource(
    BatchGeneratedQuestionDto, 
    "/qg", 
    resource_class_kwargs={
        'nlp': app.service
    }
)

api.add_resource(
    ModelConfigDto, 
    "/model/config", 
    resource_class_kwargs={
        'nlp': app.service
    }
)

if __name__ == "__main__":
    app.run(debug=True)
