from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from apps.anteproyecto.forms import *
from apps.anteproyecto.models import *
from django.db.models import Sum, F
from django.core.files.storage import FileSystemStorage

def inicio(request):
    return render(request, 'ap/inicioAP.html', {})

#AnteProyecto-------------------------------------------------------------------
def crearap(request):
    user = User.objects.all().order_by('id')
    if request.method == "POST":
        form = ApForm(request.POST, request.FILES)
        if form.is_valid():
            ap = form.save(commit=False)
            ap.user = request.user
            ap.save()
            return redirect('verap')
    else:
        form = ApForm()
    contexto = {'form': form, 'users':user}
    return render(request, 'ap/crearAP.html', contexto)

def verap(request):
    anteproyecto = AnteProyecto.objects.filter(user__username=request.user)
    contexto = {'anteproyectos':anteproyecto}
    return render(request, 'ap/viewAP.html', contexto)

def delap(request, id_anteproyecto):
	anteproyecto = AnteProyecto.objects.get(id=id_anteproyecto)
	if request.method == 'POST':
		anteproyecto.delete()
		return redirect('verap')
	return render(request, 'ap/delap.html', {'anteproyecto':anteproyecto})

def editap(request, id_anteproyecto):
	anteproyecto = AnteProyecto.objects.get(id=id_anteproyecto)
	if request.method == 'GET':
		form = ApForm(instance=anteproyecto)
	else:
		form = ApForm(request.POST, request.FILES, instance=anteproyecto)
		if form.is_valid():
			form.save()
		return redirect('verap')
	return render(request, 'ap/crearAP.html', {'form':form})

#AnteProyecto imagen------------------------------------------------------------
def antePI(request):
    if request.method == 'POST':
        form = ApForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('verap')
    else:
        form = ApForm()
    return render(request, 'ap/apimg/insertarAP.html', {'form':form})
#Calendario Global--------------------------------------------------------------
def calglo(request):
    calglo = AnteProyecto.objects.all()
    preglo = AnteProyecto.objects.aggregate(Sum('totalA'))
    contexto = {'calglos':calglo, 'preglo':preglo}
    return render(request, 'ap/calendario/CalendarioGlobal.html', contexto)

#Total por meses----------------------------------------------------------------
def totm(request):
    tm = Fila.objects.all()
    obj=Fila.objects.all().aggregate(Sum('enero'))
    objF=Fila.objects.all().aggregate(Sum('febrero'))
    objM=Fila.objects.all().aggregate(Sum('marzo'))
    objA=Fila.objects.all().aggregate(Sum('abril'))
    objMay=Fila.objects.all().aggregate(Sum('mayo'))
    objJ=Fila.objects.all().aggregate(Sum('junio'))
    objJul=Fila.objects.all().aggregate(Sum('julio'))
    objAg=Fila.objects.all().aggregate(Sum('agosto'))
    objS=Fila.objects.all().aggregate(Sum('septiembre'))
    objO=Fila.objects.all().aggregate(Sum('octubre'))
    objN=Fila.objects.all().aggregate(Sum('noviembre'))
    objD=Fila.objects.all().aggregate(Sum('diciembre'))
    nf=Fila.objects.all().count()
    contexto = {'tms':tm, 'obj':obj, 'objF':objF, 'objM':objM,
     'objA':objA, 'objMay':objMay, 'objJ':objJ, 'objJul':objJul,
     'objAg':objAg, 'objS':objS, 'objO':objO, 'objN':objN, 'objD':objD, 'nf':nf }
    return render(request, 'ap/totMes/totMes.html', contexto)

#Fila---------------------------------------------------------------------------
def crearf(request):
    anteproyecto = AnteProyecto.objects.filter(user__username=request.user)
    if request.method == "POST":
        form = FilaForm(request.POST)
        if form.is_valid():
            ap = form.save()
            return redirect('verap')
    else:
        form = FilaForm()
    contexto = {'form':form, 'anteproyectos':anteproyecto}
    return render(request, 'ap/filas/crearF.html', contexto)

