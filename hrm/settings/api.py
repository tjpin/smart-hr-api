# REST FRAMEWORK [JSONParser, CamelCaseJSONRenderer, CamelCaseBrowsableAPIRenderer]
REST_FRAMEWORK = {
    # 'DEFAULT_FILTER_BACKENDS': (
    #     'rest_framework_filters.backends.RestFrameworkFilterBackend',
    # ),
    "DEFAULT_RENDERER_CLASSES": (
        # 'rest_framework.parsers.JSONParser',
        "djangorestframework_camel_case.render.CamelCaseJSONRenderer",
        "djangorestframework_camel_case.render.CamelCaseBrowsableAPIRenderer",
    ),
    "DEFAULT_PARSER_CLASSES": (
        # 'rest_framework.parsers.JSONParser',
        "djangorestframework_camel_case.parser.CamelCaseFormParser",
        "djangorestframework_camel_case.parser.CamelCaseMultiPartParser",
        "djangorestframework_camel_case.parser.CamelCaseJSONParser",
    ),
    "DATE_INPUT_FORMATS": ["%Y-%m-%d", "iso-8601"],
    "DATETIME_FORMAT": "%Y-%m-%d %H:%M:%S",
    "DATE_FORMAT": "%Y-%m-%d",
    "TIME_FORMAT": "%H:%M:%S",
}
