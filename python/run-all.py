# Runs all Python files from this folder (except for this of course) and then
# moves all PDF files from this folder to "../latex".


import os


for f in os.listdir('.'):

    if f == 'run-all.py':
        continue


    if os.path.splitext(f)[-1] == '.py':
        print(f'Executing file \'{f}\'..')
        exec(open(f).read())
    else:
        continue


for f in os.listdir('.'):

    if os.path.splitext(f)[-1] == '.pdf':
        dst = '../latex/' + f
        print(f'Moving \'{f}\' to \'{dst}\'...')
        os.rename(f, dst)


print('Done.')
