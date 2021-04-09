# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#   kmdiff
#   Authors: T. Lemane
#
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU Affero General Public License as
#  published by the Free Software Foundation, either version 3 of the
#  License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU Affero General Public License for more details.
#
#  You should have received a copy of the GNU Affero General Public License
#  along with this program.  If not, see <http://www.gnu.org/licenses/>.
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

from github import Github
import os
import sys
import platform

py_path = os.path.dirname(os.path.abspath(__file__))
sys.path.append(py_path+'/..')

kmdiff_version = "0.0.1"

system = platform.system()

LINUX, OSX = system == 'Linux', system == 'Darwin'

PACKAGE_NAME = f'kmdiff-{kmdiff_version}-bin-{system}.tar.gz'
PACKAGE_PATH = f'{py_path}/../build/{PACKAGE_NAME}'
try:
    d = sys.argv[1]
    PACKAGE_PATH = f'{d}/{PACKAGE_NAME}'
except IndexError:
    pass

PACKAGE_EXISTS = os.path.exists(PACKAGE_PATH)

GH_TOKEN = os.environ['GH_TOKEN']

BUILD_INFO = ''

release_desc_path = f'{py_path}/../doc/releases/desc-{kmdiff_version}.txt'
if os.path.exists(release_desc_path):
    with open(release_desc_path, 'r') as desc_in:
        BUILD_INFO = desc_in.read()

g = Github(GH_TOKEN)
u = g.get_user()
lz4_repo = u.get_repo('kmdiff')

LATEST_VERSION = []
try:
    latest_release = lz4_repo.get_latest_release()
    assets = latest_release.get_assets()
    assets_name = [asset.name for asset in assets]
    tag_name = latest_release.tag_name
    tag_name = tag_name[1:] if tag_name.startswith('v') else tag_name
    LATEST_VERSION = list(map(int, tag_name.split('.')))
except:
    pass

CURRENT_VERSION = list(map(int, kmdiff_version.split('.')))

print(BUILD_INFO)
print(system)
print(PACKAGE_EXISTS)
print(PACKAGE_PATH)
print(LATEST_VERSION, CURRENT_VERSION)

if not CURRENT_VERSION == [0, 0, 0]:
    if CURRENT_VERSION > LATEST_VERSION or not LATEST_VERSION:
        if PACKAGE_EXISTS:
            release = lz4_repo.create_git_release(
                f'v{kmdiff_version}',
                f'Release v{kmdiff_version}',
                BUILD_INFO, False, prerelease=False)
            release.upload_asset(PACKAGE_PATH)
        else:
            print('Package bad version')
    elif CURRENT_VERSION == LATEST_VERSION:
        if PACKAGE_NAME not in assets_name:
            latest_release.upload_asset(PACKAGE_PATH)
    else:
        print('Nothing to upload')