def verf(request, id_anteproyecto):
    #Para el form
    ap = AnteProyecto.objects.get(id=id_anteproyecto)
    #AnteProyecto de x usuario
    anteproyecto = AnteProyecto.objects.filter(user__username=request.user)
    #Ver filas que pertenecen a x anteproyecto
    fila = Fila.objects.filter(anteProyecto_id=id_anteproyecto)
    #Numero de filas con filtro de anteProyecto
    nf = Fila.objects.filter(anteProyecto=id_anteproyecto).count()
    #Suma de columnas por mes con filtro de anteProyecto
    obj=Fila.objects.filter(anteProyecto_id=id_anteproyecto).aggregate(Sum('enero'))
    objF=Fila.objects.filter(anteProyecto_id=id_anteproyecto).aggregate(Sum('febrero'))
    objM=Fila.objects.filter(anteProyecto_id=id_anteproyecto).aggregate(Sum('marzo'))
    objA=Fila.objects.filter(anteProyecto_id=id_anteproyecto).aggregate(Sum('abril'))
    objMay=Fila.objects.filter(anteProyecto_id=id_anteproyecto).aggregate(Sum('mayo'))
    objJ=Fila.objects.filter(anteProyecto_id=id_anteproyecto).aggregate(Sum('junio'))
    objJul=Fila.objects.filter(anteProyecto_id=id_anteproyecto).aggregate(Sum('julio'))
    objAg=Fila.objects.filter(anteProyecto_id=id_anteproyecto).aggregate(Sum('agosto'))
    objS=Fila.objects.filter(anteProyecto_id=id_anteproyecto).aggregate(Sum('septiembre'))
    objO=Fila.objects.filter(anteProyecto_id=id_anteproyecto).aggregate(Sum('octubre'))
    objN=Fila.objects.filter(anteProyecto_id=id_anteproyecto).aggregate(Sum('noviembre'))
    objD=Fila.objects.filter(anteProyecto_id=id_anteproyecto).aggregate(Sum('diciembre'))
    tot = obj['enero__sum']+objF['febrero__sum']+objM['marzo__sum']+objA['abril__sum']+objMay['mayo__sum']+objJ['junio__sum']+objJul['julio__sum']+objAg['agosto__sum']+objS['septiembre__sum']+objO['octubre__sum']+objN['noviembre__sum']+objD['diciembre__sum']
    #Guardar el total y numero de Filas
    if request.method == 'GET':
        form = ApForm(instance=ap)
    else:
        form = ApForm(request.POST, instance=ap)
        if form.is_valid():
            form.save()
        return redirect('verap')
    contexto = {'filas':fila, 'obj':obj, 'objF':objF, 'objM':objM, 'objA':objA, 'objMay':objMay, 'objJ':objJ, 'objJul':objJul, 'objAg':objAg, 'objS':objS, 'objO':objO, 'objN':objN, 'objD':objD, 'tot':tot, 'anteproyectos':anteproyecto, 'nf':nf, 'form':form}
    return render(request, 'ap/filas/verF.html', contexto)

def delf(request, id_fila):
	fila = Fila.objects.get(id=id_fila)
	if request.method == 'POST':
		fila.delete()
		return redirect('verap')
	return render(request, 'ap/filas/delF.html', {'fila':fila})

def editf(request, id_fila):
	fila = Fila.objects.get(id=id_fila)
	if request.method == 'GET':
		form = FilaForm(instance=fila)
	else:
		form = FilaForm(request.POST, instance=fila)
		if form.is_valid():
			form.save()
		return redirect('verap')
	return render(request, 'ap/filas/crearF.html', {'form':form})

#capitulos----------------------------------------------------------------------
def iniciopc(request):
    return render(request, 'ap/capitulos/opc.html', {})

def vercap(request):
	capitulo = Capitulo.objects.all().order_by('id')
	contexto = {'capitulos':capitulo}
	return render(request, 'ap/capitulos/cap/vercap.html', contexto)

def crearcap(request):
    if request.method == "POST":
        form = CapituloForm(request.POST)
        if form.is_valid():
            cpn = form.save()
            return redirect('vercap')
    else:
        form = CapituloForm()
    return render(request, 'ap/capitulos/cap/crearcap.html', {'form':form})

def delcap(request, id_capitulo):
	capitulo = Capitulo.objects.get(id=id_capitulo)
	if request.method == 'POST':
		capitulo.delete()
		return redirect('vercap')
	return render(request, 'ap/capitulos/cap/delcap.html', {'capitulo':capitulo})

def editcap(request, id_capitulo):
	capitulo = Capitulo.objects.get(id=id_capitulo)
	if request.method == 'GET':
		form = CapituloForm(instance=capitulo)
	else:
		form = CapituloForm(request.POST, instance=capitulo)
		if form.is_valid():
			form.save()
		return redirect('vercap')
	return render(request, 'ap/capitulos/cap/crearcap.html', {'form':form})

#Conceptos----------------------------------------------------------------------
def vercon(request):
	concepto = Concepto.objects.all().order_by('id')
	contexto = {'conceptos':concepto}
	return render(request, 'ap/capitulos/conn/vercon.html', contexto)

