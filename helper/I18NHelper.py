import os
import re
import sys


__Format__ = '.h'


def translateStringsFileToDictionary(strings_file_path):
    with open(strings_file_path) as f:
        dictionary = {}
        line = f.readline()

        while line:
            line = line.strip()
            if '=' in line:
                keyValue = line.split('=')
                key = keyValue[0]
                value = keyValue[1].replace(';', '')
                dictionary[value] = key

            line = f.readline()

        return dictionary


def extractToStringsFile(project_directory, strings_file_path=None):
    userHome = os.path.expanduser("~")
    if strings_file_path is None:
        strings_file_path = userHome + '/Desktop/zh-Hans.strings'

    stringsOutput = open(strings_file_path, 'w')
    chineseArray = []
    previewOutput = open(userHome + '/Desktop/preview.txt', 'w')

    for parent, dirnames, filenames in os.walk(project_directory):
            filenames = filter(lambda filename: filename[-2:] == __Format__, filenames)

            for filename in filenames:
                fullname = os.path.join(parent, filename)

                with open(fullname) as f:
                    flag = 0
                    line = f.readline()

                    while line:
                        matchLine = re.match(ur".*(@\"\w*[\u4e00-\u9fa5]+\w*\")", line.decode('utf-8'))

                        if matchLine:
                            result = matchLine.group()
                            result = result.encode('utf-8')

                            if all(s not in result for s in ['DLog', 'NSLog']):
                                pattern = re.compile(ur"@\"\w*[\u4e00-\u9fa5]+\w*\"", re.IGNORECASE)
                                matches = pattern.findall(line.decode('utf-8'))

                                for element in matches:
                                    if flag == 0:
                                        previewOutput.write("\n\r" + "\n\r" + fullname + ":\n\r")
                                        flag = 1

                                    chinese = element.encode('utf-8')
                                    previewOutput.write('\n\r')
                                    previewOutput.write(chinese)

                                    if chinese not in chineseArray:
                                        chineseArray.append(chinese)

                        line = f.readline()

    for i, chinese in enumerate(chineseArray):
        chinese = chinese.replace("@", "\"\"=") + ';'

        if i != 0:
            stringsOutput.write('\n')

        stringsOutput.write(chinese)

    previewOutput.close()
    stringsOutput.close()


def replaceFromStringsFile(project_directory, strings_file_path=None):
    userHome = os.path.expanduser("~")
    if strings_file_path is None:
        strings_file_path = userHome + '/Desktop/zh-Hans.strings'

    for parent, dirnames, filenames in os.walk(project_directory):
            filenames = filter(lambda filename: filename[-2:] == __Format__, filenames)

            stringsDictionary = translateStringsFileToDictionary(strings_file_path)
            for filename in filenames:
                fullname = os.path.join(parent, filename)

                lineNumChineses = {}
                with open(fullname) as f:
                    line = f.readline()
                    lineNumber = 0

                    while line:
                        lineNumber += 1
                        matchLine = re.match(ur".*(@\"\w*[\u4e00-\u9fa5]+\w*\")", line.decode('utf-8'))

                        if matchLine:
                            result = matchLine.group()
                            result = result.encode('utf-8')

                            if all(s not in result for s in ['DLog', 'NSLog']):
                                pattern = re.compile(ur"@\"\w*[\u4e00-\u9fa5]+\w*\"", re.IGNORECASE)
                                matches = pattern.findall(line.decode('utf-8'))

                                elements = []
                                for element in matches:
                                    chinese = element.encode('utf-8')
                                    elements.append(chinese)

                                lineNumChineses[lineNumber] = elements

                        line = f.readline()

                for (lineNum, elements) in lineNumChineses.items():
                    for chinese in elements:
                        try:
                            chinese = chinese.replace("@", "")
                            i18nkey = stringsDictionary[chinese]
                            i18nkey = re.escape(i18nkey)
                            i18nkey = "LOCALIZE(@" + i18nkey + ")"
                            command = "sed -i -e '" + str(lineNum) + "s/@" + chinese + "/" + i18nkey + "/g' " + fullname
                            print command
                            os.system(command)
                        except KeyError as e:
                            print "Replacing Error. " + chinese + " Line " + str(lineNum) + " , " + os.path.basename(fullname)
                            print (e)


def handleFileContents(file_path):
    with open(file_path) as f:
        temp_file_path = os.path.dirname(file_path) + '/' + '_____' + os.path.basename(file_path)
        tempFileOutput = open(temp_file_path, 'w')
        line = f.readline()
        lineNumber = 0
        while line:
            lineNumber += 1
            tempFileOutput.write(line.strip() + ';' + '\n')
            line = f.readline()
        tempFileOutput.flush()
        tempFileOutput.close()


if __name__ == '__main__':
    project_directory = sys.argv[1]
    strings_file_path = sys.argv[2] if len(sys.argv) >= 3 else None
    user_input = raw_input("Select your action: 1 for extract , 2 for replace , 3 for extract & replace , 4 for Handle One File\n")
    if user_input == '1':
        extractToStringsFile(project_directory, strings_file_path)
    elif user_input == '2':
        replaceFromStringsFile(project_directory, strings_file_path)
    elif user_input == '3':
        extractToStringsFile(project_directory, strings_file_path)
        user_input = raw_input("After you finish the .strings files keys, hit any key to continue:\n")
        replaceFromStringsFile(project_directory, strings_file_path)

    elif user_input == '4':
        handleFileContents(sys.argv[1])
