import config


def url_builder(variable, resource, context):
    return config.BASE_URL + '/' + resource + '/' + variable + '/' + context + config.FORMAT


api_response_data = {
    "ResultsOrderedBy": "email|list|date default:email",
    "OrderDirection": "asc|desc default:asc",
    "PageNumber": 'int',
    "PageSize": 'int default:1000',
    "RecordsOnThisPage": 'int',
    "TotalNumberOfRecords": 'int',
    "NumberOfPages": 'int'
}
