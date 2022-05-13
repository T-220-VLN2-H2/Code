# FireSale! codebase


# Environment setup
Inside the `firesale` directory, please add your own `.env` file with the following information
```
SECRET_KEY=<Supersecretkey>
DB_NAME=<Name of your database>
DB_USER=<Name of your database user>
DB_PASSWORD=<Database user password>
DB_HOST=<Ip address of your database>
DEBUG=1 # Set value to 0 to remove debug mode
DJANGO_ALLOWED_HOSTS=127.0.0.1 [::1] # Add IP's separated by a space after needs 
```

You will need to have version 13/14 of postgres installed before installing the requirements
### Running locally
```
python -m venv venv
source venv/bin/activate

pip -r requirements.txt

python manage.py makemigrations
python manage.py migrate
python manage.py loaddata core/fixtures/*.json
python manage.py createsuperuser
```
This setup will create over 200 products and assign them to the "shopkeeper" user.
If you do not want to load items into the page run the following loaddata command instead
```
python manage.py loaddata categories users only_profile
```
This will only create the shopkeeper default user along with some default images for the profile and the products.  
Our static folder includes all the needed images for the default items


### Running with docker
```
docker-compose up -d --build
docker exec code_web_1 python manage.py makemigrations && python manage.py migrate && python loadddata core/fixtures/*.json  
docker exec code_web_1 -it python manage.py createsuperuser
```
This should initialize the database, you'll still have to have the postgres database server setup on a different machine, as per the requirements
## Extra requirements added
* Pagination for category view
* Site deployed on a remote server [Site link](http://fire-sale.deals)
* Rating system for sellers
* History of past purchases
* History of past sold items
* List of active listing for each user
* List of active bids for each user 
* Github workflow for linting and automatic testing
* Default items fixtures 
