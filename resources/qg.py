from .nlp_aware import NLPAwareResource
from flask import request

class GeneratedQuestionDto(NLPAwareResource):
    def get(self, baseKnowledge): 
        generated = self.nlp.offer(baseKnowledge + " </s>")
        return {"input": baseKnowledge, "generated": generated}

    def post(self):
        json_payload = request.get_json(force=True)
        try:
            messages = json_payload['messages']
            print("messages! = ", messages)
        except:
            return {"type": "error", "message": "required key not available."}

        responses = [{
            "input": message, 
            "generated": self.nlp.offer(message + " </s>")
            } for message in messages]

        return {"responses": responses}

