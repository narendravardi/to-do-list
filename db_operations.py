import boto3
from boto3.dynamodb.conditions import Key, Attr
import credentials

dynamodb = boto3.resource(
    'dynamodb',
    aws_access_key_id=credentials.aws_access_key_id,
    aws_secret_access_key=credentials.aws_secret_access_key, region_name=credentials.region_name)

table = dynamodb.Table(credentials.table_name)


# return None if the specified email_id doesnt exists in dynamodb
def get_user_details(email):
    global table;
    get_user_details_response = table.query(
        KeyConditionExpression=Key('email').eq(email)
    )
    if len(get_user_details_response[u'Items']) >= 1:
        return get_user_details_response[u'Items'][0]
    return None


def update_new_task_to_dynamodb(user_data):
    global table
    response = table.update_item(
        Key={
            'email': user_data['email'],
        },
        UpdateExpression="set pending_tasks = :r",
        ExpressionAttributeValues={
            ':r': user_data['pending_tasks']
        },
    )
    return "successfully updated!"


def create_user_in_db(email, password):
    global table
    response = table.put_item(
        Item={
            'email': email,
            'password': password,
            'pending_tasks': [],
            'completed_tasks': []
        }
    )
    return "created user successfully!!!"


def update_pending_tasks_in_db(completed_tasks, pending_tasks, email):
    global table
    response = table.update_item(
        Key={
            'email': email
        },
        UpdateExpression="set pending_tasks = :p, completed_tasks = :c",
        ExpressionAttributeValues={
            ':p': pending_tasks,
            ':c': completed_tasks
        },
        ReturnValues="UPDATED_NEW"
    )
