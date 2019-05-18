from django.shortcuts import render, redirect
from .models import SKU
from .tasks import handle_uploaded_file
import tempfile
#from rq import Queue
#from worker import conn
#q = Queue(connection=conn)

# Create your views here.
def product(request):
    message = {}
    template_name = 'product/index.html'
    if request.method == 'GET':
        context = {}
        products = SKU.objects.all()
        context["products"] = products 
        return render(request, template_name,context)
    
    csv_file = request.FILES['file']
    if not csv_file.name.endswith('.csv'):
        return 'Not csv file'
    with tempfile.NamedTemporaryFile(delete=False) as f:
        for chunk in request.FILES["file"].chunks():
            f.write(chunk)
    
    #result = q.enqueue(handle_uploaded_file,io_string)
    print('filename: {}'.format(f.name))
    handle_uploaded_file.delay(f.name)
    context = {}
    products = SKU.objects.all()
    context["products"] = products 
    return render(request,template_name, context)

def deleteAllProducts(request):
    SKU.objects.all().delete()
    return redirect('product')
