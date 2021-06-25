import cx_Freeze
executables = [cx_Freeze.Executable(
    script="jogológica.py", icon="icones/icon.ico")]

cx_Freeze.setup(
    name="Torre de Hanoi",
    options={
        "build_exe": {
            "packages": ["pygame"],
            "include_files": ["icones", "sounds", "libs.py", "historia.txt"]
        }},
    executables=executables
)
