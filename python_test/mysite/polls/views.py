
from django.shortcuts import render

'''from .utils import generic_search
from .models import Patient, Study, Series, MR_Params, US_Params, CT_Params, Review
from django.shortcuts  import render_to_response,redirect



def search(request):
    query_string = ''
    found_entries = None
    if ('q' in request.GET) and request.GET['q'].strip():
        query_string = request.GET['q']

        entry_query = get_query(query_string, ['title', 'body',])

        found_entries = Patient.objects.filter(entry_query) #.order_by('-pub_date')

    return render_to_response('polls/index.html',
                          { 'query_string': query_string, 'found_entries': found_entries },
                          context_instance=RequestContext(request))'''
