import os
import shutil

#target the downloads folder and get all the exe files from it.
user = os.getlogin()
downloadsPath = "C:\\Users\\"+user+"\\Downloads"
downloadsList = os.listdir(downloadsPath)

#where to put the files
targetFolders = [
    "C:\\Users\\"+user+"\\Downloads\\EXES", 
    "C:\\Users\\"+user+"\\Downloads\\DOCX",
    "C:\\Users\\"+user+"\\Downloads\\PDF",
    "C:\\Users\\"+user+"\\Downloads\\IMAGE",
    "C:\\Users\\"+user+"\\Downloads\\AUDIO AND VIDEO",
    "C:\\Users\\"+user+"\\Downloads\\ZIP"

]

class SortType:
    #filetypes is an array containing the 
    def __init__(self, filetypes, destiniation):
        self.filetypes = filetypes
        self.destiniation = destiniation
        self.moveFiles()
    fileArray = []

    def buildArray(self):
        print("building the files to go to..." + self.destiniation)
        for file in downloadsList:  
            fileParts = os.path.splitext(downloadsPath+"\\"+file)
            for fileType in self.filetypes:
                if fileType == fileParts[1]:
                    self.fileArray.append(file)
    def moveFiles(self):
        self.buildArray()
        for item in self.fileArray:
            print(item)
        for file in self.fileArray:
            shutil.move(downloadsPath+"\\"+file, self.destiniation)
        self.fileArray.clear()
        print("DONE \n\n\n\n\n\n")
                
                
#add new file types here. They get automatically updated.
toSort = {

    "installerFiles":SortType([".exe", ".msi"],targetFolders[0]),

    "pdfFiles":SortType([".pdf"], targetFolders[2]),

    "mediaFiles": SortType([".mp3", ".mp4",".mov",".wav",".MP4"], targetFolders[4]),

    "microsoftWordFiles":SortType([".docx",".doc"], targetFolders[1]),

    "imagesFiles":SortType([".jpg", ".jpeg",".JPEG",".JPG",".png",".gif",".svg",".NEF"], targetFolders[3]),

    "zipFiles":SortType([".zip"], targetFolders[5]),

    "xmpFiles":SortType([".xmp"],targetFolders[3])
}
