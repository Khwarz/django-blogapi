from typing import Any

from rest_framework import permissions
from rest_framework.permissions import BasePermission
from rest_framework.request import Request
from rest_framework.views import APIView


class IsAuthorOrReadOnly(BasePermission):
    def has_permission(self, request: Request, _: APIView) -> bool:
        return request.user.is_authenticated

    def has_object_permission(self, request: Request, _: APIView, obj: Any) -> bool:
        return request.method in permissions.SAFE_METHODS or obj.author == request.user
