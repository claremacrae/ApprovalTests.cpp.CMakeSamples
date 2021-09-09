#!/usr/bin/env python3

# traverse directory, and convert cmake files to include files for
# use in ApprovalTests.cpp documentation
#
# The CMake files in this directory are intended for inclusion in 
# ApprovalTests.cpp documentation.
# 
# Currently there is no way to tell mdsnippets to use
# cmake syntax for CMakeLists.txt files.
# 
# So for now, I'm copying these CMake files on to that
# repo, converted to Markdown format, for inclusion
# in the documentation there.

import os

def remove_unwanted_dirs(dirs):
    kept_dirs = []
    excluded = ['.git', '.idea', 'build']
    for dir in dirs:
        if dir.startswith('cmake-build'):
            continue
        if dir in excluded:
            continue
        kept_dirs.append(dir)
    return kept_dirs


def is_wanted_file(file):
    if os.path.splitext(file)[1] == '.cmake':
        return True
    if file == 'CMakeLists.txt':
        return True
    if file == 'conanfile.txt':
        return True
    if file == 'build.sh':
        return True
    if file == 'vcpkg.json':
        return True
    return False


def get_syntax_name(file_base_name, file_extension):
    print(file_base_name, file_extension)
    if file_extension == ".sh":
        return 'bash'
    if file_extension == ".json":
        return 'json'
    if file_base_name == 'CMakeLists' or file_extension == ".cmake":
        return 'cmake'
    return ''


def show_for_markdown(root, file):
    top_level = os.path.split(root)[0]
    if top_level == '.' or top_level == '':
        top_level = root

    rel_path = os.path.join(root, file)
    abs_path = os.path.abspath(rel_path)
    url_to_file = F'https://github.com/claremacrae/ApprovalTests.cpp.CMakeSamples/blob/main/{rel_path}'

    dir_name = os.path.normpath(root).replace('/', '_')
    file_base_name = os.path.splitext(file)[0]
    file_extension = os.path.splitext(file)[1]
    syntax_name = get_syntax_name(file_base_name, file_extension)

    output_dir=f'{top_level}/mdsource'
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    output_file = f'{top_level}/mdsource/inc_{dir_name}_{file_base_name.lower()}.include.md'
    print(output_file)
    with open(output_file, 'w') as s:
        s.write('\n')
        s.write('\n')
        s.write(f'```{syntax_name}\n')
        with open(abs_path) as f:
            s.write(f'{"".join(f.readlines())}')
        s.write('```\n')
        s.write(F"<sup><a href='{url_to_file}' title='File snippet was copied from'>snippet source</a></sup>\n")
        s.write('\n')


for root, dirs, files in os.walk(".", topdown=True):
    dirs[:] = remove_unwanted_dirs(dirs)
    for file in files:
        if not is_wanted_file(file):
            continue
        show_for_markdown(root, file)
