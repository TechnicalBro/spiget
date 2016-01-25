from __future__ import (absolute_import, division,
                        print_function, unicode_literals)
from builtins import *
import requests

__config = {
    'domain': 'http://api.spiget.org',
    'version': 'v1',
    'userAgent': 'Spiget-PythonAPI/0.0.1',
}


def __build_api_url():
    return "%s/%s" % (__config['domain'], __config['version'])


def __get_header_dict():
    return {'user-agent': __config['userAgent']}


#
# def get_api_url(uri, params=None):
#     if not params:
#         params = []
#     url = "%s/%s" % (__build_api_url(), uri)
#     print("Debug: API Url is %s" % url)
#     if params is not None and isinstance(params, list) and len(params) > 0:
#         params = "/".join(param for param in params)
#         print("Debug: Parameters are %s" % params)
#         url += params
#     return url

def get_api_url(uri):
    url = "%s/%s" % (__build_api_url(), uri)
    print("Debug -> API Url is %s" % url)
    return url


def get_resources(size=100):
    r = requests.get(get_api_url('resources/'), params={"size": size}, headers=__get_header_dict())
    return r.json()


def get_resource(id, version=None):
    r = None
    if version is not None:
        r = requests.get(get_api_url('resources/%s/versions/%s' % (id, version)), headers=__get_header_dict())
    else:
        r = requests.get(get_api_url('resources/%s' % id), headers=__get_header_dict())

    return r.json()


def get_resource_download(id, version="latest"):
    r = requests.get(get_api_url('resources/%s/versions/%s/download' % (id, version)), headers=__get_header_dict())
    return r.json()


def get_resource_author(id):
    r = requests.get(get_api_url('resources/%s/author' % id), headers=__get_header_dict())
    return r.json()


def get_new_resources(size=25):
    r = requests.get(get_api_url('resources/new'), params={"size": size}, headers=__get_header_dict())
    return r.json()


def get_categories(sub_category=""):
    r = requests.get(get_api_url('categories/%s' % sub_category), headers=__get_header_dict())
    return r.json()


def get_category_resources(category, size=None):
    r = None
    if size is not None and size > 0:
        r = requests.get(get_api_url('categories/%s/resources' % category), params={"size": size},
                         headers=__get_header_dict())
    else:
        r = requests.get(get_api_url('categories/%s/resources' % category), headers=__get_header_dict())
    return r.json()


def get_authors(size=None):
    r = None
    if size is not None and size > 0:
        r = requests.get(get_api_url('authors'), params={'size': size}, headers=__get_header_dict())
    else:
        r = requests.get(get_api_url('authors'), headers=__get_header_dict())

    return r.json()


def get_author_details(id):
    r = requests.get(get_api_url('authors/%s' % id), headers=__get_header_dict())
    return r.json()


def get_author_resources(id):
    r = requests.get(get_api_url('authors/%s/resources' % id), headers=__get_header_dict())
    return r.json()


def get_new_authors(size=None):
    r = None
    if size is not None:
        r = requests.get(get_api_url('authors/new'), params={"size": size}, headers=__get_header_dict())
    else:
        r = requests.get(get_api_url('authors/new'), headers=__get_header_dict())

    return r.json()


def search_resources(query, field=None):
    r = None
    if field is not None:
        r = requests.get(get_api_url('search/resources/%s/%s' % (query, field)), headers=__get_header_dict())
    else:
        r = requests.get(get_api_url('search/resources/%s' % query), headers=__get_header_dict())
    return r.json()


def search_author(query):
    r = requests.get(get_api_url('search/authors/%s' % query), headers=__get_header_dict())
    return r.json()