from distutils.core import setup, Extension
setup(name='libsvm_py',
      version='323',
      package_dir = {'' : 'python'},
      py_modules=['svm', 'svmutil', 'commonutil'],
      #ext_modules=[Extension('libsvm', ['svm.cpp'])],
      )
