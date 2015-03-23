# -*- mode: python -*-
from kivy.tools.packaging.pyinstaller_hooks import install_hooks
install_hooks(globals())

a = Analysis(['src/main.py'],
             pathex=['/opt/git/kivyMacBuild'],
             hiddenimports=[],
             runtime_hooks=None)
pyz = PYZ(a.pure)
exe = EXE(pyz,
          a.scripts,
          exclude_binaries=True,
          name='HelloWorld',
          debug=False,
          strip=None,
          upx=True,
          console=False )
coll = COLLECT(exe,
               Tree('src'),
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=None,
               upx=True,
               name='HelloWorld')
app = BUNDLE(coll,
             name='HelloWorld.app',
             icon=None)
