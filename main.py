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
    def __init__(self, filetypes, destination):
        self.filetypes = filetypes
        self.destination = destination
        self.moveFiles()
    fileArray = []
    renamedFilesArray = []
    filesRecognized = False
    destinationFiles = []
    fileTypeIsSorted = False
    itemsSorted = 0
    def buildArray(self):
        print("building the files to go to..." + self.destination)
        for file in downloadsList:  
            fileParts = os.path.splitext(downloadsPath+"\\"+file)
            for fileType in self.filetypes:
                if fileType == fileParts[1]:
                    self.fileTypeIsSorted = True
                    self.fileArray.append(file)
                    self.itemsSorted+=1

    def renameCopies(self):
        self.destinationFiles = os.listdir(self.destination)
        for file in self.fileArray:
            print(file)
            for fileInDestinationFolder in self.destinationFiles:
                if file == fileInDestinationFolder:
                    self.fileArray.remove(file)
                    print("the file: " + file + " is already in your destination folder!")
                    fullFileName = os.path.splitext(downloadsPath+"\\"+file)
                    fileName = fullFileName[0]
                    fileName += "(1)"
                    newFullFileName = fileName + fullFileName[1]
                    
                    print("The file was renamed: " + newFullFileName)
                    os.rename(downloadsPath + "\\" + file, fileName + fullFileName[1])
                    self.renamedFilesArray.append(fileName+fullFileName[1])

    def moveFiles(self):
        self.buildArray()
        self.renameCopies()
        #for item in self.fileArray:
            #print(item)
        for file in self.fileArray:
            fullFileName = downloadsPath + "\\" + file
            shutil.move(fullFileName, self.destination)
        for file in self.renamedFilesArray:
            shutil.move(file, self.destination)
            #if the filename is == to something already in that folder....
                #add a (1) to the name and copy it over.
        self.fileArray.clear()
        self.renamedFilesArray.clear()
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