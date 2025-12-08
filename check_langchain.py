import importlib, pkgutil, sys, os
try:
    m = importlib.import_module('langchain.document_loaders')
    print('OK: imported langchain.document_loaders')
    print('submodules:', [n for _, n, _ in pkgutil.iter_modules(m.__path__)])
except Exception as e:
    print('ERROR importing langchain.document_loaders:', e)
    try:
        import langchain
        print('langchain module file:', getattr(langchain, '__file__', '<no file>'))
        d = os.path.dirname(langchain.__file__)
        print('langchain directory listing (first 50 entries):')
        print(os.listdir(d)[:50])
    except Exception as e2:
        print('ERROR importing langchain itself:', e2)
sys.exit(0)
