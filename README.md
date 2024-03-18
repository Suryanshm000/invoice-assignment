# invoice-assignment

## Screenshots

https://github.com/Suryanshm000/invoice-assignment/assets/65828169/2538e00b-f5c1-4a9a-9faf-56370e81c513


## Running Test suite

<img width="553" alt="invoice-tests" src="https://github.com/Suryanshm000/invoice-assignment/assets/65828169/794f9245-a505-4da6-b6eb-a69c4a9bef26">



## API Reference

**Create invoice API**
```
curl --location --request POST 'http://127.0.0.1:8000/invoices/create/' \
--form 'customer_name="Testuser"' \
--form 'date="2024-03-18"'
```

**View invoice list API**
```
curl --location --request GET 'http://127.0.0.1:8000/invoices/'
```

**View invoice API**
```
curl --location --request GET 'http://127.0.0.1:8000/invoices/<id>/'
```

**Delete invoice API**
```
curl --location --request DELETE 'http://127.0.0.1:8000/invoices/<id>/'
```

**Create invoice-detail API**
```
curl --location --request POST 'http://127.0.0.1:8000/invoice-details/create/' \
--form 'invoice="<invoice-id>"' \
--form 'description="<text>"' \
--form 'quantity="<value>"' \
--form 'unit_price="<value>"' \
--form 'price="<value>"'
```

**View invoice-detail list API**
```
curl --location --request GET 'http://127.0.0.1:8000/invoice-details/'
```

**Delete invoice-detail API**
```
curl --location --request DELETE 'http://127.0.0.1:8000/invoice-details/<id>/'
```

**Update invoice-detail API**
```
curl --location --request PUT 'http://127.0.0.1:8000/invoice-details/<id>/' \
--form 'invoice="<invoice-id>"' \
--form 'description="<text>"' \
--form 'quantity="<value>"' \
--form 'unit_price="<value>"' \
--form 'price="<value>"'
```

**View invoice-detail API**
```
curl --location --request GET 'http://127.0.0.1:8000/invoice-details/<id>/'
```

# Running at localhost

These are the steps to follow in order to run the project on local host: 
<br>

```
git clone https://github.com/Suryanshm000/invoice-assignment.git`
```

```
cd invoice-assignment
```

Virtual Environment setup
```
pip install virtualenv
python -m venv <name of environment>
cd <name of environment>/Scripts
activate
pip install -r requirements.txt
cd ..
cd ..
```

The *django api server* is started via the following command.

```
python manage.py runserver
```


# Command to run the test suite
```
python manage.py test
```
