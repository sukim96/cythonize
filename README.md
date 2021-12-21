# Cythonize: Example for cythonizing python package

## Introduction
Python은 script language로, interpreter를 이용해 실행한다.

기존의 컴파일 언어에 비해 파이썬 패키지는 쉽게 구현할 수 있고,
packing / test 등이 간편하다는 장점이 있지만,
컴파일 언어에 비해 실행 속도가 느리다.

또한 일반적인 방법으로 setup을 진행할 경우, source code가 그대로 site package로 저장되기 때문에 패키지 구조를 전부 확인할 수 있다.

이것을 보완하기 위해, cython은 shared object file 형태로 export 할 수 있는 방법을 제시한다.

또한, wheel 파일로 패키지를 export하여 설치할 수 있는 형태로 제공하는 방법을 제시한다.

## Project Description
- 간단한 deep learning model을 패키지 형태로 제작
- cythonize하여 shared object(.so) 파일 형태로 export
- bdist_wheel 옵션을 이용하여 build & dist package로 export (wheel 파일)

## Code Structure
```
.
├── sample_package
│   ├── __init__.py
│   └── engine.py           : 간단한 deep learning model 위치
├── setup.py                : python package setup (cythonize)
├── test.py                 : build한 package로 test 실행
├── requirements.txt        : pip requirements to setup (dependencies)
└── README.md
```

## Prerequisites
- Cython
- pytorch
- torchvision

## Build
1. build_ext 로 빌드
```
$ python setup.py build_ext
```
2. bdist 로 빌드
```
$ python setup.py bdistwheel
```

## Run
1. build_ext 로 빌드
    - build/lib.linux-{architecture}-{python_version} directory 내부에 .so 파일, __init__.py 파일 생김
    - 해당 디렉토리에서 .so파일 내부의 패키지 불러와서 사용 가능

2. bdist 로 빌드
    - dist 디렉토리에 패키지 생김
    - 해당 패키지에 맞게 패키지 설치 후 실행
    - ex) .whl: pip으로 설치
        ```
        $ pip install dist/*.whl
        ```
3. 설치 후 실행 (sample)
    ```
    $ python
    >>> from sample_package import Engine
    >>> import torch
    >>> device = 'cuda' if torch.cuda.is_available() else 'cpu'
    >>> engine = Engine(num_classes=3, device=device)
    >>> t = torch.randn((1, 3, 224, 224), device=device)
    >>> o = engine(t)
    >>> print(o)
    ```
