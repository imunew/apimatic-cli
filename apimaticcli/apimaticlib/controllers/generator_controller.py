# -*- coding: utf-8 -*-

"""
    apimaticlib.controllers.generator_controller

    This file was automatically generated by APIMATIC BETA v2.0 on 09/04/2016
"""

from .base_controller import *



class GeneratorController(BaseController):

    """A Controller to access Endpoints in the apimaticlib API."""

    def __init__(self, http_client = None, http_call_back = None):
        """Constructor which allows a different HTTP client for this controller."""
        BaseController.__init__(self, http_client, http_call_back)

    def get_generate_from_key(self,
                              apikey,
                              template):
        """Does a GET request to /codegen.

        Generates SDK given an API key.

        Args:
            apikey (string): The API key from APIMatic
            template (string): TODO: type description here. Example:
                cs_portable_net_lib

        Returns:
            string: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # The base uri for api requests
        _query_builder = Configuration.BASE_URI
 
        # Prepare query string for API call
        _query_builder += '/codegen'

        # Process optional query parameters
        _query_parameters = {
            'apikey': apikey,
            'template': template
        }
        
        # Validate and preprocess url
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'user-agent': 'APIMATIC 2.0'
        }

        # Prepare the API call.
        _request = self.http_client.get(_query_url, headers=_headers, query_parameters=_query_parameters)

        # Invoke the on before request HttpCallBack if specified
        if self.http_call_back != None:
            self.http_call_back.on_before_request(_request)

        # Invoke the API call  to fetch the response.
        _response = self.http_client.execute_as_string(_request)

        # Wrap the request and the response in an HttpContext object
        _context = HttpContext(_request, _response)

        # Invoke the on after response HttpCallBack if specified
        if self.http_call_back != None:
            self.http_call_back.on_after_response(_context)

        # Global error handling using HTTP status codes.
        self.validate_response(_context)    

        # Return appropriate type
        return _response.raw_body



    def get_generate_from_url(self,
                              name,
                              template,
                              description_url):
        """Does a GET request to /codegen.

        TODO: type endpoint description here.

        Args:
            name (string): TODO: type description here. Example: 
            template (string): TODO: type description here. Example:
                cs_portable_net_lib
            description_url (string): TODO: type description here. Example: 

        Returns:
            string: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # The base uri for api requests
        _query_builder = Configuration.BASE_URI
 
        # Prepare query string for API call
        _query_builder += '/codegen'

        # Process optional query parameters
        _query_parameters = {
            'name': name,
            'template': template,
            'descriptionUrl': description_url
        }
        
        # Validate and preprocess url
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'user-agent': 'APIMATIC 2.0'
        }

        # Prepare the API call.
        _request = self.http_client.get(_query_url, headers=_headers, query_parameters=_query_parameters, username=Configuration.basic_auth_user_name, password=Configuration.basic_auth_password)

        # Invoke the on before request HttpCallBack if specified
        if self.http_call_back != None:
            self.http_call_back.on_before_request(_request)

        # Invoke the API call  to fetch the response.
        _response = self.http_client.execute_as_string(_request)

        # Wrap the request and the response in an HttpContext object
        _context = HttpContext(_request, _response)

        # Invoke the on after response HttpCallBack if specified
        if self.http_call_back != None:
            self.http_call_back.on_after_response(_context)

        # Global error handling using HTTP status codes.
        self.validate_response(_context)    

        # Return appropriate type
        return _response.raw_body



    def create_generate_from_file(self,
                                  name,
                                  template,
                                  file):
        """Does a POST request to /codegen.

        TODO: type endpoint description here.

        Args:
            name (string): TODO: type description here. Example: 
            template (string): TODO: type description here. Example:
                cs_portable_net_lib
            file (string): TODO: type description here. Example: 

        Returns:
            string: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # The base uri for api requests
        _query_builder = Configuration.BASE_URI
 
        # Prepare query string for API call
        _query_builder += '/codegen'

        # Process optional query parameters
        _query_parameters = {
            'name': name,
            'template': template
        }

        _files = {
            'file': file
        }
        
        # Validate and preprocess url
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'user-agent': 'APIMATIC 2.0'
        }

        # Prepare the API call.
        _request = self.http_client.post(_query_url, headers=_headers, query_parameters=_query_parameters, files=_files, username=Configuration.basic_auth_user_name, password=Configuration.basic_auth_password)

        # Invoke the on before request HttpCallBack if specified
        if self.http_call_back != None:
            self.http_call_back.on_before_request(_request)

        # Invoke the API call  to fetch the response.
        _response = self.http_client.execute_as_string(_request)

        # Wrap the request and the response in an HttpContext object
        _context = HttpContext(_request, _response)

        # Invoke the on after response HttpCallBack if specified
        if self.http_call_back != None:
            self.http_call_back.on_after_response(_context)

        # Global error handling using HTTP status codes.
        self.validate_response(_context)    

        # Return appropriate type
        return _response.raw_body


