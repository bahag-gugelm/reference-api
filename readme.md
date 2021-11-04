# API for EAN to internal PIM SKUs resolution

## Usage


### Request

```
curl -X 'GET' \
  'http://host:port/pim_ean/4078500017244' \
  -H 'accept: application/json' \
  -H 'X-Token: access_token'
```

### Response

```
{
  "id": 490226,
  "variant_product": "23711105",
  "base_product": "1543330",
  "material_group": "7315",
  "ean": "4078500017244"
}
```

### For automated queries, use the following snippet:

```
from requests import Session

def get_sku_by_ean(ean: str) -> dict:
    session = Session()
    session.headers = {'X-Token': 'token'}
        
    with session as client:
        response = client.get(f'https://reference-api-mbhqfkchoq-ew.a.run.app/pim_ean/{ean}')
        response.raise_for_status()
        return response.json()
```

## How to run the app locally

````
$ docker-compose up -d --build
````

and go to http://localhost:8000/docs

## Development

- setup virtualenv for the local develpoment
- install the requirements
- make .env file with the following local config parameters
```
API_KEY="secret_string"
SERVER_NAME="reference_api"
SERVER_HOST="http://localhost:8000"
POSTGRES_SERVER="35.233.0.181"
POSTGRES_USER="user"
POSTGRES_PASSWORD="password"
POSTGRES_DB="reference"
```

- if the app-container still runs, stop it to avoid hosts/IPs conflicts etc.
- start the app manually
````
$ uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
````
- rebuild app image to push your changes into the conainer
- use local postgres db

Always generate migrations after altering the db-schema,
migrations should be included into correspondent commit
````
$ alembic revision --autogenerate -m "changes msg"
````
Manually apply migrations (up to the latest)
````
$ alembic upgrade head
````

## How to run tests

````
$ docker-compose exec app python -m pytest app/tests
````
