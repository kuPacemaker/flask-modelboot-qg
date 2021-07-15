from .nlp_aware import NLPAwareResource
from flask import request

def response_wrapping(input_message, generated_message):
    return { "input": input_message, "generated": generated_message }

class GeneratedQuestionDto(NLPAwareResource):
    def get(self, baseKnowledge): 
        generated = self.nlp.offer(baseKnowledge + " </s>")
        responses = [
            response_wrapping(baseKnowledge, generated)
        ]
        return {"responses": responses}

class BatchGeneratedQuestionDto(NLPAwareResource):
    def post(self):
        json_payload = request.get_json(force=True)
        try:
            messages = json_payload['messages']
        except:
            return {"type": "error", "message": "required key not available."}
        
        knowledges = [baseKnowledge + " </s>" for baseKnowledge in messages]
        answers = self.nlp.offer(knowledges)
        responses = [
            response_wrapping(baseKnowledge, generated_answer) for baseKnowledge, generated_answer in zip(knowledges, answers)
        ]
        return {"responses": responses}
