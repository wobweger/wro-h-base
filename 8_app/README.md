## application

This section/folder contain application.

:construction:


### docker 

[](https://phoenixnap.com/kb/how-to-install-docker-on-centos-8)

```shell
systemctl disable firewalld
```


### GCP

+ [GCP](https://github.com/GoogleCloudPlatform)
+ [gcloud](https://cloud.google.com/sdk/gcloud)
+ [gcloud cheatsheet](https://cloud.google.com/sdk/docs/cheatsheet)
+ [Cloud SQL proxy](https://cloud.google.com/sql/docs/mysql/sql-proxy)
  + [Cloud SQL proxy](https://cloud.google.com/sql/docs/mysql/connect-external-app#proxy)
  + [Cloud SQL proxy auth](https://cloud.google.com/sql/docs/mysql/sql-proxy#authentication-options)
  + [Cloud SQL proxy](https://cloud.google.com/sql/docs/mysql/connect-external-app?&_ga=2.45916128.-551510918.1601550873#proxy)
+ [python-docs](https://github.com/GoogleCloudPlatform/python-docs-samples)
+ [AppEngine](https://cloud.google.com/appengine/docs/standard/python3?hl=en_GB)

```shell
git clone https://github.com/GoogleCloudPlatform/python-docs-samples.git
```

```shell
export GOOGLE_CLOUD_PROJECT=boxwood-magnet-291210
```

```shell
docker build --tag helloworld:python .
```

```shell
~/.local/bin/pytest
```

```shell
gcloud builds submit --tag gcr.io/${GOOGLE_CLOUD_PROJECT}/helloworld
```

```shell
gcloud config set project $GOOGLE_CLOUD_PROJECT
```

```shell
gcloud builds submit --tag
 gcr.io/${GOOGLE_CLOUD_PROJECT}/helloworld
```

set default region

```shell
gcloud config set run/region us-central1
```

### remote development

+ [quickstart](https://cloud.google.com/code/docs/vscode/quickstart-remote-dev)

vscode://googlecloudtools.cloudcode/shell?repo=https://github.com/GoogleCloudPlatform/cloud-code-samples.git&subpath=/python/python-guestbook

+ [vscode](vscode://googlecloudtools.cloudcode/shell)

so cool, the only extension needed is *Remote -SSH*
[makteplace](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-ssh)


### python

+ [GCP py3](https://cloud.google.com/appengine/docs/standard/python3?hl=en_GB)
+ [getting started](https://cloud.google.com/python/getting-started/)
  + [github](https://github.com/GoogleCloudPlatform/getting-started-python)
+ [python-docs](https://github.com/GoogleCloudPlatform/python-docs-samples)
  + [github](https://github.com/GoogleCloudPlatform/python-docs-samples)
+ [prj sel](https://console.cloud.google.com/projectselector2/home/dashboard?_ga=2.218161753.1121144402.1601703128-551510918.1601550873)
+ [prj billing](https://cloud.google.com/billing/docs/how-to/modify-project)
+ create Firestore database, Cloud Console
  + select native mode

+ [logging](https://cloud.google.com/logging/docs/setup/python)

```python
# Imports the Cloud Logging client library
import google.cloud.logging

# Instantiates a client
client = google.cloud.logging.Client()

# Retrieves a Cloud Logging handler based on the environment
# you're running in and integrates the handler with the
# Python logging module. By default this captures all logs
# at INFO level and higher
client.get_default_handler()
client.setup_logging()
```

```shell
virtualenv env
source env/bin/activate
pip install -r requirements.txt
```

```shell
pip3 install -r requirements.txt --user
pip3 install gunicorn --user
export GOOGLE_APPLICATION_CREDENTIALS=py01-68835-567090ae32d1.json
```

### django

+ [AppEngine](https://cloud.google.com/python/django/appengine)

py02-80723

```shell
gcloud config list
gcloud auth application-default login

```

*enable Cloud SQL Admin API*

```shell
gcloud services enable sqladmin
```

**install Cloud SQL proxy**

```shell
wget https://dl.google.com/cloudsql/cloud_sql_proxy.linux.amd64 -O cloud_sql_proxy
chmod +x cloud_sql_proxy

```

```shell
export SQL_INSTNACE_NAME=polls-instance
export CONNECTION_NAME=py02-80723:europe-west3:polls-instance
```


```shell
./cloud_sql_proxy -instances=${CONNECTION)=tcp:3306
./cloud_sql_proxy -instances="[YOUR_INSTANCE_CONNECTION_NAME]"=tcp:3306
```

```shell
gcloud sql instances describe polls-instance

walter_obweger@cloudshell:~/github/python-docs-samples/appengine/standard/django (py02-80723)$ gcloud sql instances describe polls-instance
backendType: SECOND_GEN
connectionName: py02-80723:europe-west3:polls-instance
databaseVersion: MYSQL_5_7
etag: 253dac13e0029452379d9966c12abf43f2a6d47c45f08cac019830301808d14f
gceZone: europe-west3-a
instanceType: CLOUD_SQL_INSTANCE
ipAddresses:
- ipAddress: 10.103.48.3
  type: PRIVATE
kind: sql#instance
name: polls-instance
project: py02-80723
region: europe-west3
selfLink: https://sqladmin.googleapis.com/sql/v1beta4/projects/py02-80723/instances/polls-instance
serverCaCert:
  cert: |-
    -----BEGIN CERTIFICATE-----
    MIIDfzCCAmegAwIBAgIBADANBgkqhkiG9w0BAQsFADB3MS0wKwYDVQQuEyQ3MjBm
    NzQ2Mi0yZWE1LTRjNWUtYjhlYi0yNzZlMDRkMWE3ZTUxIzAhBgNVBAMTGkdvb2ds
    ZSBDbG91ZCBTUUwgU2VydmVyIENBMRQwEgYDVQQKEwtHb29nbGUsIEluYzELMAkG
    A1UEBhMCVVMwHhcNMjAxMDA0MDY1MTUwWhcNMzAxMDAyMDY1MjUwWjB3MS0wKwYD
    VQQuEyQ3MjBmNzQ2Mi0yZWE1LTRjNWUtYjhlYi0yNzZlMDRkMWE3ZTUxIzAhBgNV
    BAMTGkdvb2dsZSBDbG91ZCBTUUwgU2VydmVyIENBMRQwEgYDVQQKEwtHb29nbGUs
    IEluYzELMAkGA1UEBhMCVVMwggEiMA0GCSqGSIb3DQEBAQUAA4IBDwAwggEKAoIB
    AQCMA0IXGgJwnso0npM8JAFeeJ+Hr+q4mM3alfUmENqpWyh2R9LTaROB4wCjCaBJ
    P9FxSFK17p7hrzGvTwN649k3oHW+OPZiD6Q+Ye0L8IUKTzN1sHp+Ylx8rXd1q0yA
    OfNcXbKeRYojoIyjmHHe+J32W0WUTx4hjjdbSXB4JZ3JrA1ETphf+v+NSbzQ2GIW
    2gJlvp6Lwk0EH5VmunD8N6DGwkiW8FKyMyZKM15y0h4bcBxqLo03NIUCWtSVg/ce
    oEhsGKxKrIfyipIPqwOVVfOCnXRU49wSmRHvshZCTnh2xOy/EV5l6mxQShQRDUX9
    tC1Nnx9A3NA/0budBCruqMMpAgMBAAGjFjAUMBIGA1UdEwEB/wQIMAYBAf8CAQAw
    DQYJKoZIhvcNAQELBQADggEBAHAQgN5M79xE2F57A3X7yikqdrgP9hCgZSTpXJbP
    hGcyvRlfb6VXkb/PeJ/JHrq56qc2mAULL4PntSLfom0W50g79vl1VraHkPQMI8cp
    xo4q2y7ixXnN4ocYrjAGrOHROof0/jLX8nY8Qh05Bx9Yiy/J711nF5tJ7CDXtOT+
    hPOGwZfvh/bBQNnYDnSGjsOw4lR1ScjfSGnoFSNPOb7xyhAfdHBTpxWhL4LTj71t
    tfQjrjjBi+FDEy+HIgoHOblSHyu9Wn54TDesU3IBindlop6E8XLOpWI8fHZ+0ma1
    f1zchtFhc++Shn0er/rXH5ofdukEtq24tNWfqBZ+RV9gc/I=
    -----END CERTIFICATE-----
  certSerialNumber: '0'
  commonName: C=US,O=Google\, Inc,CN=Google Cloud SQL Server CA,dnQualifier=720f7462-2ea5-4c5e-b8eb-276e04d1a7e5
  createTime: '2020-10-04T06:51:50.199Z'
  expirationTime: '2030-10-02T06:52:50.199Z'
  instance: polls-instance
  kind: sql#sslCert
  sha1Fingerprint: 092197f10b3be6e60655d4042bfd61f87ccbe559
serviceAccountEmailAddress: p238058132317-nuq5zi@gcp-sa-cloud-sql.iam.gserviceaccount.com
settings:
  activationPolicy: ALWAYS
  availabilityType: ZONAL
  backupConfiguration:
    binaryLogEnabled: true
    enabled: true
    kind: sql#backupConfiguration
    location: eu
    startTime: 20:00
  dataDiskSizeGb: '10'
  dataDiskType: PD_SSD
  ipConfiguration:
    ipv4Enabled: false
    privateNetwork: projects/py02-80723/global/networks/default
  kind: sql#settings
  locationPreference:
    kind: sql#locationPreference
    zone: europe-west3-a
  maintenanceWindow:
    day: 0
    hour: 0
    kind: sql#maintenanceWindow
  pricingPlan: PER_USE
  replicationType: SYNCHRONOUS
  settingsVersion: '1'
  storageAutoResize: true
  storageAutoResizeLimit: '0'
  tier: db-n1-standard-1
state: RUNNABLE
```

```shell
gcloud sql instances describe polls-instance

connectionName: py02-80723:europe-west3:polls-instance
```

```shell
./cloud_sql_proxy -instances=py02-80723:europe-west3:polls-instance=tcp:3306 \
                  -credential_file=py02-80723-86e725ec87ca.json &
```

```shell
gcloud sql connect polls-instance --user=root --quiet
```

```shell
export export GOOGLE_APPLICATION_CREDENTIALS=py02-80723-86e725ec87ca.json
export CONNECTION=py02-80723:europe-west3:polls-instance
./cloud_sql_proxy -instances=${CONNECTION)=tcp:3306 python manage.py makemigrations python manage.py makemigrations polls python manage.py createsuperuser python manage.py collectstatic
```

```shell
virtualenv env
source env/bin/activate
pip install -r requirements.txt

```

```shell
python manage.py makemigrations
python manage.py makemigrations polls
python manage.py migrate

```

```shell
python manage.py createsuperuser
python manage.py runserver

```

```shell
python manage.py collectstatic
gcloud app deploy

```

```shell
walter_obweger@cloudshell:/ (py02-80723)$ cd 
walter_obweger@cloudshell:~ (py02-80723)$ cd github/
walter_obweger@cloudshell:~/github (py02-80723)$ cd python-docs-samples/
walter_obweger@cloudshell:~/github/python-docs-samples (py02-80723)$ cd appengine/standard_python3/
walter_obweger@cloudshell:~/github/python-docs-samples/appengine/standard_python3 (py02-80723)$ cd django/
walter_obweger@cloudshell:~/github/python-docs-samples/appengine/standard_python3/django (py02-80723)$ gcloud auth login
Go to the following link in your browser:

    https://accounts.google.com/o/oauth2/auth?client_id=32555940559.apps.googleusercontent.com&redirect_uri=urn%3Aietf%3Awg%3Aoauth%3A2.0%3Aoob&scope=openid+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fuserinfo.email+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fcloud-platform+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fappengine.admin+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fcompute+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Faccounts.reauth&code_challenge=7efyfseDB2sCCaAb2aMLc1U9dqyPyKwSoqewMeCNTpU&code_challenge_method=S256&access_type=offline&response_type=code&prompt=select_account


Enter verification code: 4/4wE6ae4ELr0-ioP-CFSzfd2qNirSnbnD5uAzVIh7Vn9m18fIzUQAbog

You are now logged in as [walter.obweger@gmail.com].
Your current project is [py02-80723].  You can change this setting by running:
  $ gcloud config set project PROJECT_ID
walter_obweger@cloudshell:~/github/python-docs-samples/appengine/standard_python3/django (py02-80723)$ ./cloud_sql_proxy -instances=py02-80723:europe-west3:polls-instance=tcp:3306 \
>                   -credential_file=py02-80723-86e725ec87ca.json &
[1] 3524
walter_obweger@cloudshell:~/github/python-docs-samples/appengine/standard_python3/django (py02-80723)$ 2020/10/04 12:20:55 current FDs rlimit set to 1048576, wanted limit is 8500. Nothing to do here.
2020/10/04 12:20:55 using credential file for authentication; email=sql-834@py02-80723.iam.gserviceaccount.com
2020/10/04 12:20:55 Listening on 127.0.0.1:3306 for py02-80723:europe-west3:polls-instance
2020/10/04 12:20:55 Ready for new connections

walter_obweger@cloudshell:~/github/python-docs-samples/appengine/standard_python3/django (py02-80723)$ virtualenv env

created virtual environment CPython3.7.3.final.0-64 in 1774ms
  creator CPython3Posix(dest=/home/walter_obweger/github/python-docs-samples/appengine/standard_python3/django/env, clear=False, global=False)
  seeder FromAppData(download=False, pip=bundle, setuptools=bundle, wheel=bundle, via=copy, app_data_dir=/home/walter_obweger/.local/share/virtualenv)
    added seed packages: Django==3.1.2, PyMySQL==0.10.1, asgiref==3.2.10, pip==20.2.2, pytz==2020.1, setuptools==49.6.0, setuptools==50.3.0, sqlparse==0.3.1, wheel==0.35.1
  activators BashActivator,CShellActivator,FishActivator,PowerShellActivator,PythonActivator,XonshActivator
walter_obweger@cloudshell:~/github/python-docs-samples/appengine/standard_python3/django (py02-80723)$ source env/bin/activate
(env) walter_obweger@cloudshell:~/github/python-docs-samples/appengine/standard_python3/django (py02-80723)$ 
(env) walter_obweger@cloudshell:~/github/python-docs-samples/appengine/standard_python3/django (py02-80723)$ python manage.py makemigrations
2020/10/04 12:21:50 New connection for "py02-80723:europe-west3:polls-instance"
No changes detected
2020/10/04 12:21:51 Client closed local connection on 127.0.0.1:3306
(env) walter_obweger@cloudshell:~/github/python-docs-samples/appengine/standard_python3/django (py02-80723)$ python manage.py makemigrations polls
2020/10/04 12:22:01 New connection for "py02-80723:europe-west3:polls-instance"
Migrations for 'polls':
  polls/migrations/0001_initial.py
    - Create model Question
    - Create model Choice
2020/10/04 12:22:02 Client closed local connection on 127.0.0.1:3306
(env) walter_obweger@cloudshell:~/github/python-docs-samples/appengine/standard_python3/django (py02-80723)$ python manage.py migrate
2020/10/04 12:22:13 New connection for "py02-80723:europe-west3:polls-instance"
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, polls, sessions
Running migrations:
  Applying contenttypes.0001_initial... OK
  Applying auth.0001_initial... OK
  Applying admin.0001_initial... OK
  Applying admin.0002_logentry_remove_auto_add... OK
  Applying admin.0003_logentry_add_action_flag_choices... OK
  Applying contenttypes.0002_remove_content_type_name... OK
  Applying auth.0002_alter_permission_name_max_length... OK
  Applying auth.0003_alter_user_email_max_length... OK
  Applying auth.0004_alter_user_username_opts... OK
  Applying auth.0005_alter_user_last_login_null... OK
  Applying auth.0006_require_contenttypes_0002... OK
  Applying auth.0007_alter_validators_add_error_messages... OK
  Applying auth.0008_alter_user_username_max_length... OK
  Applying auth.0009_alter_user_last_name_max_length... OK
  Applying auth.0010_alter_group_name_max_length... OK
  Applying auth.0011_update_proxy_permissions... OK
  Applying auth.0012_alter_user_first_name_max_length... OK
  Applying polls.0001_initial... OK
  Applying sessions.0001_initial... OK
2020/10/04 12:22:16 Client closed local connection on 127.0.0.1:3306
(env) walter_obweger@cloudshell:~/github/python-docs-samples/appengine/standard_python3/django (py02-80723)$ python manage.py createsuperuser
2020/10/04 12:22:31 New connection for "py02-80723:europe-west3:polls-instance"
Username (leave blank to use 'walter_obweger'): python manage.py runserver
Error: Enter a valid username. This value may contain only letters, numbers, and @/./+/-/_ characters.
Username (leave blank to use 'walter_obweger'): djroot
Email address: walter.obweger@gmail.com
Password: 
Password (again): 
The password is too similar to the username.
This password is too short. It must contain at least 8 characters.
Bypass password validation and create user anyway? [y/N]: n
Password: 
Password (again): 
Superuser created successfully.
2020/10/04 12:23:46 Client closed local connection on 127.0.0.1:3306
(env) walter_obweger@cloudshell:~/github/python-docs-samples/appengine/standard_python3/django (py02-80723)$ python manage.py runserver
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
2020/10/04 12:23:56 New connection for "py02-80723:europe-west3:polls-instance"
October 04, 2020 - 12:23:56
Django version 3.1.2, using settings 'mysite.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
^C2020/10/04 12:24:02 Client closed local connection on 127.0.0.1:3306
(env) walter_obweger@cloudshell:~/github/python-docs-samples/appengine/standard_python3/django (py02-80723)$ python manage.py collectstatic

132 static files copied to '/home/walter_obweger/github/python-docs-samples/appengine/standard_python3/django/static'.
(env) walter_obweger@cloudshell:~/github/python-docs-samples/appengine/standard_python3/django (py02-80723)$ gcloud app deploy
Services to deploy:

descriptor:      [/home/walter_obweger/github/python-docs-samples/appengine/standard_python3/django/app.yaml]
source:          [/home/walter_obweger/github/python-docs-samples/appengine/standard_python3/django]
target project:  [py02-80723]
target service:  [default]
target version:  [20201004t122427]
target url:      [https://py02-80723.ey.r.appspot.com]


Do you want to continue (Y/n)?  y

Beginning deployment of service [default]...
╔════════════════════════════════════════════════════════════╗
╠═ Uploading 48 files to Google Cloud Storage               ═╣
╚════════════════════════════════════════════════════════════╝
File upload done.
Updating service [default]...done.                                                                                                                                          
Setting traffic split for service [default]...done.                                                                                                                         
Deployed service [default] to [https://py02-80723.ey.r.appspot.com]

You can stream logs from the command line by running:
  $ gcloud app logs tail -s default

To view your application in the web browser run:
  $ gcloud app browse
(env) walter_obweger@cloudshell:~/github/python-docs-samples/appengine/standard_python3/django (py02-80723)$ gcloud app browse
Did not detect your browser. Go to this link to view your app:
https://py02-80723.ey.r.appspot.com
(env) walter_obweger@cloudshell:~/github/python-docs-samples/appengine/standard_python3/django (py02-80723)$ 
```

djroot
asdflkj5

```shell
```

```shell
```
