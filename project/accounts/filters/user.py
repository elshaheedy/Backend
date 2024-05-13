# from django_filters import rest_framework as filters    
# class AddressFilter:
#     def __init__(self, address_prop, lookups):
#         self.address_prop = address_prop
#         self.lookups = lookups

#     def apply_filter(self, queryset, lookup_type, value):
#         lookup = f"{self.address_prop}__{lookup_type}"
#         filter_args = {lookup: value}
#         return queryset.filter(**filter_args)