# gpt2-qg-boot

qg에 강(強)의존하는 입출력 어댑터

## 문제 정의

**자연어 처리 모델**이 있다. 모델은 python 인터프리터에서 실행되며, 자연어가 배치로 입력되어서 그에 대한 배치 연산 결과를 반환한다.

[python 인터프리터에 UniLMv1을 적재하는 인터페이스]

```
python biunilm/decode_seq2seq.py --bert_model bert-large-cased --new_segment_ids --mode s2s \\
  --input_file ${DATA_DIR}/dev.pq.txt --split ${EVAL_SPLIT} \\
  --model_recover_path ${MODEL_RECOVER_PATH} \\
  --max_seq_length 512 --max_tgt_length 48 \\
  --batch_size 16 --beam_size 1 --length_penalty 0
```

예시는 마이크로소프트가 제공하는 파인튠드 모델: `UniLMv1`이다.

보았듯이 `biunilm/decode_seq2seq.py`의 인터페이스는 args로 전달된 텍스트 파일에서 자연어를 읽어들이고, 연산하여 결과를 반환하고 종료되도록 설계되었다.

이 인터페이스는 서비스에 사용할 수 없다. 모델의 적재 속도는 너무 느리기 때문에 쿼리 요청마다 적재 작업을 수행하는 일은 없어야 하기 때문이다.

그러므로 배치 입력에 대해 배치 출력을 만들어내는 자연어 처리 모델이 주어졌을 때,

1. 이 모델을 파이썬 인터프리터에 적재하고
2. 입력과 출력을 지속하도록 하려고 한다.

이 요구사항을 만족시키는 어댑터 컴포넌트를 구현하고 자연어 처리 모델 코드(.py)를 최소한으로 수정하여 결합하시오.

## 도메인 정의: 자연어처리 서비스

자연어처리 서비스란, 이용자로부터 자연어를 입력받고, 입력을  인공지능 모델에 전파하여 도출한 결과를 다시 이용자에게 되돌려 주는 서비스이다. 

### 주체 및 역할

- 이용자: 모델에 입력하고픈 자연어를 제공하고, 자연어처리 결과를 돌려 받는다.
- 클라이언트 앱: 이용자와 마주하는 얼굴 마담이다. 이용자는 자연어를 입력한다. 이 입력은 어댑터가 이해할 수 있는 형식으로 바꾸어 클라이언트 앱이 어댑터에게 전달한다. 이후 어댑터가 입력에 대한 결과물을 반환하면, 이것을 이용자가 이해할 수 있는 형식으로 바꾸어 다시 이용자에게 반환한다.
- 어댑터: 클라이언트 앱과 어댑티 모델 사이에 있는 컴포넌트이다. 자연어 처리 모델을 래핑하여 이 모델이 적재 이후 지속적인 '자연어 입력- 모델 전파 - 결과 반환' 프로세스로 실행되도록 한다.
- 자연어처리 모델: 처리해야 할 자연어를 입력 받고, 네트워크에 이를 전파하여 자연어 처리 결과물을 만드는 모듈이다.
- 어댑티 모델: 어댑터와 상호작용 가능하도록 인터페이스 요구사항을 구현한, "수정된 자연어처리 모델"이다.

## 인터페이스 정의

이 프로젝트는 `Question Generation` 태스크에 한정하여 확장성을 고려하지 않는 인터페이스를 정의한다.

### 이용자 - 클라이언트 앱

`GET http://localhost/qg/{baseKnowledge}`

자연어 단락 `baseKnowledge` 에 대한 질문 생성을 요청한다.

생성된 질문은 JSON `bkd` 와 `q` 로 이뤄진 객체이다.

```json
{
  "bkd": "질문 생성에 사용할 단락",
  "q": "모델이 생성한 질문"
}

{
  "bkd": "Well, but I still wanna ask: 'How was your day?'",
  "q": "Why do you think I still want to say hello to?"
}
```

### 클라이언트 앱 - 어댑터

클라이언트 앱과 어댑터가 Java로 구현될 경우 명세는 다음과 같다.

```java
@Controller
class QuestionGenerationController {
  private final NLPModel model;
  
  @GetMapping("/qg/{baseKnowledge}")
  public QuestionGenerationResponseDto questionGeneration(@RequestParam String baseKnowledge) {
    return new QuestionGenerationResponseDto(baseKnowledge, model.offer(baseKnowledge));
  }
}

interface NLPModel {
  public void boot();
  public String offer(String message);
  public List<String> offer(List<String> message);
  public void close();
} 
```

### 어댑터 - 어댑티 모델

어댑터와 어댑티 모델은 HTTP REST 형식의 통신을 한다.

```java
abstract class DefaultModelAdapter implements ModelAdapter<ByteArray> {

  private final PythonInterpreter process;
  private final RestIO restio;
  private final Queue<String> resultQueue;

  @Override
  public void boot(){...}

  @Override
  public void write(String message) {
    JSONObject response = restio.send(message);
    resultQueue.offer(resopnse.get("question"));
  }

  @Override
  public ByteArray read() {
    ...
    return resultQueue.pop();
  }
}
```

```python
[어댑티 모델 개략 구조]
Flask앱:
  1. 의존 모델 부팅 (huggingface Auto API)
  2. REST 인터페이스 설정
  3. WebService로서 실행
```
## 마감일
~21.07.17 ><;;;

## 모델 디펜던시
2가지 GPT2 모델을 래핑해 볼 것을 권고한다.
https://huggingface.co/p208p2002/gpt2-squad-qg-hl?text=Harry+Potter+is+a+series+of+seven+fantasy+novels+written+by+British+author%2C+%5BHL%5DJ.+K.+Rowling%5BHL%5D.
https://huggingface.co/danyaljj/gpt2_question_generation_given_paragraph_answer
