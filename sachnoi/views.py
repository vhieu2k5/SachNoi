from django.shortcuts import render
from django.http import HttpResponse , JsonResponse
from gtts import gTTS # type: ignore
from sachnoi.models import TextEntry, Books
from .forms import TextToSpeechForm
from io import BytesIO

def text_to_speech_view(request):
    if request.method == "POST":
        form = TextToSpeechForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data['text']
            print("Văn bản người dùng nhập:", text)
            try:
                tts = gTTS(text, lang='vi')
                audio_file = BytesIO()
                tts.write_to_fp(audio_file)
                audio_file.seek(0)
                print("Tạo file âm thanh thành công")
                
                action = request.POST.get("action")  # Lấy hành động từ nút nhấn
                
                if action == "play":
                    # Trả file MP3 để phát trực tiếp
                    response = HttpResponse(audio_file, content_type="audio/mpeg")
                    response['Content-Disposition'] = 'inline; filename="output.mp3"'
                    return response
                elif action == "download":
                    # Trả file MP3 để tải về
                    response = HttpResponse(audio_file, content_type="audio/mpeg")
                    response['Content-Disposition'] = 'attachment; filename="output.mp3"'
                    return response
            except Exception as e:
                print("Lỗi khi chuyển văn bản thành giọng nói:", e)
                return render(request, 'app/text_to_speech.html', {
                    'form': form,
                    'error': f"Không thể chuyển văn bản thành giọng nói: {str(e)}"
                })
    else:
        form = TextToSpeechForm()
    return render(request, 'app/text_to_speech.html', {'form': form})


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
