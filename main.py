import os
import shutil

#target the downloads folder and get all the exe files from it.
user = os.getlogin()
downloadsPath = "C:\\Users\\"+user+"\\Downloads"
downloadsList = os.listdir(downloadsPath)

#where to put the files
targetFolders = [
    "C:\\Users\\"+user+"\\Downloads\\EXES", 
    "C:\\Users\\"+user+"\\Downloads\\OFFICE FILES",
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
    fileTypeIsSorted = False
    itemsSorted = 0
    def buildArray(self):
        print("building the files to go to..." + self.destiniation)
        for file in downloadsList:  
            fileParts = os.path.splitext(downloadsPath+"\\"+file)
            for fileType in self.filetypes:
                if fileType == fileParts[1]:
                    self.fileTypeIsSorted = True
                    self.fileArray.append(file)
                    self.itemsSorted+=1

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

    "installer files":SortType([".exe", ".msi"],targetFolders[0]),

    "pdf files":SortType([".pdf"], targetFolders[2]),

    "media files": SortType([".mp3", ".mp4",".mov",".wav",".MP4",".m4a"], targetFolders[4]),

    "microsoft word files":SortType([".docx",".doc",".xls",".xlsx",".pptx",".pptm",".accdb",".one",".xps",".csv"], targetFolders[1]),

    "images files":SortType([".jpg", ".jpeg",".JPEG",".JPG",".png",".gif",".svg",".NEF",".xmp",".ico"], targetFolders[3]),

    "zip files":SortType([".zip"], targetFolders[5]),
}

for itemKey, itemValue in toSort.items():
    print("Sorted the "+ itemKey.capitalize() +  ": " + str(itemValue.fileTypeIsSorted) + "\n Number of Files:" + str(itemValue.itemsSorted) + "\n\n")
