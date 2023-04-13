def get_preferred_option(task_1, task_2):
    if task_1.description == "Wash Dishes":
        if task_2.description == "Cook Dinner":
            return f"first: {task_1.description}, second: {task_2.description}"
        else:
            return f"first: {task_2.description}, second: {task_1.description}"
        
    elif task_1.description == "Cook Dinner":
        if task_2.description == "Clean Windows":
            return f"first: {task_1.description}, second: {task_2.description}"
        else:
            return f"first: {task_2.description}, second: {task_1.description}"
        
    elif task_1.description == "Clean Windows":
        if task_2.description == "Wash Dishes":
            return f"first: {task_1.description}, second: {task_2.description}"
        else:
            return f"first: {task_2.description}, second: {task_1.description}"
        
def get_preferred_options_extension(preference_1, preference_2, preference_lists):
    if preference_1.description in preference_lists :
        if preference_2.description in preference_lists[preference_1.description]:
                return f"{preference_1.description} is preferred over {preference_2.description}"
        
        elif preference_1.description in preference_lists[preference_2.description]:
            return f"{preference_2.description} is preferred over {preference_1.description}"