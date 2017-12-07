### Requirements

*  Python3

### Development setup

* Create base folder on your projects folder

```shell
cd <your projects folder>
mkdir docvite
```

* Inside the base folder, clone this project

```shell
cd dovcite
git clone https://github.com/neequole/docvite.git
```

* Still inside the base folder, create a virtual environment and activate it

```shell
cd docvite
python3 -m venv <your venv name>
source <your venv name>/bin/activate
```

* Install needed Python package

```shell
cd docvite
pip install -r requirements.txt
```

* Create the database tables (no setup needed as it uses SQLite3)

```shell
./manage.py migrate
```

* Run

```shell
./manage.py runserver
```

### Testing

To run the test cases:

```shell
./manage.py test
```

To test e-mail sent without setting up a SMTP server ([source](https://stackoverflow.com/questions/4642011/test-sending-email-without-email-server)):

```shell
python3 -m smtpd -n -c DebuggingServer localhost:1025
```