import FinanceDataReader as fdr # pip install finance-datareader 파이낸스 데이터 리더 (FinanceDataReader)

krx_list = fdr.StockListing('KRX') # 한국거래소(KRX)의 상장 종목 전체 목록 가져오기

# 삼성전자의 종목 코드 찾기
sam = fdr.DataReader('005930','2023-01-03','2023-01-05')

print(sam)
#print(sam['Open'][2])
print(str(sam.index[0])[:10])

num_indexes = len(sam.index)
print(num_indexes)  # 데이터프레임의 인덱스 개수 출력