pre-commit install

# copy settings 
cp .devcontainer/local_settings.py froide/

# Create a superuser
python manage.py createsuperuser --no-input # see environment variables in docker-compose.dev.yml

# Create and populate search index
python manage.py search_index --create
python manage.py search_index --populate
