from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404

from ..models import Question

def index(request):
    # return HttpResponse("안녕하세요 pybo에 오신 것을 환영합니다.")
    #input parameter
    page = request.GET.get('page','1') #page
    #조회
    question_list = Question.objects.order_by('-create_date')
    #페이징처리
    paginator = Paginator(question_list, 10) #10 contents/page
    page_obj = paginator.get_page(page)
    context = {'question_list': page_obj}
    return render(request, 'pybo/question_list.html', context)

def detail(request, question_id):
    question = Question.objects.get(id=question_id)
    context = {'question': question}
    return render(request, 'pybo/question_detail.html', context)