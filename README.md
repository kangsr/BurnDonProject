# burndon : for you dream

깃클론 할때 밑에 그대로 해주시면 돼요~!

git clone https://github.com/NYeonK/burndon.git 

git init

git remote add origin https://github.com/NYeonK/burndon.git

python -m venv myvenv

source myvenv/Scripts/activate

cd burndon

pip install django

python manage.py makemigrations

python manage.py migrate

pip install django-allauth

python manage.py runserver