def loadConc(request):
    capitulo_id = request.GET.get('capitulo')
    conceptos = Concepto.objects.filter(capitulo_id=capitulo_id).order_by('id')
    return render(request, 'ap/capitulos/conn/dropcon.html', {'conceptos': conceptos})

def crearcon(request):
    if request.method == "POST":
        form = ConceptoForm(request.POST)
        if form.is_valid():
            con = form.save()
            return redirect('vercon')
    else:
        form = ConceptoForm()
    return render(request, 'ap/capitulos/conn/crearcon.html', {'form':form})

def delcon(request, id_concepto):
	concepto = Concepto.objects.get(id=id_concepto)
	if request.method == 'POST':
		concepto.delete()
		return redirect('vercon')
	return render(request, 'ap/capitulos/conn/delcon.html', {'concepto':concepto})

def editcon(request, id_concepto):
	concepto = Concepto.objects.get(id=id_concepto)
	if request.method == 'GET':
		form = ConceptoForm(instance=concepto)
	else:
		form = ConceptoForm(request.POST, instance=concepto)
		if form.is_valid():
			form.save()
		return redirect('vercon')
	return render(request, 'ap/capitulos/conn/crearcon.html', {'form':form})

#partidagenerica----------------------------------------------------------------
def verpg(request):
	partidagenerica = PartidaGenerica.objects.all().order_by('id')
	contexto = {'partidagenericas':partidagenerica}
	return render(request, 'ap/capitulos/pg/verpg.html', contexto)

def loadpg(request):
    concepto_id = request.GET.get('concepto')
    partidagenericas = PartidaGenerica.objects.filter(concepto_id=concepto_id).order_by('id')
    return render(request, 'ap/capitulos/pg/droppg.html', {'partidagenericas': partidagenericas})

def crearpg(request):
    if request.method == "POST":
        form = PGForm(request.POST)
        if form.is_valid():
            con = form.save()
            return redirect('verpg')
    else:
        form = PGForm()
    return render(request, 'ap/capitulos/pg/crearpg.html', {'form':form})

def delpg(request, id_partidagenerica):
	partidagenerica = PartidaGenerica.objects.get(id=id_partidagenerica)
	if request.method == 'POST':
		partidagenerica.delete()
		return redirect('verpg')
	return render(request, 'ap/capitulos/pg/delpg.html', {'partidagenerica':partidagenerica})

def editpg(request, id_partidagenerica):
	partidagenerica = PartidaGenerica.objects.get(id=id_partidagenerica)
	if request.method == 'GET':
		form = PGForm(instance=partidagenerica)
	else:
		form = PGForm(request.POST, instance=partidagenerica)
		if form.is_valid():
			form.save()
		return redirect('verpg')
	return render(request, 'ap/capitulos/pg/crearpg.html', {'form':form})
#partidaespecifica--------------------------------------------------------------

def verpe(request):
    partidaespecifica = PartidaEspecifica.objects.all().order_by('id')
    contexto = {'partidaespecificas':partidaespecifica}
    return render(request, 'ap/capitulos/pe/verpe.html', contexto)

def loadpe(request):
    partidagenerica_id = request.GET.get('partidagenerica')
    partidaespecificas = PartidaEspecifica.objects.filter(partidagenerica_id=partidagenerica_id).order_by('id')
    return render(request, 'ap/capitulos/pe/droppe.html', {'partidaespecificas': partidaespecificas})

def crearpe(request):
    if request.method == "POST":
        form = PEForm(request.POST)
        if form.is_valid():
            con = form.save()
            return redirect('verpe')
    else:
        form = PEForm()
    return render(request, 'ap/capitulos/pe/crearpe.html', {'form':form})

def delpe(request, id_partidaespecifica):
	partidaespecifica = PartidaEspecifica.objects.get(id=id_partidaespecifica)
	if request.method == 'POST':
		partidaespecifica.delete()
		return redirect('verpe')
	return render(request, 'ap/capitulos/pe/delpe.html', {'partidaespecifica':partidaespecifica})

def editpe(request, id_partidaespecifica):
	partidaespecifica = PartidaEspecifica.objects.get(id=id_partidaespecifica)
	if request.method == 'GET':
		form = PEForm(instance=partidaespecifica)
	else:
		form = PEForm(request.POST, instance=partidaespecifica)
		if form.is_valid():
			form.save()
		return redirect('verpe')
	return render(request, 'ap/capitulos/pe/crearpe.html', {'form':form})
