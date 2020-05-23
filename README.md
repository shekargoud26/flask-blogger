# flask-blogger

flask-blogger is a sample blogging site built using flask and jinja templates. It contains basic functionalities such as user registeration, login. create, update and delete posts after logging in.



## Usage

Setting up the files and environment
```
git clone https://github.com/shekargoud26/flask-blogger.git
cd flask-blogger
# create conda environment using the env file
conda env create -f flask-env.yml
conda activate flaskr
```

Setting the environment variables
```
export FLASK_APP=flaskr
export FLASK_ENV=development
```
Running the application
```
# creating/clearing the database and tables
flask init-db
flask run
```
## Screenshots

![index](screenshots/index.png)
![login](screenshots/login.png)
