
# Create your views here.
import simplejson as json
from django.http import HttpResponse
from django.template import loader
from django.views.decorators.csrf import csrf_exempt

from kiwoom.kiwoom import Kiwoom
from ui.ui import Ui_class


def index(request):
    template = loader.get_template('polls/index.html')
    context = {
        'text': "latest_question_list",
    }
    return HttpResponse(template.render(context, request))


@csrf_exempt
def ajaxtext(request):
    Ui_class()
    context = {
        'code': "00",
    }
    return HttpResponse(json.dumps(context), content_type="application/json")


# Leave the rest of the views (detail, results, vote) unchanged