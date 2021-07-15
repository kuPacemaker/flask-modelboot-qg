from .nlpaware import NLPAwareResource
from flask import request

def response_wrapping(input, generated):
    return { "input": input, "generated": generated }

class GeneratedQuestionDto(NLPAwareResource):
    def get(self, baseKnowledge): 
        generated_answer = self.nlp.offer(baseKnowledge + " </s>")
        responses = [
            response_wrapping(baseKnowledge, generated_answer)
        ]
        return {"responses": responses}

class BatchGeneratedQuestionDto(NLPAwareResource):
    def post(self):
        json_payload = request.get_json(force=True)
        try:
            messages = json_payload['messages']
        except:
            return {"type": "error", "message": "required key not available."}
        
        batch_baseKnowledge = [baseKnowledge + " </s>" for baseKnowledge in messages]
        batch_generated_answer = self.nlp.offer(batch_baseKnowledge)
        responses = [
            response_wrapping(baseKnowledge, generated_answer) for baseKnowledge, generated_answer in zip(batch_baseKnowledge, batch_generated_answer)
        ]
        return {"responses": responses}
