from rest_framework.pagination import PageNumberPagination


class PersonPagePagination(PageNumberPagination):
    page_size = 2


class GroupPagePagination(PageNumberPagination):
    page_size = 1


class SubjectPagePagination(PageNumberPagination):
    page_size = 4
