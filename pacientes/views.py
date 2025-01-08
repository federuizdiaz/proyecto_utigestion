from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from pacientes.models import Paciente, EntradaEvolucion
from pacientes.forms import EntradaEvolucionForm, PacienteForm

@login_required
def inicio_pacientes(request):
    return render(request, "pacientes/inicio_pacientes.html", {"usuario": request.user})

@login_required
def lista_pacientes(request):
    pacientes = Paciente.objects.all()
    return render(request, "pacientes/lista_pacientes.html", {"pacientes": pacientes})

@login_required
def registrar_paciente(request):
    if request.method == "POST":
        form = PacienteForm(request.POST)
        if form.is_valid():
            paciente = form.save(commit=False)
            paciente.personal_salud = request.user
            paciente.save()
            return redirect('lista_pacientes')  
    else:
        form = PacienteForm()
    return render(request, "pacientes/registrar_paciente.html", {"form": form})

@login_required
def detalles_paciente(request, paciente_id):
    paciente = get_object_or_404(Paciente, id=paciente_id)

    if request.method == "POST" and 'editar_entrada' not in request.POST:
        form = EntradaEvolucionForm(request.POST, request.FILES)  # Asegúrate de pasar request.FILES
        if form.is_valid():
            entrada = form.save(commit=False)
            entrada.paciente = paciente
            entrada.usuario = request.user  
            entrada.save()
            return redirect('detalles_paciente', paciente_id=paciente.id)
    
    else:
        form = EntradaEvolucionForm()

    entradas = paciente.entradas_evolucion.all()

    return render(request, 'pacientes/detalles_paciente.html', {
        'paciente': paciente,
        'form': form,
        'entradas': entradas,
    })


@login_required
def eliminar_entrada(request, entrada_id):
    entrada = get_object_or_404(EntradaEvolucion, id=entrada_id, usuario=request.user)  
    paciente_id = entrada.paciente.id
    entrada.delete()
    return redirect('detalles_paciente', paciente_id=paciente_id)

@login_required
def ver_entrada_evolucion(request, entrada_id):
    entrada = get_object_or_404(EntradaEvolucion, id=entrada_id)

    return render(request, 'pacientes/ver_entrada_evolucion.html', {
        'entrada': entrada,
    })

@login_required
def editar_entrada_evolucion(request, entrada_id):
    entrada = get_object_or_404(EntradaEvolucion, id=entrada_id, usuario=request.user)  
    if request.method == "POST":
        form = EntradaEvolucionForm(request.POST, instance=entrada)
        if form.is_valid():
            form.save()
            return redirect('detalles_paciente', paciente_id=entrada.paciente.id)
    else:
        form = EntradaEvolucionForm(instance=entrada)

    return render(request, 'pacientes/editar_entrada_evolucion.html', {
        'form': form,
        'entrada': entrada
    })




from django.shortcuts import render

def about(request):
    return render(request, 'hospital_uti/about.html')

