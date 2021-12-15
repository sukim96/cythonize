# Cythnoize: Example for cythonizing python package

## Introduction
https://www.notion.so/enerzai/Python-C-e9020be9e3634401b18ae9da50fed376

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