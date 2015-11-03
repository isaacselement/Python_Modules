import os
import re
import sys


def translateStringsFileToDictionary(strings_file_path):
    with open(strings_file_path) as f:
        dictionary = {}
        line = f.readline()

        while line:
            keyValue = line.split('=')
            key = keyValue[1].strip()
            value = keyValue[0].strip()
            dictionary[key] = value
            line = f.readline()

        return dictionary


def extractToStringsFile(project_directory, strings_file_path=None):
    userHome = os.path.expanduser("~")
    previewOutput = open(userHome + '/Desktop/preview.txt', 'w')

    if strings_file_path is None:
        strings_file_path = userHome + '/Desktop/zh-Hans.strings'

    stringsOutput = open(strings_file_path, 'w')
    chineseArray = []

    for parent, dirnames, filenames in os.walk(project_directory):
            filenames = filter(lambda filename: filename[-2:] == '.m', filenames)

            for filename in filenames:
                fullname = os.path.join(parent, filename)
                previewOutput.write("\n\r" + "\n\r" + fullname + ":\n\r")

                with open(fullname) as f:
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
                                    chinese = element.encode('utf-8')
                                    previewOutput.write('\n\r')
                                    previewOutput.write(chinese)

                                    if chinese not in chineseArray:
                                        chineseArray.append(chinese)

                        line = f.readline()

    for i, chinese in enumerate(chineseArray):
        chinese = chinese.replace("@\"", "=")
        chinese = chinese.replace("\"", "")

        if i != 0:
            stringsOutput.write('\n\r')

        stringsOutput.write(chinese)

    previewOutput.close()
    stringsOutput.close()


def replaceFromStringsFile(project_directory, strings_file_path):
    for parent, dirnames, filenames in os.walk(project_directory):
            filenames = filter(lambda filename: filename[-2:] == '.m', filenames)

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
                        chinese = chinese.replace("@\"", "").replace("\"", "")
                        key = stringsDictionary[chinese]
                        command = "sed -i -e '" + str(lineNum) + "s/@\"" + chinese + "\"/" + re.escape(key) + "/g' " + fullname
                        print command
                        os.system(command)


if __name__ == '__main__':
    # extractToStringsFile(sys.argv[1], sys.argv[2])
    replaceFromStringsFile(sys.argv[1], sys.argv[2])
    # translateStringsFileToDictionary(sys.argv[1])
