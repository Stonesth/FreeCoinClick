from cx_Freeze import setup, Executable

setup(
    name = "freecoinclick",
    version = "0.1",
    description = "",
    executables = [Executable("freecoinclick.py")]
)