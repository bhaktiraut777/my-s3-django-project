# views.py

from django.shortcuts import render, redirect
from .forms import ImageUploadForm
from .models import UploadedImage

from AWS_Learning.s3_utils.s3_client import S3Client

def upload_image(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        s3 = S3Client()
        if form.is_valid():
            # save image in s3
            image_file = form.cleaned_data['image']
            s3_key = f"images/{image_file.name}"
            result = s3.upload_fileobj(image_file, s3_key)
            print(result)
            return redirect('list_images')
    else:
        form = ImageUploadForm()
    return render(request, 'awsapp/upload.html', {'form': form})

def list_images(request):
    s3 = S3Client()
    image_urls = s3.list_image_urls(prefix="images/")
    print("IMG URLS: ",image_urls)
    return render(request, 'awsapp/list.html', {'images': image_urls})
