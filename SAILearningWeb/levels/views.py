from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from perfiles.models import Perfil

@login_required(login_url="/login/")
def avance(request):
    user = request.user
    perfil = Perfil.objects.get(usuario=user)
    niveles = range(1, 61)  # Crea una lista de niveles del 1 al 30
    nivel_actual = request.user.perfil.nivel  # Obtiene el nivel actual del usuario
    context = {
        'niveles': niveles,
        'nivel_actual': nivel_actual,
        'user':user, 
        'perfil':perfil
    }
    return render(request, 'levels/app.html', context=context)


@login_required

@login_required(login_url="/login/")
def nivel(request, nivel):
    user = request.user
    perfil = request.user.perfil
    niveles = range(1, 61)  # Crea una lista de niveles del 1 al 60
    nivel_actual = nivel

    def actualizar_nivel():
        perfil.nivel = nivel  # Incrementar el nivel del jugador
        perfil.save()  # Guardar los cambios en la base de datos
        return redirect('levels:level', nivel=perfil.nivel)  # Redirigir a la vista del nuevo nivel
    
    if perfil.nivel < nivel:
        actualizar_nivel()

    return render(request, 'levels/level.html', {'nivel_actual': nivel_actual, 'user': user, 'perfil':perfil, 'niveles':niveles})


@login_required(login_url="/login/")
def nivel_2(request, nivel):
    user = request.user
    perfil = request.user.perfil

    perfil.nivel += 1  # Incrementar el nivel del jugador
    perfil.save()  # Guardar los cambios en la base de datos
  
    return render(request, 'levels/level_2.html', {'nivel': nivel, 'user': user, 'perfil':perfil})



