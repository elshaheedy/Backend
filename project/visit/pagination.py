# -*- coding: utf-8 -*-
from rest_framework.pagination import PageNumberPagination


class VisitPagination(PageNumberPagination):
    page_size = 20
    page_size_query_param = "limit"
