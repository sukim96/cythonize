from setuptools import setup
from setuptools.extension import Extension

from Cython.Build import cythonize
from Cython.Distutils import build_ext
from pathlib import Path
import shutil


package_name = 'sample_package'


class MyBuildExt(build_ext):
    def run(self):
        build_ext.run(self)

        build_dir = Path(self.build_lib)
        root_dir = Path(__file__).parent

        target_dir = build_dir if not self.inplace else root_dir

        self.copy_file(Path(package_name) / '__init__.py', root_dir, target_dir)

    def copy_file(self, path, source_dir, destination_dir):
        if not (source_dir / path).exists():
            return
        shutil.copyfile(str(source_dir / path), str(destination_dir / path))


if __name__ == '__main__':
    with open('requirements.txt') as f:
        install_requires = f.read().strip().split('\n')

    setup(
        name="cythonize",
        version='0.0.1',
        description='Sample package for cythonize',
        author='Sungwoong Kim',
        python_requires='>=3',
        install_requires=install_requires,
        classifiers=[
            'Programming Language :: Python :: 3',
            'Programming Language :: Python :: 3.6',
            'Programming Language :: Python :: 3.7',
            'Programming Language :: Python :: 3.8',
        ],
        ext_modules=cythonize(
            [
                Extension(f"{package_name}.*", [f"{package_name}/*.py"]),
            ],
            build_dir="build",
            compiler_directives=dict(always_allow_keywords=True),
        ),
        cmdclass=dict(build_ext=MyBuildExt),
        packages=[],
    )
