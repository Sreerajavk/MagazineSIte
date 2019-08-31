from django.http import HttpResponse
from django.shortcuts import render , redirect
from .models import *
# Create your views here.


def index(request):
    return redirect('/home')


#for home page
def home(request):

    #getting all the details of list of years
    year_details=[]

    years = MagazineDetails.objects.all()
    for year in years:
        all_years = {}
        all_years['id'] = year.id
        all_years['year'] = year.year
        year_details.append(all_years)
    return  render(request , 'home2.html' , {'data': year_details})

def getdetails(request ,id):

    magazine_info = MagazineDetails.objects.get( id = id )
    details = {}
    details['year'] = magazine_info.year
    details['title'] = magazine_info.title
    details['editor_name'] = magazine_info.editor_name
    details['description'] = magazine_info.description
    details['document_link'] = magazine_info.document_link
    details['image'] = magazine_info.cover_image

    return render(request , 'details2.html' , details)

def pdf_view(request):
    with open('/home/sreeraj/Documents/study/s5 materials/sc1.pdf', 'r') as pdf:
        response = HttpResponse(pdf.read(), mimetype='application/pdf')
        response['Content-Disposition'] = 'inline;filename=some_file.pdf'
        return response
    pdf.closed

# from easy_pdf.views import PDFTemplateView
#
# class HelloPDFView(PDFTemplateView):
#     template_name = 'hello.html'

# from django.conf import settings
# from easy_pdf.views import PDFTemplateView
#
# class HelloPDFView(PDFTemplateView):
#     template_name = 'hello.html'
#
#     base_url = 'file://' + settings.STATIC_ROOT
#     download_filename = 'hello.pdf'
#
#     def get_context_data(self, **kwargs):
#         return super(HelloPDFView, self).get_context_data(
#             pagesize='A4',
#             title='Hi there!',
#             **kwargs
#         )