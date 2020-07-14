
FROM python:3-slim as builder

WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
ADD app.py app.py
COPY . /app
ADD sentiment_labeled_name_category_final.csv sentiment_labeled_name_category_final.csv
ADD merged_sentiments.csv merged_sentiments.csv
CMD ["python", "app.py" ]

#######################################

FROM builder AS dev

COPY requirements-dev.txt requirements-dev.txt
RUN pip install -r requirements-dev.txt

#######################################

FROM builder AS production

EXPOSE 8080

CMD ["python", "app.py" ]
