import os
import shutil

#target the downloads folder
user = os.getlogin()
downloadsPath = "C:\\Users\\"+user+"\\Downloads"
downloadsList = os.listdir(downloadsPath)

#where to put the files. You can change these, they just need to exist in your file system. This is just how mine's set up.
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
        self.moveFiles()#combines object instantiation with method call. Now whenever a new SortType object is created, moveFiles() is automatically called.

    #utility variables if you will.   
    fileArray = []
    renamedFilesArray = []
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
        """
        suppose you move a file "x.file" from downloads to a subfolder named "folderY". Then you later re-download a second "x.file" back into downloads and run the script to sort it into "folder Y". 
        Because Windows does not see another "x.file" in the Downloads folder (it doesn't look through subfolders, namely "folderY") it doesn't re-name it "x(1).file".
        When you run the script to move the new "x.file" into the "folderY", python throws an error because you are moving a file("x.file") into the folder with something already named that exact thing.
        So, this function automatically looks for duplicates and updates them adding a "(1)" at the end of the file name before moving.  
        """
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
                    newFullFilePath = fileName + fullFileName[1]#this gives the files full path, not just the name.
                    print("The file was renamed: " + newFullFilePath)
                    os.rename(downloadsPath + "\\" + file, fileName + fullFileName[1])
                    self.renamedFilesArray.append(fileName+fullFileName[1])#create a new array that holds the duplicate files.

    def moveFiles(self):
        self.buildArray()#the order of these functions is extremely important.
        self.renameCopies()
        for file in self.fileArray:
            fullFileName = downloadsPath + "\\" + file
            shutil.move(fullFileName, self.destination)
        for filePath in self.renamedFilesArray:
            shutil.move(filePath, self.destination)  
        self.fileArray.clear()
        self.renamedFilesArray.clear()
        print("DONE \n\n\n\n\n\n")
      
#add new file types here. They get automatically updated and run because moveFiles() is automatically called in the constructor of the SortType class.
toSort = {
    "installer files":SortType([".exe", ".msi"],targetFolders[0]),
    "pdf files":SortType([".pdf"], targetFolders[2]),
    "media files": SortType([".mp3", ".mp4",".mov",".wav",".MP4",".m4a"], targetFolders[4]),
    "microsoft word files":SortType([".docx",".doc",".xls",".xlsx",".pptx",".pptm",".accdb",".one",".xps",".csv"], targetFolders[1]),
    "images files":SortType([".jpg", ".jpeg",".JPEG",".JPG",".png",".gif",".svg",".NEF",".xmp",".ico"], targetFolders[3]),
    "zip files":SortType([".zip"], targetFolders[5]),
}

#print out a summary of what happened
for itemKey, itemValue in toSort.items():
    print("Sorted the "+ itemKey.capitalize() +  ": " + str(itemValue.fileTypeIsSorted) + "\n Number of Files:" + str(itemValue.itemsSorted) + "\n\n")