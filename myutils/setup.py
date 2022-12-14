from setuptools import setup      # 외부모듈 만들기 위한 도구

#2.대 는 __init__.py 가 필수였었음

setup(name='jputils',
      version='0.0.1',
      description='util modules by Jade',
      url='https://github.com/indiflex/jputils',            
      author='Jade IndiFlex',
      author_email='indiflex.corp@gmail.com',
      license='MIT',
      packages=['jputils'],                        # packages=['.']는 현재 디렉토리에 모듈담음, packages=['jputils'] jputils 폴더 새로 만들어서 모듈 담음
	install_requires=['requests'],              # 내가 필요로 하는 외부 라이브러리
      zip_safe=False)