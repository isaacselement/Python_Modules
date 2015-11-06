import os
import re
import sys


__UserHome__ = os.path.expanduser("~")
__CommentRegxLine__ = ur".*//"
__ChineseRegxLine__ = ur".*@\".*[\u4e00-\u9fa5]+.*\""
__BraketWorldRegx__ = r"@\".*?\""
__ChineseRegx__ = ur"@\".*[\u4e00-\u9fa5]+.*\""


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


def getStringsFilePath(strings_file_path=None):
    if strings_file_path is None:
        strings_file_path = __UserHome__ + '/Desktop/zh-Hans.strings'

    return strings_file_path


def getPreviewFilePath(preview_file_path=None):
    if preview_file_path is None:
        preview_file_path = __UserHome__ + '/Desktop/preview.txt'

    return preview_file_path


def translateStringsFileToDictionary(strings_file_path=None):
    strings_file_path = getStringsFilePath(strings_file_path)
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


def writeChineseArrayToStringsFile(chineseArray, strings_file_path=None):
    strings_file_path = getStringsFilePath(strings_file_path)
    stringsOutput = open(strings_file_path, 'w')
    for i, chinese in enumerate(chineseArray):
        chinese = '""=' + chinese[1:] + ';'

        if i != 0:
            stringsOutput.write('\n')

        stringsOutput.write(chinese)

    stringsOutput.close()


def iterateDirectory(project_directory, handler):
    for parent, dirnames, filenames in os.walk(project_directory):
        filenames = filter(lambda filename: filename[-2:] == '.h' or filename[-2:] == '.m' and filename != 'AppEmoji.m' and filename != 'EmojiQQ.m' and filename != 'ImageUtil.m', filenames)

        for filename in filenames:
            fullname = os.path.join(parent, filename)
            handler(fullname)


def iterateChineseInFile(full_file_name, handler):
    with open(full_file_name) as f:
        line = f.readline()
        lineNumber = 0
        while line:
            lineNumber += 1
            matchLine = re.match(__ChineseRegxLine__, line.decode('utf-8'))
            matchCommentLine = re.match(__CommentRegxLine__, line)

            if matchLine and matchCommentLine is None:
                result = matchLine.group()
                result = result.encode('utf-8')

                if all(s not in result for s in ['DLog', 'NSLog']):
                    pattern = re.compile(__BraketWorldRegx__, re.IGNORECASE)
                    matches = pattern.findall(result.decode('utf-8'))

                    for element in matches:
                        chineseMatch = re.match(__ChineseRegx__, element)
                        if chineseMatch:
                            chinese = chineseMatch.group().encode('utf-8')
                            handler(chinese, lineNumber, full_file_name)

            line = f.readline()


def extractToStringsFile(project_directory, strings_file_path=None):
    chineseArray = []
    previousName = ['']
    previewOutput = open(getPreviewFilePath(), 'w')

    def handlerChinese(chinese, lineNumber, fullname):
        if previousName[0] != fullname:
            previewOutput.write("\n\r" + "\n\r" + fullname + ":\n\r")
            previousName[0] = fullname

        previewOutput.write('\n\r')
        previewOutput.write(chinese)

        if chinese not in chineseArray:
            chineseArray.append(chinese)

    def handlerDirectory(full_file_name):
        iterateChineseInFile(full_file_name, handlerChinese)

    iterateDirectory(project_directory, handlerDirectory)
    previewOutput.close()
    writeChineseArrayToStringsFile(chineseArray)


def replaceFromStringsFile(project_directory, strings_file_path=None):
    strings_file_path = getStringsFilePath(strings_file_path)
    stringsDictionary = translateStringsFileToDictionary(strings_file_path)

    def handlerChinese(chinese, lineNumber, fullname):
        try:
            chinese = chinese[1:]
            i18nkey = stringsDictionary[chinese]
            i18nkey = re.escape(i18nkey)
            i18nkey = "LOCALIZE(@" + i18nkey + ")"
            chinese = chinese.replace('[', '\[').replace(']', '\]').replace('/', '\/').replace('*', '\*')
            command = "sed -i -e '" + str(lineNumber) + "s/@" + chinese + "/" + i18nkey + "/g' " + fullname
            print command
            os.system(command)
        except KeyError as e:
            print "Replacing Error. " + chinese + " Line " + str(lineNumber) + " , " + os.path.basename(fullname)
            print (e)

    def handlerDirectory(full_file_name):
        iterateChineseInFile(full_file_name, handlerChinese)

    iterateDirectory(project_directory, handlerDirectory)


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
