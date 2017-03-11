from django.shortcuts import render,render_to_response
from django.http import Http404,HttpResponseRedirect
from couchdb import Server,ResourceNotFound
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

SERVER = Server("http://127.0.0.1:5984")
if len(SERVER) == 0:
    SERVER.create('docs')
@csrf_exempt
def index(request):
    docs = SERVER['docs']
    if request.method == 'POST':
        title = request.POST['title'].replace(' ','')
        docs[title] = {'title':title,'text':''}
        return HttpResponseRedirect(u"doc/%s/"%title)
    return render_to_response('index.html',{'rows':docs})

@csrf_exempt
def detail(request,id):
    docs = SERVER['docs']
    try:
        doc = docs[id]
    except ResourceNotFound:
        raise Http404
    if request.method == 'POST':
        doc['title'] = request.POST['title'].replace(' ','')
        doc['text'] = request.POST['text']
        docs[id] = doc
    return render_to_response('detail.html',{'row':doc})
