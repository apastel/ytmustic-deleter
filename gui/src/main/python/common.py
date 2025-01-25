import os
import pathlib

import fbs_runtime

APP_DATA_DIR = str(
    pathlib.Path(os.getenv("APPDATA" if os.name == "nt" else "HOME")) / fbs_runtime.PUBLIC_SETTINGS["app_name"]
)