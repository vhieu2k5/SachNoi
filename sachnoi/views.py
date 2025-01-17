from django.shortcuts import render
from django.http import HttpResponse , JsonResponse
from gtts import gTTS # type: ignore
from sachnoi.models import TextEntry, Books


def create_text_entry(request):
    # Lưu văn bản vào database
    entry = TextEntry( content="Chào mừng bạn đến với thế giới lập trình Python. Đây là một ví dụ để kiểm tra tính năng chuyển văn bản thành giọng nói bằng gTTS. Chúc bạn thành công!")
    entry.save()
    
    return HttpResponse("Đã lưu văn bản thành công!")

def home(request):
    entries = TextEntry.objects.all()
    return render(request,'app/index.html',{'entries': entries})
def author(request):
    return render(request,'app/author.html')
def category(request):
    return render(
        request,'app/category.html'
    )
def discover(request):
    return render(request,'app/discover.html')
def login(request):
    return render(request,'app/login.html')
def signup(request):
    return render(request,'app/signup.html')
def forgot_password(request):
    return render(request,'app/forgot_password.html')
def account(request):
    return render(request,'app/account.html')
def book_history(request):
    return render(request,'app/book_history.html')
def favorite_books(request):
    return render(request,'app/favorite_books.html')
def saved_book(request):
    return render(request,'app/saved_book.html')
def enter_OTP_code(request):
    return render(request,'app/enter_OTP_code.html')
def convert_text_to_speech(request, text_id):
    from django.shortcuts import get_object_or_404  
    entry = get_object_or_404(TextEntry, id=text_id)
    tts = gTTS(text=entry.content, lang='vi')
    response = HttpResponse(content_type='audio/mpeg')
    tts.write_to_fp(response)
    response['Content-Disposition'] = f'attachment; filename="{entry.title}.mp3"'
    return response

def testapi(request):
    data = list(Books.objects.values())
    return JsonResponse(data ,safe=False)
