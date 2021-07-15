from .nlpaware import NLPAwareResource

class ModelConfigDto(NLPAwareResource):
    def get(self):
        return self.nlp.model.config.to_dict()
