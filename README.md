# Phantasia (uwu.so)

Heavily opinionated image and file uploader server, built with Nuxt and FastAPI. Ultimate successor of [Imagination Server](https://github.com/GoofyGoofsterClub/imagination-server)

## Dependencies

1. NodeJs + pnpm/npm
2. Python
3. Docker
4. PostgreSQL

## Contributing

We welcome all contributors, but keep in mind that new features are introduced with a lot of retaliation from an active user base.

For code standards use the config provided for `Prettier`.

## Setup

Make sure to install dependencies.

```bash
#  Install NodeJS, Python, PostgreSQL.
# ...

# install and run node dependencies
cd frontend
pnpm install # or npm install
pnpm run dev

# install python dependencies and run api
cd api
pip install -r requirements.txt
uvicorn src.main:app --reload
```