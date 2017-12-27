from .models import Member
from django.http import HttpResponse
from django.template.loader import render_to_string
from weasyprint import HTML
import tempfile



def generate_pdf(request):
    """Generate pdf."""
    # Model data
    people = Member.objects.all().order_by('last_name')

    # Rendered
    html_string = render_to_string('invoices/receipt.html', {'people': people})
    html = HTML(string=html_string)
    result = html.write_pdf()

    # Creating http response
    response = HttpResponse(content_type='application/pdf;')
    response['Content-Disposition'] = 'inline; filename=list_people.pdf'
    response['Content-Transfer-Encoding'] = 'binary'
    with tempfile.NamedTemporaryFile(delete=True) as output:
        output.write(result)
        output.flush()
        output.name = 'test'
        #output = open(output.name, 'r')
        #response.write(output.read())

    return response