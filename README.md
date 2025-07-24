# Phantasia (uwu.so)

Heavily opinionated image and file uploader server, built with Nuxt and FastAPI. The ultimate successor of [Imagination Server](https://github.com/GoofyGoofsterClub/imagination-server).

## Dependencies

1. Node.js + pnpm/npm  
2. Python  
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

### Nginx Setup

* `@` / `www` - frontend (TypeScript/Nuxt)
* `api` - API interface (Python/FastAPI)
* `i` - Filesystem (SeaweedFS/S3)

#### Production

Point `uwu.so`, `www.uwu.so`, `i.uwu.so`, and `api.uwu.so` to the server.

#### Staging

Point `staging.uwu.so`, `i.staging.uwu.so`, and `api.staging.uwu.so` to the server.

## Migrating from Imagination Server

Because this is a major update from Imagination Server—both in technologies used and the performance improvements these bring—both are incompatible, and there is no guarantee that any data from Imagination Server will be usable on Phantasia.