import win32com.client
import os

exportRoot =  os.getcwd()
exportRoot.replace('\\', '/')

def makePNG(dataset):
    psApp = win32com.client.Dispatch("Photoshop.Application")
    psApp.Open(r"C:/Users/gabdr/Documents/GitHub/Automated-Missed-Connections/template.psd")
    doc = psApp.Application.ActiveDocument
    layer_message = doc.ArtLayers["Message"]
    text_of_message = layer_message.TextItem
    layer_time = doc.ArtLayers["Timestamp"]
    text_of_time = layer_time.TextItem

    options = win32com.client.Dispatch('Photoshop.ExportOptionsSaveForWeb')
    options.Format = 6   # JPG
    options.Quality = 100 # Value from 0-100

    # For every key and value in the items of the dictionary "dict_sample"

    for i in range(len(dataset)):
        text_of_time.contents = str(dataset[i][0])
        text_of_message.contents = str(dataset[i][1])
        
        fileName = exportRoot + "/images/" + str(i) + ".jpg"

        print(fileName)
        
        doc.Export(ExportIn=fileName, ExportAs=2, Options=options)

def isEmpty():
    if len(os.listdir(exportRoot + "/images/")) == 0:
        return True
    else: 
        return False