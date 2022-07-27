import json
from django.http import JsonResponse
from .Compiler.compiler import run
from home.models import CodeFile

def index(request):
    output=""
    if request.method == "POST":
        data = json.loads(request.body.decode('utf8'))
        language = data.get('language')
        title = data.get('title')
        code = data.get('code')
        inp = data.get('inp')

        output = run(language = language, code = code, inp = inp)
        
        codeFile = CodeFile(language = language, title=title, code=code, inp=inp, output = output)
        codeFile.save()

    response = JsonResponse({'output' : output}, safe=False)
    response["Access-Control-Allow-Origin"] = "*" 
    response["Access-Control-Allow-Headers"] = "*" 

    return response