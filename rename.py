
import os
wkd = os.getcwd()

def rename(season: int, fileExt: str, folder: str):
    files = os.listdir(wkd+'/'+folder)
    for i in range(0,len(files)):
        files[i] = files[i].replace('.'+fileExt, "")
    #print(files)
    for count, filename in enumerate( sorted( files, key=int) ):
        seasonStr = "s"
        ep = "e"
        if season < 10:
            seasonStr += '0'+str(season)
        else:
            seasonStr += str(season)
        if count < 9:
            ep = "e0"+str(count+1)
        else:
            ep = "e"+str(count+1)
        dst = seasonStr + ep+ "."+fileExt

        src = wkd +"/"+folder+"/"+ filename + '.' +fileExt
        print("Renaming "+filename+ " to " + dst + '\n')
        
        dst = wkd +"/"+folder+"/"+ dst
        os.rename(src,dst)
        
def renameToOnlyNum(fileExt: str, folder: str):
    for count, filename in enumerate( os.listdir(wkd+'/'+folder )):
        newFilename = ""
        for char in filename:
            if char == '.':
                break
            if char.isnumeric():
                newFilename += char
        src = wkd +"/"+folder+"/"+ filename
        dst = wkd +"/"+folder+"/"+ newFilename + '.' +fileExt
        print("Renaming "+filename+ " to " + dst + '\n')
        os.rename(src,dst)

def main():
    season = input("What season is it? ")
    fileExt = input("What is the file extension? ")
    folder = input("What folder to modify? ")
    renameToOnlyNum(fileExt, folder)
    rename(int(season), fileExt, folder)

if __name__ == "__main__":
    main()
