# BlueSkyAnlytics Assignment

<h2>Demo Video Link : </h2>
https://drive.google.com/drive/folders/1XXB0VITqSFiHUGudSiz5SI1Ao-DvM7uB?usp=sharing
<br>

<h2>Inatallation SetUp</h2>
<ul>
    <li> Now create virtual environment in python  " python3 -m venv env"</li>
    <li> Activate Env "source env/bin/activate"</li>
    <li> Now run "pip install -r requirements.txt"</li>
    <li> Type command "python manage.py migrate"</li>
    <li> Type command "python manage.py runserver"</li>
    <li> Now you are ready for testing the API"</li>
</ul>
<br><br>

<h2>EndPoints</h2>
<ul>
    <li>GET  http://127.0.0.1:8000/api/countries/   :  To get all countries</li>
    <li>GET  http://127.0.0.1:8000/api/countries/<str:country>?startYear=2012&&endYear=2015&&cat=co2   :  To get all records with desird filtering all the param are optional i.e you drop any parameter or all</li>
</ul>


