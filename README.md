# Widget API using Django REST Framework

## Setup

1. Create virtual environment
```bash
python3 -m venv venv
source venv/bin/activate
```

2. Install requirements
```bash
pip install -r requirements.txt
```

3. Apply migrations
```bash
python manage.py migrate
```

4. Run development server
```bash
python manage.py runserver
```

## API Endpoints
- `GET /api/widgets/`
- `POST /api/widgets/`
- `GET /api/widgets/<id>/`
- `PUT /api/widgets/<id>/`
- `DELETE /api/widgets/<id>/`

