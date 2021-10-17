from django.http import HttpResponse
from django.shortcuts import render
import subprocess

def render_html_download_pdf(request, template, context, margin = "", fileout="out.pdf"):
    import os
    basepath = os.path.dirname(__file__)
    file_html = basepath + "/hello.html"
    f = open(file_html, 'w')
    f.write(render(request, template, context).content.decode("utf-8"))
    f.close()
    subprocess.call('wkhtmltopdf ' + margin + ' ' + file_html + ' ' + basepath + "/" + fileout, shell=True)
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="' + fileout + '"'

    fout = open(basepath + "/" + fileout, "rb")
    response.write(fout.read())
    fout.close()
    return response

