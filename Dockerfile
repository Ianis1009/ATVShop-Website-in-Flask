FROM python:3.11-slim

WORKDIR /tema

COPY . /tema


RUN pip install --no-cache-dir virtualenv

# Creare mediu virtual
RUN virtualenv venv

# Activare mediu virtual, requirements.txt este deja scris folosind comanda pip freeze > requirements.txt
RUN . /tema/venv/bin/activate && pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

# Setare variabile de mediu
ENV FLASK_APP=server.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_ENV=development

#Comadnda de run, cu activare a mediului virtual
CMD ["/bin/bash", "-c", ". /tema/venv/bin/activate && flask run --host=0.0.0.0 --port=5000"]
