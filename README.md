# productimporter101
Imorts product from csv to db, used celery. The uploaded file is given to celery task handeler to process it in background. 
This project needed redis or similar server.
1. Clone this project
2. Update settings in productimporter1001/settins.py
3. Install all requirments productimporter1001/requirments.txt
4. Make sure redis or similar server is running and in settins.py CELERY_BROKER_URL is updated for this server(redis)
5. Update databas settings in productimporter1001/settins.py 
6. Run Celery worker by command
  $ celery -A productimporter1001.celery worker -l DEBUG -E
6. Run these commands in another terminal
    $ python manage.py makemigration
    $ python manage.py migrate
    $ python manage.py runserver
7. open in browser http://localhost:8000/product/
    


