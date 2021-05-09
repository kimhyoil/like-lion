FROM python:3
RUN pip install -r requirements.txt
WORKDIR ./app 
COPY . .
WORKDIR ./todolist
CMD ["python3", "manage.py", "runserver", "0:8000"]
EXPOSE 8000