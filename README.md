# unilm-v1-boot
unilm-v1에 강(強)의존하는 입출력 어댑터

## 문제 정의

자연어 처리 모델이 있다. 모델은 python 인터프리터에서 실행되며, 자연어가 배치로 입력되어 그에 대한 배치 연산 결과를 반환한다.

[python 인터프리터에 UniLMv1을 적재하는 인터페이스]
```bash
python biunilm/decode_seq2seq.py --bert_model bert-large-cased --new_segment_ids --mode s2s \
  --input_file ${DATA_DIR}/dev.pq.txt --split ${EVAL_SPLIT} \
  --model_recover_path ${MODEL_RECOVER_PATH} \
  --max_seq_length 512 --max_tgt_length 48 \
  --batch_size 16 --beam_size 1 --length_penalty 0
```
이 프로젝트에서는 마이크로소프트가 제공하는 파인튠드 모델: `UniLMv1`만이 논의 대상이다.
보았듯이 `biunilm/decode_seq2seq.py`의 인터페이스는 args로 전달되는 텍스트 파일 하나를 읽어들여 배치 처리 후 종료되도록 설계되었다.

이 인터페이스는 서비스에 사용할 수 없다. 모델의 적재 속도는 너무 느리기 때문에 쿼리 요청마다 이 작업을 수행하는 일은 없어야 하기 때문이다.

그러므로 배치 입력에 대해 배치 출력을 만들어내는 자연어 처리 모델이 주어졌을 때,
1) 이 모델을 파이썬 인터프리터에 적재하고
2) 입력과 출력을 지속하도록 하려고 한다.

자연어 처리 모델 코드(.py)를 건드리지 않고 이 요구사항을 만족시키는 어댑터 컴포넌트를 구현하시오.

## 이슈 정의
