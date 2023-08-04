'''
    -- Crea un planificador de tareas usando closures --
    En este desafío, implementarás la lógica de un planificador de tareas en Python. El objetivo es construir la función closure llamada 
    createTaskPlanner, que devolverá una serie de métodos para administrar las tareas. A continuación, se detallan los métodos que deben implementarse:

    :) addTask(task): recibe un diccionario que contiene la información de la tarea y la agrega al array de tareas. El diccionario debe contener las 
       siguientes claves: 'id', 'name', 'priority', 'tags' y 'completed'. La clave 'completed' se establecerá automáticamente como False al agregar una tarea.

    :) removeTask(value): recibe el id o nombre de la tarea y la elimina del array de tareas.

    :) getTasks(): devuelve el array de tareas.

    :) getPendingTasks(): devuelve solo las tareas pendientes.

    :) getCompletedTasks(): devuelve solo las tareas completadas.

    :) markTaskAsCompleted(value): recibe el id o nombre de la tarea y la marca como completada.

    :) getSortedTasksByPriority(): devuelve una copia de las tareas ordenadas según su prioridad (3: poco urgente, 2: urgente, 1: muy urgente), sin modificar 
    la lista original de tareas.

    :) filterTasksByTag(tag): filtra las tareas por una etiqueta específica. 
    
    :) updateTask(taskId, updates): busca la tarea correspondiente al id especificado y actualiza sus propiedades con las especificadas en el diccionario de actualizaciones.
'''


def createTaskPlanner():
    tasks = []

    def addTask(task):
        task['completed'] = False
        tasks.append(task)

    def removeTask(value):
        # Para acceder al valor de un objeto que ha sido creado en un ámbito anterior (exterior).
        nonlocal tasks
        for task in tasks:
            if task['id'] == value or task['name'] == value:
                tasks.remove(task)

    def getTasks():
        return tasks

    def getPendingTasks():
        nonlocal tasks
        return [task for task in tasks if task['completed'] != True]

    def getCompletedTasks():
        nonlocal tasks
        return [task for task in tasks if task['completed'] == True]

    def markTaskAsCompleted(value):
        nonlocal tasks
        for task in tasks:
            if task['id'] == value or task['name'] == value:
                task['completed'] = True

    def getSortedTasksByPriority():
        sorted_tasks = sorted(tasks, key=lambda task: task['priority'])
        return sorted_tasks

    def filterTasksByTag(tag):
        return [task for task in tasks if tag in task['tags']]
        # Another solution (filter):
        # return list(filter(lambda task: tag in task['tags'], tasks))

    def updateTask(taskId, updates):
        for task in tasks:
            if task['id'] == taskId:
                for key, value in updates.items():
                    task[key] = value

    return {'addTask': addTask,
            'removeTask': removeTask,
            'getTasks': getTasks,
            'getPendingTasks': getPendingTasks,
            'getCompletedTasks': getCompletedTasks,
            'markTaskAsCompleted': markTaskAsCompleted,
            'getSortedTasksByPriority': getSortedTasksByPriority,
            'filterTasksByTag': filterTasksByTag,
            'updateTask': updateTask
            }


planner = createTaskPlanner()

planner['addTask']({
    'id': 1,
    'name': 'Comprar libros',
    'priority': 1,
    'tags': ['shopping', 'library']
})

planner['addTask']({
    'id': 2,
    'name': 'Llamar a Juan',
    'priority': 3,
    'tags': ['personal']
})

planner['markTaskAsCompleted']('Llamar a Juan')

print(planner['getCompletedTasks']())
