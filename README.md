# Shadops - Shadowing Matching App

Lalala

## Running the project
Create a virtual environment, for example:
```
python -m venv . 
source bin/activate
```

Followed by:
```
git clone https://github.com/2327031p/shadops.git
cd shadops

pip install -r requirements.txt
```

##### Start server
On Linux
```
./clean_database.sh
```

On Windows:
```
python manage.py makemigrations shadops
python manage.py migrate

python populate_shadops.py

python manage.py runserver
```

