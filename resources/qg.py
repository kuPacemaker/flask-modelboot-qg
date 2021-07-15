from .nlp_aware import NLPAwareResource

class GeneratedQuestionDto(NLPAwareResource):

    def get(self, baseKnowledge): 
        generated = self.nlp.offer(baseKnowledge + " </s>")
        return {"input": baseKnowledge, "generated": generated}

