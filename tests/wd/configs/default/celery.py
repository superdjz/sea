broker_url = 'redis://localhost:6379/2'

task_queues = {
    '{{ project }}.direct': {
        'exchange': '{{ project }}-exchange',
        'exchange_type': 'direct',
        'routing_key': '{{ project }}.direct',
    },
}

task_default_queue = '{{ project }}.celery'

task_routes = {
    'app.tasks.*': {
        'queue': task_default_queue,
    },
}
