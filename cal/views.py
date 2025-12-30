from django.shortcuts import render

# Create your views here.

def index(request):
    try:
        value = ""
        if request.method == 'GET':
            return render(request,'index.html',{'value':value})
        
        if request.method == "POST":
            in1 = request.POST.get("in1")
            in2 = request.POST.get("in2")
            in3 = request.POST.get("in3")
            print(in1,in2,in3)
            try:
                in1 = int(in1)
                in3 = int(in3)
                operator = ["+","-","*","/"]
                if in2 not in operator:
                    value = "place right operator '+','-','*','/'"
                    return render(request,'index.html',{'value':value})
                
                if in2 in operator:
                    if in2 == "+":
                        value = in1+in3
                        return render(request,'index.html',{'value':value})
                    
                    if in2 == "-":
                        value = in1-in3
                        return render(request,'index.html',{'value':value})
                    
                    if in2 == "*":
                        value = in1*in3
                        return render(request,'index.html',{'value':value})
                    
                    if in2 == "/":
                        value = in1/in3
                        return render(request,'index.html',{'value':value})
            except :
                value = "place decimal number"
                return render(request,'index.html',{'value':value})



    except:
        pass