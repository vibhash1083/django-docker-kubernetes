# Testing
1. Unit testing
2. Automated testing
3. Manual Testing

## Unit Testing
1. Set up
2. Test
3. Tear down

Run django tests
```
python manage.py test
```

Install coverage
```
pip install coverage
```

Check for coverage
```
coverage run --source=test manage.py test
coverage report -m
```