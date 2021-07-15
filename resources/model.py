from .nlp_aware import NLPAwareResource

class ModelConfigDto(NLPAwareResource):

    def get(self):
        return self.nlp.model.config.to_dict()
