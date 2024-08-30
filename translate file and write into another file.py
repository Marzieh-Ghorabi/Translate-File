import tkinter
import translate

window=tkinter.Tk()
window.config(padx=30,pady=20)
window.minsize(width=300,height=200)
window.title("Translator")

source_lbl=tkinter.Label(text="Source Path")
source_lbl.grid(row=1,column=0)

entry_source_lbl=tkinter.Entry(width=30)
entry_source_lbl.grid(row=1,column=1)


dest_lbl=tkinter.Label(text="Destination Path")
dest_lbl.grid(row=2,column=0)

entry_dest_lbl=tkinter.Entry(width=30)
entry_dest_lbl.grid(row=2,column=1)


def Translate_Button_Cliked():
    source_path=entry_source_lbl.get()
    with open(source_path) as source_file:
        source_text=source_file.read()

        trn = translate.Translator(to_lang="fa")
        destination_text=trn.translate(source_text)

    destination_path=entry_dest_lbl.get()
    with open(destination_path,mode="w",encoding="utf8") as destination_file:
           destination_file.write(destination_text)

Translate_Button=tkinter.Button(text="Translate",command=Translate_Button_Cliked)
Translate_Button.grid(row=3,column=1)
window.mainloop()
