import os
import json

def setup_mern_stack():
    # ------------------ < client > ------------------
    ''' Setting up client '''
    # ------------------ < client > ------------------
    
    os.system("cls")
    print("\nSetting Up Client Folder...")
    os.system("mkdir client && mkdir server")
    os.chdir("client")
    os.system("npm create vite@latest . -- --template react && npm install")
    os.system("cls")
    package_new_inquire = str(input("\nEnter Package Name To Add [ space separated ] or leave blank: "))
    tailwind = str(input("Would you like to add tailwind css to the project?(y/n): ")).lower()
    if tailwind == 'y':
        os.system("npm install -D tailwindcss postcss autoprefixer")
        os.system("npx tailwindcss init -p")
        data = """
/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {},
  },
  plugins: [],
}
"""
        with open('tailwind.config.js', 'w') as twconfig:
            twconfig.write(data.strip())
    if package_new_inquire == "":
        try:
            if tailwind == 'y':
                os.system(f"npm i --silent react-icons axios react-router-dom")
                os.system("cls")
                print("You did not add module yourself, so I added the following: \n✅ react-icons\n✅ axios\n✅ tailwind\n✅ react-router-dom")
            else:
                os.system(f"npm i --silent react-icons axios react-router-dom sass ")
                os.system("cls")
                print("You did not add module yourself, so I added the following: \n✅ react-icons\n✅ axios\n✅ sass\n✅ react-router-dom")
        except:
            print("\nAn Error Occured. Couldn't install default packages...")
    else:
        try:
            os.system(f"npm i --silent {package_new_inquire.rstrip()}")
            os.system("cls")
            print("✅ You installed the following packages: ", package_new_inquire)
        except:
            print("\nAn Error Occured. Make Sure You Entered A Valid Package name...")



    # ------------------ < client /src > ------------------
    ''' client src modification '''
    # ------------------ < client /src > ------------------

    os.chdir('src')
    os.system('mkdir components && mkdir styles && mkdir pages && mkdir hooks && mkdir utils && mkdir context')

    with open('App.css', 'w') as stylefile:
        stylefile.write('')
        
    with open('index.css', 'w') as indexstylefile:
        if tailwind == 'y':
            indexstylefile.write("@import url('https://fonts.googleapis.com/css2?family=Montserrat:ital,wght@0,400;0,500;0,600;0,700;0,800;0,900;1,400;1,500;1,600;1,700;1,800;1,900&family=Nunito+Sans:ital,opsz,wght@0,6..12,400;0,6..12,500;0,6..12,600;0,6..12,700;0,6..12,800;0,6..12,900;0,6..12,1000;1,6..12,400;1,6..12,500;1,6..12,600;1,6..12,700;1,6..12,800;1,6..12,900;1,6..12,1000&family=Poppins:ital,wght@0,400;0,500;0,600;0,700;0,800;0,900;1,400;1,500;1,600;1,700;1,800;1,900&display=swap');\n\n@tailwind base;\n@tailwind components;\n@tailwind utilities;\n\n/* Fonts: Poppins, Nunito Sans, Montserrat */ \n\n*, ::before, ::after {\n\n\tmargin: 0;\n\tpadding: 0;\n\tbox-sizing: border-box;\n\n}\n")
        else:
            indexstylefile.write("@import url('https://fonts.googleapis.com/css2?family=Montserrat:ital,wght@0,400;0,500;0,600;0,700;0,800;0,900;1,400;1,500;1,600;1,700;1,800;1,900&family=Nunito+Sans:ital,opsz,wght@0,6..12,400;0,6..12,500;0,6..12,600;0,6..12,700;0,6..12,800;0,6..12,900;0,6..12,1000;1,6..12,400;1,6..12,500;1,6..12,600;1,6..12,700;1,6..12,800;1,6..12,900;1,6..12,1000&family=Poppins:ital,wght@0,400;0,500;0,600;0,700;0,800;0,900;1,400;1,500;1,600;1,700;1,800;1,900&display=swap');\n\n/* Fonts: Poppins, Nunito Sans, Montserrat */ \n\n*, ::before, ::after {\n\n\tmargin: 0;\n\tpadding: 0;\n\tbox-sizing: border-box;\n\n}\n")
    
    with open('App.jsx', 'w') as AppFile:
        if tailwind == 'y':
            AppFile.write("const App = () => {\n\treturn (\n\t\t<h1 className='text-3xl font-bold underline'>Hello World!</h1>\n\t)\n}\nexport default App")
        

    # ------------------ < server > ------------------
    '''Setting up server'''
    # ------------------ < server > ------------------

    os.chdir('..\\..\\server')
    package_new_inquire_b = str(input("\nEnter Package Name To Add [ space separated ] or leave blank: "))
    if package_new_inquire_b == "":
        os.system("npm init -y && npm i --silent express mongoose cors bcryptjs dotenv multer cookie-parser jsonwebtoken")
        os.system("npm i nodemon --save-dev")
        os.system("cls")
        print("You did not added module yourself, so I added the following: \n✅ mongoose\n✅ cors\n✅ express\n✅ bcryptjs\n✅ cookie-parser\n✅ multer\n✅ jsonwebtoken\n✅ dotenv\n✅ nodemon")
    else:
        try:
            os.system(f"npm i --silent {package_new_inquire_b.rstrip()}")
            os.system("cls")
            print("✅ You installed the following packages: ", package_new_inquire_b)
        except:
            print("\nAn Error Occured. Make Sure You Entered A Valid Package name...")

    # ------------------ < server files > ------------------
    '''Setting up server components'''
    # ------------------ < server files > ------------------

    os.system("mkdir controllers && mkdir middlewares && mkdir models && mkdir routes && mkdir utils && mkdir config")
    os.system("echo. >  index.js && echo. > .env")
    
    with open('.env', 'w') as env:
        env.write("PORT=3000\nMONGO_DB_URI=\nJWT_SECRET=")

    with open('index.js', 'w') as serverindex:
        serverindex.write('import express from "express"\nimport dotenv from "dotenv"\ndotenv.config()\n\nconst app = express()\nconst PORT = process.env.PORT || 5000\n\napp.get("/", (req, res) => {\n\tres.send("Hello World!")\n});\n\napp.listen(PORT, () => {\n\tconsole.log(`Server is running on port ${PORT}.`)\n})\n')

    with open('package.json', 'r') as packagefile:
        data = json.load(packagefile)

    if 'test' in data['scripts']:
        del data['scripts']['test']

    data['type'] = "module"
    data['scripts']['start'] = "nodemon index.js"

    with open('package.json', 'w') as file:
        json.dump(data, file, indent=2)

    os.system("echo. > .gitignore")

    with open('.gitignore', 'w') as gitignorefile:
        gitignorefile.write("logs\n*.log\nnpm-debug.log*\n\nnode_modules\ndist\ndist-ssr\n*.local\n\n.env\n\n.vscode/*\n!.vscode/extensions.json\n")

    # ------------------ < git > ------------------
    '''Setting up git and exit'''
    # ------------------ < git > ------------------

    os.chdir("..\\")
    os.system("git init")
    os.system("echo. > .gitignore")

    with open('.gitignore', 'w') as gitignorefile:
        gitignorefile.write("logs\n*.log\nnpm-debug.log*\n\nnode_modules\ndist\ndist-ssr\n*.local\n\n.env\n\n.vscode/*\n!.vscode/extensions.json\n")

    os.system("cls")
    print("Setup Completed! MERN App template initialized successfully. 🗿")

if __name__ == "__main__":
    setup_mern_stack()