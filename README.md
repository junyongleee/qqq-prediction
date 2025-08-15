QQQ Forecast (작은 시계열 프로젝트)

간단한 QQQ(ETF) 시계열 예측 프로젝트입니다.

구조
- app/ : FastAPI 코드
- notebooks/ : EDA 및 실험 노트북
- data/ : 원본/전처리 데이터 (git에 업로드하지 않음)
- model_artifacts/ : 학습된 모델 바이너리 (git에 업로드하지 않음)

시작 방법 (로컬)
1. Conda 환경 생성 및 활성화
2. 의존성 설치: pip install -r requirements.txt
3. Jupyter: jupyter lab
4. FastAPI 실행: uvicorn app.main:app --reload
