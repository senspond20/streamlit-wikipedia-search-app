# Streamlit Wikipedia Search App

## DEMO

> https://easywiki.streamlit.app/

+ wikipedia search

![demo1](images/demo1.jpg)

+ keyword extraction
 
![demo2](images/demo2.jpg)
  
![demo2](images/demo3.jpg)


## ISSUE

> Streamlit Share 에 배포하게 되면 konlpy 가 JAVA 런타임이 필요해서 오류가 발생 


![error](images/jvm.jpg)

+ 아래처럼 코드를 심어서 서버에서 JDK 를 설치되도록 시도해보았으나 실패.

```python
# share.streamlit 에 배포하면 konlpy 때문에 자바 환경변수 설정 필요
import jdk
import os
from jdk.enums import OperatingSystem, Architecture
jdk.install('11', operating_system=OperatingSystem.LINUX)
jdk_version = 'jdk-11.0.19+7'
os.environ['JAVA_HOME'] = '/root/.jdk/{jdk_version}'
os.environ['PATH'] = f"{os.environ.get('PATH')}:{os.environ.get('JAVA_HOME')}/bin"
```

![error](images/permission.jpg)

