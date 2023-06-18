## 사용자 인증 기반 DB설계

##### 배민경 & 송원규
---
<br>

대전 1반 배민경 0933929

---

## 단계별 구현 과정 중 배운 점

페어짝꿍 원규는 movies, 저는 accounts를 진행하였습니다.
<br><br>
### A. 짜잘한 실수들

```python
# forms.py
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        # fields = ['first_name', 'last_name']  <- 이 줄은 필요 없다 

class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = get_user_model()
        fields = ['first_name', 'last_name']
```

```python
# update 기능에서 instance를 추가 안해줬다 ! 
def update(request):
    if request.method == "POST":
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            redirect("movies:index")
    else:
        form = CustomUserChangeForm(instance=request.user)
    context = {
        'form':form,
    }
    return render(request, "accounts/update.html", context)
```

### B. git branch로 협업

이전 페어프로그래밍에서는 한 명의 로컬을 공유해서 driver와 navigater 역할을 맡아 동시에 코딩하였지만 이번엔 git branch를 활용하여 두 명의 로컬에서 각자 자신이 맡은 역할을 분담하여 프로그래밍하였습니다. 현업 개발환경과 더 비슷한 것 같아서 좋았고, 이전 관통과 비슷한 서비스 구현임에도 불구하고 개발 속도가 2.5배 이상 빨라졌습니다!



<br><br><br>

---

대전 1반 송원규

## 단계별 구현 과정 중 배운 점

movies를 담당했습니다.

### A. 실수

1. 변수명 오타와 습관적으로 변수명을 작성하는 실수가 있었습니다.

### B. 배운점 / 느낀점
git.
코드 충돌 (Code conflict):
서로가 같은 코드 파일을 동시에 수정해서(settings.py) 각각의 수정이 충돌이 났습니다.  이런 경우, git은 충돌 부분을 자동으로 감지하고, 사용자에게 충돌 방안을 제시하기 때문에 우리는 git에서 settings.py를 수정했습니다. 

브랜치 (Branch)
git을 사용하면 브랜치를 만들어서 개발 작업을 병렬로 진행할 수 있습니다. 이를 통해 페어와 함께 동시에 작업을 진행하면서, 각각의 작업 결과를 쉽게 합칠 수 있었습니다.

...
git을 자유롭게 사용할 수 있게 공부를 해야겠습니다.