from django.shortcuts import render
from django.http import JsonResponse
from testtask.models import Order, Сontact, Product
from django.views.generic import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.http import QueryDict

# Create your views here.
data = [{'name': 'Test', 'e-mail': 'linux@org.ru'},
        {'name': 'Test2', 'e-mail': 'linux2@org.ru'}]

def index(request):
    print(request.GET)
    data = [{'name': 'Test', 'e-mail': 'linux@org.ru'},
            {'name': 'Test2', 'e-mail': 'linux2@org.ru'}]

    return JsonResponse(data, safe=False)


def serialize(order):

    return { 
             'order_num': order.number,
             'date_create':order.date,
             'byer': [{ 'name':f'{order.contact.first_name} {order.contact.last_name}',
                        'tel':f'{order.contact.tel_number}',
                        'email':order.contact.email,
                        'address':order.contact.address,
                      }],
             'amount':sum([product.cost for product in order.products.all()])
            }
  
# @method_decorator(csrf_exempt,name='dispatch')
# class ApiView(View):
#     http_method_names = ['get', 'post', 'put', 'delete']

#     def post(self, *args, **kwargs):
#         print(self.request.POST.get('test2'))
#         return JsonResponse(data, safe=False)



#     def put(self, *args, **kwargs):

#         orders = Order.objects.all()
#         data = [serialize(order) for order in orders]
#         return JsonResponse(data, safe=False)
    
#     def delete(self, *args, **kwargs):
#         # print(self.request.POST.get('_method') )
#         get = QueryDict(self.request.body)
#         print(get.dict())
       
#         return JsonResponse(data, safe=False)

@csrf_exempt
def get_api(request, pk=None):
    if request.method == "PUT":
        q=QueryDict(request)
        print(q.values())
        orders = Order.objects.all()
        data=[serialize(order) for order in orders]
            
        return JsonResponse(data, safe=False)