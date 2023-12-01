import os
import logging

from utils.constants import (
    LOGGER_VERSION, LOGGER_LEVEL,
    DEFAULT_FILE_LOGGER, LOGGER_FILENAMES
)

LOGGING = {
    'version': LOGGER_VERSION,
    'disable_existing_loggers': False,
    "formatters": {
        "base": {
            "format": "[#] Date & Time: {asctime} | Level: {levelname} | [Message]: {message}",
            "style": "{",
            'datefmt': '%Y-%m-%d %H:%M:%S'
        }
    },
    'handlers': {
        'create_user_for_staff': {
            "formatter": "base",
            'level': LOGGER_LEVEL['info'],
            'class': DEFAULT_FILE_LOGGER,
            'filename': LOGGER_FILENAMES['users'],
        },
        'log_user_deleted': {
            "formatter": "base",
            'level': LOGGER_LEVEL['warning'],
            'class': DEFAULT_FILE_LOGGER,
            'filename': LOGGER_FILENAMES['users'],
        },
        'log_staff_deleted': {
            "formatter": "base",
            'level': LOGGER_LEVEL['warning'],
            'class': DEFAULT_FILE_LOGGER,
            'filename': LOGGER_FILENAMES['staffs'],
        },
        'update_settiings': {
            "formatter": "base",
            'level': LOGGER_LEVEL['info'],
            'class': DEFAULT_FILE_LOGGER,
            'filename': LOGGER_FILENAMES['settings'],
        },
        'upload_document': {
            "formatter": "base",
            'level': LOGGER_LEVEL['info'],
            'class': DEFAULT_FILE_LOGGER,
            'filename': LOGGER_FILENAMES['documents'],
        },
        'docs_delete': {
            "formatter": "base",
            'level': LOGGER_LEVEL['warning'],
            'class': DEFAULT_FILE_LOGGER,
            'filename': LOGGER_FILENAMES['documents'],
        },
    },
    'loggers': {
        'user_create_logger': {
            'handlers': ['create_user_for_staff'],
            'level': LOGGER_LEVEL['info'],
            'propagate': True,
        },
        'user_delete_logger': {
            'handlers': ['log_user_deleted'],
            'level': LOGGER_LEVEL['warning'],
            'propagate': True,
        },
        'staff_delete_logger': {
            'handlers': ['log_staff_deleted'],
            'level': LOGGER_LEVEL['warning'],
            'propagate': True,
        },
        'settings_logger': {
            'handlers': ['update_settiings'],
            'level': LOGGER_LEVEL['info'],
            'propagate': True,
        },
        'settings_logger': {
            'handlers': ['update_settiings'],
            'level': LOGGER_LEVEL['info'],
            'propagate': True,
        },
        'document_upload_logger': {
            'handlers': ['upload_document'],
            'level': LOGGER_LEVEL['info'],
            'propagate': True,
        },
        'deleted_document_logger': {
            'handlers': ['docs_delete'],
            'level': LOGGER_LEVEL['warning'],
            'propagate': True,
        },
    },
}
