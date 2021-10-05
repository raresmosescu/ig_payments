from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .decorators import groups_required
from pages.models import Page, Package
# Create your views here.

@login_required
@groups_required(allowed_groups=['seller'])
def page_create(request):
    if request.method == "POST":
        
        return render(request, 'page_view.html')
    else:
        return render(request, 'page_create.html')

# with gcs.open('/mybucket/newfile.txt', 'w', content_type='text/html; charset=utf-8') as f:


def page_view(request):
    pagename = request.GET.get('name')
    page_obj = Page.objects.get(username=pagename)
    # growth_options = Package.objects.filter(page_id=page_obj.id, package_type="growth").order_by('posts_amount')
    # sales_options = Package.objects.filter(page_id=page_obj.id, package_type="sales").order_by('posts_amount')
    # print(sales_options)
    
    return render(request, 'page_view.html', context={'page':page_obj})