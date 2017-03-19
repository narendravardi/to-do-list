from db_operations import get_user_details, update_new_task_to_dynamodb, create_user_in_db, update_pending_tasks_in_db


def has_user_signedup(email):
    if get_user_details(email) is None:
        return "true"
    else:
        return "false"


def is_valid_login_password(email, hashed_password):
    '''verify if the email_id and password provided by the user are equal to the existing credentials'''
    dynamodb_email = get_user_details(email)[u'email']
    dynamodb_password = get_user_details(email)[u'password']
    if dynamodb_email == email and dynamodb_password == hashed_password:
        return True
    else:
        return False


def get_all_tasks(email):
    user_data = get_user_details(email)
    if "pending_tasks" in user_data and "completed_tasks" in user_data:
        return {"pending_tasks": user_data['pending_tasks'], "completed_tasks": user_data['completed_tasks']}
    elif "pending_tasks" in user_data:
        return user_data
    elif "completed_tasks" in user_data:
        return user_data
    else:
        return {"pending_tasks": None, "completed_tasks": None}


def update_new_task(new_task_title_value, new_task_description_value, email):
    user_data = get_user_details(email)
    if len(user_data['pending_tasks']) != 0:
        pending_tasks = user_data['pending_tasks']
        pending_tasks_count = len(pending_tasks)
        pending_tasks.append(
            {'id': pending_tasks_count + 1, 'title': new_task_title_value, 'description': new_task_description_value})
    else:
        user_data['pending_tasks'].append(
            {'id': 1, 'title': new_task_title_value, 'description': new_task_description_value})
    update_new_task_to_dynamodb(user_data)


def create_user(email, password):
    create_user_in_db(email, password)


def get_user_details_helper(email):
    return get_user_details(email)


def mark_task_as_pending_helper(task_id, email):
    print 'mark_task_as_pending_helper', mark_task_as_pending_helper
    user_details = get_user_details(email)
    pending_tasks_after_toggle = []
    completed_tasks_after_toggle = []

    print 'user_details', user_details
    if 'completed_tasks' in user_details:
        print 'completed_tasks', user_details['completed_tasks']
        for task in user_details['completed_tasks']:
            if int(task['id']) != int(task_id):
                print task['id'], task_id
                completed_tasks_after_toggle.append(task)
            else:
                pending_tasks_after_toggle.append(task)
    if 'pending_tasks' in user_details:
        for task in user_details['pending_tasks']:
            pending_tasks_after_toggle.append(task)
    update_pending_tasks_in_db(completed_tasks_after_toggle, pending_tasks_after_toggle, email)
    return 'true'


def mark_task_as_complete_helper(task_id, email):
    user_details = get_user_details(email)
    pending_tasks_after_toggle = []
    completed_tasks_after_toggle = []
    if 'pending_tasks' in user_details:
        for task in user_details['pending_tasks']:
            # print task['id'], task_id
            if int(task['id']) != int(task_id):
                # typecast above values with int as the types are as follows <class 'decimal.Decimal'> <type 'unicode'>
                # print type(task['id']),type(task_id)
                # print task['id'],task_id
                pending_tasks_after_toggle.append(task)
            else:
                completed_tasks_after_toggle.append(task)
    # print 'pending_task',user_details['pending_tasks']
    # print 'pending_tasks_after_toggle',pending_tasks_after_toggle
    if 'completed_tasks' in user_details:
        for task in user_details['completed_tasks']:
            completed_tasks_after_toggle.append(task)
    update_pending_tasks_in_db(completed_tasks_after_toggle, pending_tasks_after_toggle, email)
    return 'true'
