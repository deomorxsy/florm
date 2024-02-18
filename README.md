# vlusk-primer
> Simple fullstack and monorepo PoC for data visualization, using Python/Flask, Node/Vue.js and Postgres, deployed as containers handling backend, frontend and database. Test it locally with docker-compose/k3s, running the individual container images or via scripts.

container images at [hub]()

Featuring:
- Backend:Python/Flask
    - ~Session-Cookie Authentication: flask_login~
    - PyJWT
- Frontend: Node/Vue.js
    - Build tooling: Vite
    - Validation: vee-validate, yup, “@vee-validate/yup”
    - Routing: vue-router
    - Visualization: vue-chartjs
    - Visualization: vue-chart.js
- Database ORM: SQLAlchemy
    - postgres for dataframe storage
    - sqlite3 for session cache [?]



## Frontend

Scaffolding generated with create-vite@5.1.3:

```sh
; npm create vite@5.1.3 frontend/ -- --template vue-ts
;
; npm install vee-validate@4.12.5 yup@1.3.3 vue-router@4.2.5 vue-router@4.2.5 axios@1.6.7
;
; npm run dev

```
## Database
### Standalone container

Run the container process with the database
```sh
podman run -it -p=5432:5432 --name dbdrop -d \
    -e POSTGRES_USER=admin \
    -e POSTGRES_PASSWORD=Passw0rd \
    -v /mnt/ssd/dataStore/containers/database/pgad-pod/pgdata:/var/lib/postgresql/data:Z \
    docker.io/library/postgres:16.0
```

Connect psql to the process, create the schema and populate the database. The loop below reads all files under the database directory in alphanumeric order, so you can always tell that the reading respects precedence.
```sh
# Create schema with Raw SQL script then populate the database
#psql -U admin -d database_name -f=file.sql

for f in *.sql;
do
    psql -U admin -d dbdrop -f "$f"
done
```


## Backend
### Running in Standalone mode

Make sure to set the virtualenv:
```sh
; git clone git@github.com:isi23drop/vlusk-primer.git
; python3 -m venv venv
```

Prepare the environment:
```sh
; cd ./vlusk/backend/
; source ../venv/bin/activate
; pip3 install --upgrade pip
; pip3 install -r ./requirements.txt

```

Now that all dependencies are installed, just run each process from a different terminal:

1. database migration
```sh
flask --app app init-db
```

2. PS: now in flask 3.0 the FLASK_ENV is deprecated alongside the debug mode that goes back to the framework on the CLI call, hence the flag "--debug".
```sh
cd ./app/
flask --debug run
```

### Podman Service and DOCKER_HOST
[compose](https://docs.docker.com/compose/) concentrates in orchestrating multiple containers in a single host. To do this with k8s, you would need kind, k3s (does not use virtualization) or similar. It was made to be compatible with other OCI runtimes, such as Podman, which was one of the first to enable rootless containers, and can be setup with compose using the Podman Service's systemd unit file for unix sockets.

The orchestration tool ```docker-compose``` supports Podman Service through the DOCKER_HOST environment variable. This makes it possible to run containers with podman but with the benefit of rootless.

Source the [script](./scripts/podman-service-compose.sh) and run it to run compose with podman:

```sh
; source ./scripts/podman-service-compose.sh
```


### Running with the podman-compose script


## Running with k8s
Kubernetes is a container orchestrator. To run this project on single host just like the Compose tool, you can use tools like kind or k3s (which don't use virtualization).
