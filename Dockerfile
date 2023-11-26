# Используйте базовый образ CentOS
FROM centos

# Установите необходимые зависимости
RUN yum install -y python3 python3-pip

# Установите рабочую директорию внутри контейнера
WORKDIR /app

# Скопируйте файлы проекта в контейнер
COPY . /app

# Установите зависимости проекта
RUN pip3 install -r requirements.txt

# Запустите команду для старта Django-приложения
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]