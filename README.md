# Bank List and its Branch Details API

This API provides information about banks and their branches. Using Django REST Framework, we expose endpoints to fetch the list of banks and the details of a specific bank branch.

## Endpoints

### 1. **Get Bank List**

**URL:** `/banklist/`

**Method:** `GET`

**Description:**  
This endpoint returns a list of all available banks and its branches.

**Response (200 OK):**
HTTP 200 OK
Allow: GET, OPTIONS
Content-Type: application/json
Vary: Accept
```bash
[
    {
        "bank_name": "BankA",
        "branches": [
           {
                "branch": "branchA1",
                "IFSC": "BankA123"
            },
            {
                "branch": "branchA2",
                "IFSC": "BankA456"
            }
        ]
    },
    {
        "bank_name": "BankB",
        "branches": [
            {
                "branch": "BankB1",
                "IFSC": "BankB10202"
            },
            {
                "branch": "branchB2",
                "IFSC": "BankB2536"
            },
            {
                "branch": "brancbB3",
                "IFSC": "BankB9682"
            }
        ]
    },
    {
        "bank_name": "BankC",
        "branches": [
            {
                "branch": "branchc1",
                "IFSC": "BankC5826"
            }
        ]
    }
]
```
# How it Works
The project is built with Django and Django REST Framework to provide a simple API to fetch the list of banks and their respective branches.

## 1. Models:
We define two models in the Django application:
<ul><li>Bank: A model that stores information about a bank (name).</li>
<li>Branch: A model that stores information about a bank branch (bank, branch, IFSC).</li>
<li>Here we established Foreign Key realtion and related_field to get all branch details in Bank also.</li></ul>

```bash
    bank=models.ForeignKey(Banks,related_name='branches',on_delete=models.CASCADE)
```

## 2. Serializers:
We create serializers to convert model data into JSON format and validate input data:
<ul>
<li>BankSerializer: Converts bank data to JSON format.</li>
    <li>BranchSerializer: Converts branch data to JSON format.</li>
</ul>

  ```bash
   class BankSerializer(ModelSerializer):
        branches=BranchSerializer(many=True)
        class Meta:
            model=Banks
            fields=['bank_name','branches']
 ```

## 3.Views
we create api_view(['GET']) to all banklist and its branch details.
 ```bash
    @api_view(['GET'])
      def banklist(reqeust):
      banks=Banks.objects.all()
      banklist=BankSerializer(banks,many=True)
      return Response(banklist.data)
 ```

## Requirements
- Python 3.8+
- Django 4.x+
- Django REST Framework 3.x+

1. Clone the repository:
    ```bash
    git clone https://github.com/sreenivaskuppala2002/Banks.git
    ```

2. Install dependencies:
    ```bash
    cd <project_name>
    pip install -r requirements.txt
    ```

3. Migrate the database:
    ```bash
    python manage.py migrate
    ```

4. Create a superuser to access the admin panel (optional):
    ```bash
    python manage.py createsuperuser
    ```

5. Run the development server:
    ```bash
    python manage.py runserver
    ```

The API will now be running on `http://127.0.0.1:8000`.
To get banklist endpoint use `http://127.0.0.1:8000\banklist\`.


<h3>Finally deployed application on vercel</h3>
<h3>It took 3 hours to complete total development and deployment </h3>


