FROM python:3.5

# install 
RUN mkdir /app
WORKDIR /app

# install requirements
COPY requirements.txt /app
RUN pip install -r requirements.txt

# copy source / this can be changed to a git-clone
COPY . /app
WORKDIR /app/src

# make database
RUN python manage.py makemigrations && python manage.py migrate && python manage.py collectstatic --noinput

# create default super_user
# RUN echo "from django.contrib.auth.models import User; User.objects.create_superuser('admin', 'admin@example.com', 'password')" | python manage.py shell

# expose ports
EXPOSE 8000

# CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000" ]

WORKDIR /app/src
CMD ["gunicorn", "--bind=0.0.0.0:8000", "davixxa_website.wsgi"]