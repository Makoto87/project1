class File:
    def __init__(self,fileName,fileExtension,content,locked,parentFolder):
        self.fileName = fileName
        self.fileExtension = fileExtension
        self.content = content
        self.locked = locked
        self.parentFolder = parentFolder

    # 使われるファイルの最大容量を返します
    def getLifetimeBandwidthSize(self):
        dataOfAmount = len(self.content)
        if dataOfAmount >= 1000:
            return str(dataOfAmount / 1000) + "GB"
        else:
            return str(dataOfAmount) + "MB"

    # ファイルのタイプを返します
    def getFileType(self):
        if self.fileExtension == ".pdf" or self.fileExtension == ".word" or self.fileExtension == ".txt":
            return "document"
        elif self.fileExtension == ".js" or self.fileExtension == ".css" or self.fileExtension == ".html":
            return "source-code"
        elif self.fileExtension == ".mp4":
            return "video"
        elif self.fileExtension == ".mp3":
            return "music"
        else:
            return "no file type"

    # lockされていなければ、ファイルのコンテンツの先頭に文字を追加します
    def prependContent(self,data):
        if self.locked == False:
            self.content = data + self.content
        return self.content
    
    # lockされていなければ、ファイルのコンテンツの末尾に文字を追加します
    def appendContent(self,data):
        if self.locked == False:
            self.content += data
        return self.content

    # lockされていなければ、ファイルのコンテンツの途中に文字を追加します
    def addContent(self,data,position):
        if self.locked == False:
            self.content = self.content[:position] + data + self.content[position:]
        return self.content

    # 親ファイルと現在のファイルを返します。
    def showFileLocation(self):
        return self.parentFolder + " > " + self.fileName + self.fileExtension


assignment = File("assignment", ".word", "Something that occurs too early before preparations are ready. Starting too soon.", False, "homework")

print(assignment.getLifetimeBandwidthSize())
print(assignment.getFileType())
print(assignment.prependContent("good morning "))
print(assignment.appendContent(" good evening"))
print(assignment.addContent("hello world ", 13))
print(assignment.showFileLocation())