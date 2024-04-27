from typing import List
from rest_framework import exceptions
from django.db.models import Q, Max

"""
This class is used for base repository
Fields:
Methods:
    Create: This method is used to create a new object
    GetFirst: This method is used to get the first object
    GetAll: This method is used to get all the objects
    Query: This method is used to get the query
    Filters: This method is used to filter the query
    GetValueList: This method is used to get the value list
    CheckExists: This method is used to check if the object exists or not
    Objects: This method is used to get the objects
    Destroy: This method is used to delete the object
    UpdateWhere: This method is used to update the object
    DeleteWhere: This method is used to delete the object    
"""


class BaseRepository:
    def __init__(self):
        pass

    def Create(self, values: dict = {}):
        new_obj = self.model(**values)
        new_obj.save()
        return new_obj

    def GetFirst(
        self, filters=[], error=True, err_detail="Not Found", order_filter: str = None
    ):
        if order_filter is not None:
            query = self.Query(filters=filters).order_by(order_filter).first()
        else:
            query = self.Query(filters=filters).first()
        if error and not query:
            raise exceptions.NotFound(err_detail)
        return query

    def GetAll(self, filters=[], error=True, err_detail="Not Found"):
        query = self.Query(filters=filters)
        if error and not query:
            raise exceptions.NotFound(err_detail)
        return query

    def GetOrCreate(self, filters=[], values={}, err_detail="Not Found"):
        query = self.GetFirst(filters=filters, error=False, err_detail=err_detail)
        if query:
            return query
        else:
            return self.Create(values=values)

    def Query(self, filters=[]):
        self.res = self.model.objects.all()
        query = self.res
        for fil in filters:
            query = self.Filters(query, fil[0], fil[1])
        return query

    def Filters(self, queryset, name, value):
        query = queryset.filter(**{name: value})
        return query

    def GetValueList(self, queryset, name, flat=True):
        query = queryset.values_list(name, flat=flat)
        return query

    def CheckExists(self, filters=[], error=True, err_detail="Not Found"):
        query = self.GetFirst(filters=filters)
        if error and not query:
            raise exceptions.NotFound(err_detail)
        return query

    def Objects(self):
        return self.model.objects

    def Destroy(self, obj):
        obj.delete()

    def UpdateWhere(self, query: List[tuple], update: List[tuple]):
        return self.model.objects.filter(**dict(query)).update(**dict(update))

    def DeleteWhere(self, query: List[tuple], exclude: List[tuple] = None):
        if exclude:
            return (
                self.model.objects.filter(**dict(query))
                .exclude(**dict(exclude))
                .delete()
            )
        return self.model.objects.filter(**dict(query)).delete()

    # Fixed by Ambar
    def CreateOrUpdate(self, filters=[], values={}):
        query = self.Query(filters=filters).first()

        if query:
            # Entry exists, update it
            for key, value in values.items():
                setattr(query, key, value)
            query.save()
        else:
            # Entry does not exist, create a new one
            new_obj = self.model(**values)
            new_obj.save()
            query = new_obj

        return query

    def Search(self, keyword, fields=[], order_filter: str = None, first: bool = False):
        q_objects = Q()
        for field in fields:
            q_objects |= Q(**{field: keyword})
        if order_filter:
            self.query = self.model.objects.filter(q_objects).order_by(order_filter)
        self.query = self.model.objects.filter(q_objects)
        if first:
            return self.query.first()
        return self.query

    
    def GetMax(self, field):
        return self.model.objects.aggregate(Max(field))
