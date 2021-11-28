# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(['/storage/James Codes/Python/CYB/Test/Merlin.py'],
             pathex=[],
             binaries=[],
             datas=[('/storage/James Codes/Python/CYB/Test/cyb.json', '.'), ('/storage/James Codes/Python/CYB/Test/EmailBody.txt', '.'), ('/storage/James Codes/Python/CYB/Test/EmailSubject.txt', '.')],
             hiddenimports=[],
             hookspath=[],
             hooksconfig={},
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)

exe = EXE(pyz,
          a.scripts, 
          [],
          exclude_binaries=True,
          name='Merlin',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=False,
          disable_windowed_traceback=False,
          target_arch=None,
          codesign_identity=None,
          entitlements_file=None , icon='Merlin-Icon.ico')
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas, 
               strip=False,
               upx=True,
               upx_exclude=[],
               name='Merlin')
