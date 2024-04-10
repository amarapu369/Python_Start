def buildHomepage():
    global progressBarHome, consoleHome, rebootCore, rebootGnb, skipToProceed
    #Buttons
    progressBarHome = ttk.Progressbar(bgCanvas, orient="horizontal", length = 250, mode = "determinate")
    progressBarHome.grid(row=1, column=0, padx=50, pady=50, sticky=tk.NW)
    processBar(progressBarHome, val=10)

    consoleHome = tk.Text(bgCanvas, width=30, height = 8, bg = "black", fg = "#13FC0F", bd=5, font=('arial',11,'italic'))
    consoleHome.grid(row = 2, column =0, padx = 50, pady = 0, sticky=tk.NW)
    consoleHome.insert(tk.INSERT, "!!Welcome to FR2-ISC Platform!!\n")
    consoleHome.yview(tk.END)