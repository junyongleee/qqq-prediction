import yfinance as yf
import pandas as pd

# 1) QQQ 일봉 데이터 다운로드
df = yf.download("QQQ", start="2005-01-01", interval="1d")

# 2) 기본 정보 확인
print("Shape:", df.shape)
display(df.head())
display(df.tail())

# 3) 결측치 개수 확인
print("\nMissing values per column:")
display(df.isna().sum())