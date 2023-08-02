from django.shortcuts import render , redirect
from .models import *

# Create your views here.
def recipes(request):
    if request.method == 'POST':
        data=request.POST
        
        RecipeName = data.get('recipe_name')
        RecipeDesc = data.get('recipe_description')
        RecipeImage = request.FILES.get('recipe_image')
        
        recipe.objects.create(
            recipe_name = RecipeName,
            recipe_description = RecipeDesc ,
            recipe_image = RecipeImage
        )
        return redirect('/recipe/')


    queryset = recipe.objects.all()

    if request.GET.get('search'):
        queryset = queryset.filter(recipe_name__icontains = request.GET.get('search')) 
 
    context = {'recipes' : queryset}
    return render(request , "recipe.html",context)



def update_recipe(request , id):
    queryset = recipe.objects.get(id=id)

    if request.method == "POST":
        data=request.POST
        
        RecipeName = data.get('recipe_name')
        RecipeDesc = data.get('recipe_description')
        RecipeImage = request.FILES.get('recipe_image')

        queryset.recipe_name = RecipeName
        queryset.recipe_description = RecipeDesc

        if queryset.recipe_image:
            queryset.recipe_image = RecipeImage

        queryset.save()
        return redirect('/recipe/')

    context = {'recipes' : queryset}
    return render(request , "update_recipe.html",context)
    # return redirect()


def delete_recipe(request , id):
    queryset = recipe.objects.get(id=id)
    queryset.delete()
    return redirect('/recipe/')