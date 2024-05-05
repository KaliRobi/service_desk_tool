
from django.views import View
from rest_framework.views import APIView
from django.http import JsonResponse
import re

# Create your views here.

#file is transfered to the location, with a unique id
#access the file
#get the content 
#execute the query on the selected db
#get the result
#convert it to Dataframe and export it to excel in a different directory


class ExecuteSQLQuery(APIView):
    # will be a post request

    def get(self, request, *args, **kwargs):
        return self.create_query_object (req=request) 

    @classmethod
    def is_sql_file(cls, name):
        return re.compile(r'\.sql$', name) is not None
    
    
    def create_query_object(self,req, *args, **kwargs):
        temp_file = '../test.sql'
        with open(f'{temp_file}') as cursor:
                    sql_query = cursor.readlines()
                    
                    return JsonResponse(sql_query, safe=False)
             
  

    def execute_on_db(sql_query, databse_name):
         pass



class FollowUpRunningQueries(View):
    """
    When one query is executed a RunningQUERYModel should recodr the name, the insert time, the status, and the result (error or none)   
    """


    pass


        

    

             

    
   

    









