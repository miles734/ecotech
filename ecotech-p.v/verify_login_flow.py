import os
import tempfile
from pathlib import Path
from unittest.mock import patch

os.environ['DB_ENGINE'] = 'sqlite'
os.environ['DB_NAME'] = str(Path(tempfile.mkdtemp()) / 'ecotech.db')

import main

with patch('main.limpiar_consola'), patch('main.solicitar_login', return_value={'id': 1, 'empleado_id': 1, 'nombre_usuario': 'admin', 'rol': 'admin'}), patch('main.menu_privado', return_value='0'):
    try:
        main.main()
    except SystemExit:
        pass

print('LOGIN_FLOW_OK')
