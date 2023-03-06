import cx_Freeze

executables = [cx_Freeze.Executable("coin.py")]

cx_Freeze.setup(
    name = "Baby-Eater",
    options = {"build_exe": {"packages":["pygame"],
               "include_files":["./fonts/creepy.ttf", "./images/demon.png", "./images/baby.png", "./images/coin.png", "./images/fox.png"]}},
    executables = executables
)