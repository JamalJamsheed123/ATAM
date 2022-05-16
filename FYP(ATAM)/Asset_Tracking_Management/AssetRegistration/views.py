from django.shortcuts import redirect, render
from AssetRegistration.models import Asset
from AssetRegistration.forms import AssetForm

# Create your views here.

def asset(request):
    if request.method == "POST":
        form = AssetForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect("/show")
            except:
                pass
    else:
        form = AssetForm()
    return render(request, 'index.html', {'form':form})

def show(request):
    assets = Asset.objects.all()
    return render(request,'show.html',{'assets':assets})

def edit(request,id):
    asset = Asset.objects.get(id=id)
    return render(request,'edit.html',{'asset':asset})

def update(request,id):
    asset = Asset.objects.get(id=id)
    form = AssetForm(request.POST,instance=asset)
    if form.is_valid():
        form.save()
        return redirect("/show")

    return render(request,'edit.html',{'asset':asset})

def destroy(request,id):
    asset = Asset.objects.get(id=id)
    asset.delete()
    return redirect("/show")
    

        