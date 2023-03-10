# coding: utf-8

"""
    ECE 461 - Fall 2021 - Project 2

    API for ECE 461/Fall 2021/Project 2: A Trustworthy Module Registry  # noqa: E501

    OpenAPI spec version: 2.0.0
    Contact: davisjam@purdue.edu
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from swagger_client.api_client import ApiClient


class DefaultApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_auth_token(self, body, **kwargs):  # noqa: E501
        """create_auth_token  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_auth_token(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param AuthenticationRequest body: (required)
        :return: AuthenticationToken
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_auth_token_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.create_auth_token_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def create_auth_token_with_http_info(self, body, **kwargs):  # noqa: E501
        """create_auth_token  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_auth_token_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param AuthenticationRequest body: (required)
        :return: AuthenticationToken
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_auth_token" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `create_auth_token`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/authenticate', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AuthenticationToken',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def package_by_name_delete(self, name, **kwargs):  # noqa: E501
        """Delete all versions of this package.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.package_by_name_delete(name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param PackageName name: (required)
        :param AuthenticationToken x_authorization:
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.package_by_name_delete_with_http_info(name, **kwargs)  # noqa: E501
        else:
            (data) = self.package_by_name_delete_with_http_info(name, **kwargs)  # noqa: E501
            return data

    def package_by_name_delete_with_http_info(self, name, **kwargs):  # noqa: E501
        """Delete all versions of this package.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.package_by_name_delete_with_http_info(name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param PackageName name: (required)
        :param AuthenticationToken x_authorization:
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['name', 'x_authorization']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method package_by_name_delete" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'name' is set
        if ('name' not in params or
                params['name'] is None):
            raise ValueError("Missing the required parameter `name` when calling `package_by_name_delete`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'name' in params:
            path_params['name'] = params['name']  # noqa: E501

        query_params = []

        header_params = {}
        if 'x_authorization' in params:
            header_params['X-Authorization'] = params['x_authorization']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/package/byName/{name}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def package_by_name_get(self, name, **kwargs):  # noqa: E501
        """package_by_name_get  # noqa: E501

        Return the history of this package (all versions).  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.package_by_name_get(name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param PackageName name: (required)
        :param AuthenticationToken x_authorization:
        :return: list[PackageHistoryEntry]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.package_by_name_get_with_http_info(name, **kwargs)  # noqa: E501
        else:
            (data) = self.package_by_name_get_with_http_info(name, **kwargs)  # noqa: E501
            return data

    def package_by_name_get_with_http_info(self, name, **kwargs):  # noqa: E501
        """package_by_name_get  # noqa: E501

        Return the history of this package (all versions).  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.package_by_name_get_with_http_info(name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param PackageName name: (required)
        :param AuthenticationToken x_authorization:
        :return: list[PackageHistoryEntry]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['name', 'x_authorization']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method package_by_name_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'name' is set
        if ('name' not in params or
                params['name'] is None):
            raise ValueError("Missing the required parameter `name` when calling `package_by_name_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'name' in params:
            path_params['name'] = params['name']  # noqa: E501

        query_params = []

        header_params = {}
        if 'x_authorization' in params:
            header_params['X-Authorization'] = params['x_authorization']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/package/byName/{name}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[PackageHistoryEntry]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def package_create(self, body, x_authorization, **kwargs):  # noqa: E501
        """package_create  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.package_create(body, x_authorization, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Package body: (required)
        :param AuthenticationToken x_authorization: (required)
        :return: PackageMetadata
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.package_create_with_http_info(body, x_authorization, **kwargs)  # noqa: E501
        else:
            (data) = self.package_create_with_http_info(body, x_authorization, **kwargs)  # noqa: E501
            return data

    def package_create_with_http_info(self, body, x_authorization, **kwargs):  # noqa: E501
        """package_create  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.package_create_with_http_info(body, x_authorization, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Package body: (required)
        :param AuthenticationToken x_authorization: (required)
        :return: PackageMetadata
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'x_authorization']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method package_create" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `package_create`")  # noqa: E501
        # verify the required parameter 'x_authorization' is set
        if ('x_authorization' not in params or
                params['x_authorization'] is None):
            raise ValueError("Missing the required parameter `x_authorization` when calling `package_create`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_authorization' in params:
            header_params['X-Authorization'] = params['x_authorization']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/package', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='PackageMetadata',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def package_delete(self, id, **kwargs):  # noqa: E501
        """Delete this version of the package.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.package_delete(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param PackageID id: Package ID (required)
        :param AuthenticationToken x_authorization:
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.package_delete_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.package_delete_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def package_delete_with_http_info(self, id, **kwargs):  # noqa: E501
        """Delete this version of the package.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.package_delete_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param PackageID id: Package ID (required)
        :param AuthenticationToken x_authorization:
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'x_authorization']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method package_delete" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `package_delete`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []

        header_params = {}
        if 'x_authorization' in params:
            header_params['X-Authorization'] = params['x_authorization']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/package/{id}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def package_rate(self, id, **kwargs):  # noqa: E501
        """package_rate  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.package_rate(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param PackageID id: (required)
        :param AuthenticationToken x_authorization:
        :return: PackageRating
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.package_rate_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.package_rate_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def package_rate_with_http_info(self, id, **kwargs):  # noqa: E501
        """package_rate  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.package_rate_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param PackageID id: (required)
        :param AuthenticationToken x_authorization:
        :return: PackageRating
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'x_authorization']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method package_rate" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `package_rate`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []

        header_params = {}
        if 'x_authorization' in params:
            header_params['X-Authorization'] = params['x_authorization']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/package/{id}/rate', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='PackageRating',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def package_retrieve(self, id, **kwargs):  # noqa: E501
        """package_retrieve  # noqa: E501

        Return this package.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.package_retrieve(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param PackageID id: ID of package to fetch (required)
        :param AuthenticationToken x_authorization:
        :return: Package
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.package_retrieve_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.package_retrieve_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def package_retrieve_with_http_info(self, id, **kwargs):  # noqa: E501
        """package_retrieve  # noqa: E501

        Return this package.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.package_retrieve_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param PackageID id: ID of package to fetch (required)
        :param AuthenticationToken x_authorization:
        :return: Package
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'x_authorization']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method package_retrieve" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `package_retrieve`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []

        header_params = {}
        if 'x_authorization' in params:
            header_params['X-Authorization'] = params['x_authorization']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/package/{id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Package',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def package_update(self, body, id, **kwargs):  # noqa: E501
        """Update this version of the package.  # noqa: E501

        The name, version, and ID must match.  The package contents (from PackageData) will replace the previous contents.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.package_update(body, id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Package body: (required)
        :param PackageID id: (required)
        :param AuthenticationToken x_authorization:
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.package_update_with_http_info(body, id, **kwargs)  # noqa: E501
        else:
            (data) = self.package_update_with_http_info(body, id, **kwargs)  # noqa: E501
            return data

    def package_update_with_http_info(self, body, id, **kwargs):  # noqa: E501
        """Update this version of the package.  # noqa: E501

        The name, version, and ID must match.  The package contents (from PackageData) will replace the previous contents.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.package_update_with_http_info(body, id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Package body: (required)
        :param PackageID id: (required)
        :param AuthenticationToken x_authorization:
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'id', 'x_authorization']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method package_update" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `package_update`")  # noqa: E501
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `package_update`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []

        header_params = {}
        if 'x_authorization' in params:
            header_params['X-Authorization'] = params['x_authorization']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/package/{id}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def packages_list(self, body, **kwargs):  # noqa: E501
        """Get packages  # noqa: E501

        Get any packages fitting the query.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.packages_list(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param list[PackageQuery] body: (required)
        :param AuthenticationToken x_authorization:
        :param EnumerateOffset offset: Provide this for pagination. If not provided, returns the first page of results.
        :return: list[PackageMetadata]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.packages_list_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.packages_list_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def packages_list_with_http_info(self, body, **kwargs):  # noqa: E501
        """Get packages  # noqa: E501

        Get any packages fitting the query.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.packages_list_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param list[PackageQuery] body: (required)
        :param AuthenticationToken x_authorization:
        :param EnumerateOffset offset: Provide this for pagination. If not provided, returns the first page of results.
        :return: list[PackageMetadata]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'x_authorization', 'offset']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method packages_list" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `packages_list`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'offset' in params:
            query_params.append(('offset', params['offset']))  # noqa: E501

        header_params = {}
        if 'x_authorization' in params:
            header_params['X-Authorization'] = params['x_authorization']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/packages', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[PackageMetadata]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def registry_reset(self, **kwargs):  # noqa: E501
        """registry_reset  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.registry_reset(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param AuthenticationToken x_authorization:
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.registry_reset_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.registry_reset_with_http_info(**kwargs)  # noqa: E501
            return data

    def registry_reset_with_http_info(self, **kwargs):  # noqa: E501
        """registry_reset  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.registry_reset_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param AuthenticationToken x_authorization:
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['x_authorization']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method registry_reset" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_authorization' in params:
            header_params['X-Authorization'] = params['x_authorization']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/reset', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
