import subprocess

toc_items = open('SUMMARY.md', 'r').read().splitlines()

counter = 0
for toc_item in toc_items:
    if toc_item.startswith('*'):
        counter+=1
        md_filename = toc_item.split('(')[-1][:-1]
        subprocess.run(['notedown', 
                        md_filename, 
                        '--from', 'markdown',
                        '--to', 'notebook', 
                        '--output', f"{counter}_{md_filename.replace('.md','.ipynb')}"],
                        shell=True, capture_output=True)