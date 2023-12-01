from split_settings.tools import optional, include

all_settings = [
    'base.py',
    'apps_list.py',
    'database.py',
    'api.py',
    'logger_settings.py',
]

include(*all_settings)
