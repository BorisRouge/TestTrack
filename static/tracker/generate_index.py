#!/usr/bin/env python3


import sys


for filename in sys.argv[1:]:
    if filename == 'index.html':
        continue

    print(f'''
              <tr>
                <td class="relative py-4 pl-4 pr-3 text-sm sm:pl-6">
                  <div class="font-medium text-gray-900">
                    <a href="{filename}"><u>{filename}</u></a>
                  </div>
                </td>
              </tr>''')
