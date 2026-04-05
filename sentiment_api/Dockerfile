# 1. Base Image - 가볍고 필수적인 환경만 포함하는 slim 이미지 사용
FROM python:3.10-slim

# 2. 파이썬 환경 변수 설정
# Python이 .pyc 파일을 쓰지 않도록 설정하고 출력 버퍼링을 비활성화해서 로그가 바로 출력되도록 함
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONPATH=/app

# 3. 보안을 위해 root 권한이 아닌 별도의 사용자 생성 (현업 Best Practice)
RUN addgroup --system appgroup && adduser --system --group appuser

# 4. 작업 디렉토리 설정
WORKDIR /app

# 5. 의존성 파일 복사 및 설치
# 애플리케이션 코드를 복사하기 전에 requirements.txt만 복사하여
# 코드가 수정되어도 의존성이 변경되지 않으면 Docker 캐시를 재활용할 수 있게 함
COPY requirements.txt /app/

RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# 5-1. TextBlob 리소스 프리패치 (런타임 지연 및 런타임 오류 방지)
RUN python -m textblob.download_corpora

# 6. 소스 코드 복사 후 소유권 변경
COPY --chown=appuser:appgroup . /app/

# 7. 비권한 사용자로 변경 (컨테이너 내 보안 강화)
USER appuser

# 8. 컨테이너 개방 포트 (문서화 용도)
EXPOSE 8000

# 9. 애플리케이션 실행
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
