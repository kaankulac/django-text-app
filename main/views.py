from django.shortcuts import render,redirect
from .models import Post


def main(request):
    postes = Post.objects.all()
    context = {
        'postes':postes,
    }
    if request.method == 'POST':
        username = request.user.username
        description = request.POST['description']

        if len(description)>10:
                post = Post(fromWho = username,description=description,likeCount=0,commentCount=0)
                post.save()
                print('Paylaşım yapıldı.')
                return redirect('main')
        else:
            print('yetersiz karakter')
            return redirect('main')
            
    else:
        return render(request,'main/main.html',context)
