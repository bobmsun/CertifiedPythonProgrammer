
# 这里干的事情是 make our package installable，需要用到 setuptools

from setuptools import find_packages, setup

setup(
    name="words",
    version="1.0.0",
    description="Helper library for working with random works",
    package_dir={"": "src"},
    padkages=find_packages(where="src")
)


# cd packages/words

# pip3.7 install --upgarde wheel   (先use pip to install wheel, 或 upgrade it if it's already there )
# (上一行出了 EnvironmentError: [ERRNO 13] Permission denied 之后, run 下面的，加了一个 --user)
# pip3.7 install --user --upgarde wheel

# python3.7 setup.py bdist_wheel    （to build the distributuion that can be installed）
# (这一句 run完了之后，在 packages/words 下面，与 src 同级，出现了 build 和 dist 文件夹
# 同时，在package/words/src/words下，与__init__.py 和 generator.py 同级也会出现一个 words.egg-info)
 
# pip3.7 install --user ~/packages/words/dist/words-1.0.0-py3-none-any.whl   
# （with that build, 这里我们就可以 install package了, 这里的 path 是教程中用到 老师的 绝对 path）



