from combojsonapi.permission.permission_system import (
    PermissionMixin,
)


class UserPermission(PermissionMixin):
    ALL_AVAILABLE_FIELDS = [
          "id",
          "first_name",
          "last_name",
          "username",
          "is_staff",
          "email",
    ]

