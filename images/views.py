from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import ImageCreateForm
from django.shortcuts import get_object_or_404
from .models import Image


@login_required
def image_create(request):
    if request.method == 'POST':
        # form is sent
        form = ImageCreateForm(request.POST, request.FILES)
        if form.is_valid():
            # form data is valid
            image = form.save(commit=False)
            # assign current user to the item
            image.user = request.user
            image.save()

            messages.success(request, 'Image added Successfully')

            # redirect to new created item detail view
            return redirect(image.get_absolute_url())
    else:
        # build form by the data provided by the bookmarklet via GET
        form = ImageCreateForm(data=request.GET)

    return render(request, 'images/image/create.html', {'section': 'images',
                                                        'form': form})


def image_detail(request, id, slug):
    image = get_object_or_404(Image, id=id, slug=slug)
    return render(request,
                  'images/image/detail.html',
                  {'section': 'images',
                   'image': image})
