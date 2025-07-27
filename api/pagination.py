from rest_framework.pagination import CursorPagination

class StandardCursorPagination(CursorPagination):
    page_size = 15
    ordering = '-created_datetime'
