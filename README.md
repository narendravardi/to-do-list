# to-do-list
A Simple To-Do list web application using Flask and JQuery. Feel free to check this webapp at http://task-todo.herokuapp.com

## Getting Started

All the requirements for this application are listed in requirements.txt. To get up and running, preferably using a `pip`, run: `pip install -r requirements.txt`.

Before running the application create a file named `credentials.py`. 
* Create `IAM User` with DynamoDB `*` permissions. Now, add the following details to the `credentials.py` file
```
aws_access_key_id = "AWS_ACCESS_KEY_ID"
aws_secret_access_key = 'AWS_SECRET_KEY_ID'
region_name = 'REGION_IN_WHICH_DYNAMODB_TABLE_IS_CREATED'
app_secret_key = 'APP_SECRET_KEY'
table_name = 'TABLE_NAME'
```

If you trying learn `Flask`, start from `app.py`. 
For JQuery, `static` folder is all yours.
