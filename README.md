# Inventory-Web-App

This app was built with HTML, CSS, and Django. It allows the user to add laboratory items to a database.  
A search bar can be used to narrow down items in this list. Items can be edited and their informtion updated, <br> 
or they can be deleted. The user can also list items that have expired and edit or delete them. There is <br>
barcode scanner functionality built into the app made for two commonly scanned items in my lab. 


<h3>Commands required to run this app: </h3>

Note: As this project was built with Django, it requires python to be able to run

### `Python environment and dependencies`

<ul>
  <li>Create a python virtual environment (venv) </li>
  <li>Activate the virtual environment and navigate to the main project folder </li>
  <li>Pip install "requirements.txt" for the dependencies necessary for this project </li>
  
</ul>


### `Create superuser`
Use `python manage.py createsuperuser` to create an admin
<ul>
  <li>This app requires a login before being able to use it </li>
</ul>


### `Launch the app`

While in the main folder, run`python manage.py runserver` 
<ul>
  <li>In your browser navigate to "localhost:8000/manager"</li>
  <li>Login and you can now use the app!</li>
</ul>


### `More info`

<ul>
  <li>There is dummy data already added to the app that can be manipulated</li>
  <li>There is CRUD functionality built into the app, but the admin panel can also be used to accomplish all of these functions</li>
  <li> Other users can be added with the Admin panel</li>
</ul>

