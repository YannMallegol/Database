import os, re
from django.db.models import Q
from polls.models import Patient, Study, Series, MR_Params, US_Params, CT_Params, Review


print('')





def normalize_query(query_string)
    qry=re.compile(r'[^\s";,.:]+').findall(query_string)
    print(qry)
    return qry



def get_query(query_string, search_fields):
    query = None # Query to search for every search term
    terms = normalize_query(query_string)
    for term in terms:
        or_query = None # Query to search for a given term in each field
        for field_name in search_fields:
            q = Q(**{"%s__icontains" % field_name: term})
            if or_query is None:
                or_query = q
            else:
                or_query = or_query | q
        if query is None:
            query = or_query
        else:
            query = query & or_query
    return query
