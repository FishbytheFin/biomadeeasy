import os

HTMLFILENAME = ""
lastQuestion = ""  # A really fucking stupid varible needed because the file has the questions on different lines from the answer
outputText = ""  # text to be outputted to output.txt

# Searches the input folder for html files and sets the first found as HTMLFILENAME
for file in os.listdir("input"):
    if file.endswith(".html"):
        HTMLFILENAME = os.path.join("input", file)

with open(HTMLFILENAME, "r") as f:
    for i in f.readlines():
        if "<li><div><span class=\"quia_standard\">" in i:
            print(i)
            lastQuestion = i.replace("<li><div><span class=\"quia_standard\">", "").split(
                "<")[0]  # dum line of code that grabs the question from the line
        else:
            j = i.split("<td class=\"quia_standard\">")
            for t in j:
                if "(correct answer)" in t:
                    # adds the answer and the question to a var for later
                    outputText += lastQuestion + ": " + t.split("(")[0] + "\n\n"

with open("output.txt", "w") as o:
    o.write(outputText)
