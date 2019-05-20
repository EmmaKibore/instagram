# Instagram
Instagram is a social app where users get to interact, post their photos and follow each other.

## User stories
The user should be able to:

 * Sign in to the application to start using.
 * Upload my pictures to the application.
 * See my profile with all my pictures.
 * Follow other users and see their pictures on my timeline.
 * Like a picture and leave a comment on it.

## Prerequisites
 * Python3.6

## Installation
To install, follow the following instructions;

  * $ git clone https://github.com/EmmaKibore/Insta-Clone.git
  * $ cd Insta-Clone
  * $ source virtual/bin/activate
  * Install all the necessary requirements by running pip install -r requirements.txt (Python 3.6).
  * $ ./manager.py runserver

## How to Prepare enviroment variables
Since one needs a virtual enviroment, Create a virtual file and add the following configutions to it

    SECRET_KEY= #secret key will be added by default
    DEBUG= #set to false in production
    DB_NAME= #database name
    DB_USER= #database user
    DB_PASSWORD=#database password
    DB_HOST="127.0.0.1"
    MODE= # dev or prod , set to prod during production
    ALLOWED_HOSTS='.localhost', '.herokuapp.com', '.127.0.0.1'


## Technologies used
* Django 1.11
* Heroku
* Bootstrap

## License (MIT License)
* This project is licensed under the MIT Open Source license, (c) Emma Kibore