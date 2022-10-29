# Travel-Agency-Python07
Trying to create a website to travel all around the world.

Installation Instruction:

Clone the repo:
git clone https://github.com/Neslo87/Travel-Agency-Python07

Enter repo and create virtual environment
cd Travel
python -m venv --prompt=Travel venv
. venv\Scripts\Activate.ps1

pip install -r requirements.txt
Run migrations

python manage.py migrate vehicles
Run local development server

python manage.py runserver
Visit the following url on your browser: http://localhost:8000/
