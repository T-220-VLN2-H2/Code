# FireSale! codebase


# Environment setup
Inside the `firesale` directory, please add your own `.env` file with the following information
```
SECRET_KEY=
DB_NAME=
DB_USER=
DB_PASSWORD=
DB_HOST=
```

You will need to have version 13/14 of postres installed before installing the requirements

```
python -m venv venv
source venv/bin/activate

pip -r requirements.txt

python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```
