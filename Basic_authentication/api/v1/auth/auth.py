#!/usr/bin/env python3
""" Authentication module for API """
from flask import request
from typing import List, TypeVar


class Auth:
    """ Template for authentication system """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        returns False - path and excluded_paths will be used later
        """
        if path is None:
            return True

        if not excluded_paths:
            return True

        if path[-1] != '/':
            path += '/'

        if path in excluded_paths:
            return False

        return True

    def authorization_header(self, request=None) -> str:
        """
        returns None - request will be the Flask request object
        """
        return None

    User = TypeVar("User")

    def current_user(self, request=None) -> User:
        """
        returns None - request will be the Flask request object
        """
        return None
