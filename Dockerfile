FROM python:3.9

# JDK install 설정 필요

WORKDIR /dashboard/
ENV TZ=Asia/Seoul
ENV VIRTUAL_ENV=/dashboard/.venv
ENV PATH=${VIRTUAL_ENV}/bin:$PATH
RUN python -m venv ${VIRTUAL_ENV}
COPY requirements.txt /dashboard/requirements.txt
RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt
COPY . .
ENTRYPOINT ["streamlit", "run"]
CMD ["App.py"]