from fabricate import *

sources = ['test01', ]

def build():
    compile()
    link()

def compile():
    compiler_options = [ '-Wall',
                         '-std=c++11' ]

    for source in sources:
        run('g++', compiler_options, '-c', source+'.cpp')

def link():
    objects = [s+'.o' for s in sources]
    run('g++', '-o', 'program.out', objects)

def clean():
    autoclean()

main()