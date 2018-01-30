# WebsiteProj
> The code that runs [davixxa.net](http://davixxa.net)


## Installation

```sh
# Clone the repository
git clone https://github.com/Davixxa/WebsiteProj.git
cd WebsiteProj
```

### Using Docker
The easiest way is to run it inside a Docker container

For running the entire stack
```sh
docker-compose up
```

For running just the web-app
```sh
docker build . -t dev
docker run dev
```

### Using Virtualenv

```sh
# Create a virtual environment
virtualenv venv -p python3.5
```

Activate it using one of the following commands: 
```sh
# Windows
.\venv\Scripts\activate

# Linux / OSX
source venv/bin/activate
```

Run the dev server
```sh
python manage.py runserver
```
