# Phantasia (uwu.so)

Heavily opinionated image and file uploader server, built with Nuxt and FastAPI. The ultimate successor of [Imagination Server](https://github.com/GoofyGoofsterClub/imagination-server).

## Dependencies

1. Node.js 24 + pnpm/npm  
2. Python 3.13
3. Docker  
4. PostgreSQL  

## Contributing

We welcome all contributors, but keep in mind that new features are often met with significant pushback from an active user base.

For code standards, use the config provided for `Prettier`.

## Setup

Make sure to install the dependencies.

```bash
# Install Node.js, Python, PostgreSQL.
# ...

# Install and run node dependencies
cd frontend
pnpm install # or npm install
pnpm run dev

# Install python dependencies and run API
cd api
pip install -r requirements.txt
uvicorn src.main:app --reload
```

When working locally, dont forget to run `aerich upgrade` in `api` directory to migrate database changes to your local environment.

### Nginx Setup

For local development it's recommended to setup local domains through mDNS or `/etc/hosts`.

Needed configuration for `/etc/hosts` is provided in `nginx/local.hosts` file.

* `@` / `www` - frontend (TypeScript/Nuxt)
* `api` - API interface (Python/FastAPI)
* `i` - Filesystem (SeaweedFS/S3)

After setting up local domains it is advised to setup local certificates using `mkcert`:

```bash
$ mkcert -install
$ mkcert uwu.local api.uwu.local i.uwu.local stats.uwu.local
$ mv uwu.local+3.pem ./nginx/certificates/uwu.local.pem
$ mv uwu.local+3-key.pem ./nginx/certificates/uwu.local-key.pem
```

#### Production

Point `uwu.so`, `www.uwu.so`, `i.uwu.so`, and `api.uwu.so` to the server. Any additional domains need to be specified within `default.conf` following the same schema. Having different subdomains will result in unexpected errors.

After pointing domains to the correct server you will have to copy your SSL certificates in `nginx/certificates` and be renamed to `uwu.local.pem` (certificate) and `uwu.local-key.pem` (private key) respectively.

If you do not have SSL certificate generate it using `certbot` and **NOT** `mkcert` as it's not designed for production environment.

#### Staging

Point `staging.uwu.so`, `i.staging.uwu.so`, and `api.staging.uwu.so` to the server. Any additional domains need to be specified within `default.conf` following the same schema. Having different subdomains will result in unexpected errors.

Make sure that your SSL certificate allows for use of the specified subdomains.

If you do not have SSL certificate generate it using `mkcert`, like this:

```bash
$ mkcert staging.uwu.so api.staging.uwu.so i.staging.uwu.so
```

or if you want to host both production and staging on one server please use:

For any exposed domains it is recommended to use `certbot` instead of `mkcert`.

```bash
$ mkcert uwu.so www.uwu.so staging.uwu.so api.uwu.so api.staging.uwu.so i.uwu.so i.staging.uwu.so
```

#### Statistics (Grafana dashboards)

To expose the Grafana dashboards it needs to be exposed separately from the rest of the services as it's completely optional. It's recommended to use a reverse proxy to expose it.

## Migrating from Imagination Server

Because this is a major update from Imagination Server—both in technologies used and the performance improvements these bring—both are incompatible, and there is no guarantee that any data from Imagination Server will be usable on Phantasia.

Currently there is no migration path from Imagination Server to Phantasia, however the semi-automatic migration script will be added and instructions appended to this README in the future.