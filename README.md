# WOS
This is official Wissam OS, It works for Windows, Linux, and Mac.

The default password is wissamiscool22


## Table of Contents
- [Install](#how-to-install)







## How to Install
- First, click download on the Github page.
- Next, go to [python.org](python.org) and install the most [recent version](python.org/downloads).

![PythonRecent](https://user-images.githubusercontent.com/75694885/175171518-9f4205f1-2e34-4296-ac94-743cb2eb5069.png)

- Once you install python, go to your terminal/console.
- Inside the terminal/console, type pip help.
- If an error shows up, contact me.
- If it shows a bunch of options, you are good to go.
- The last thing you need to do is type in your terminal/console:
  ```
  1. pip install tkinter
  2. pip install tqdm
  3. pip install cryptography
  ```
 
 Everything below does not talk about changing the code.
 
 
## How to Login
- You will be greeted with a prompt asking for your IP_ADDRESS.
- In order to find your IP_ADDRESS, open up your terminal/console, and type `ipconfig`.
- The number next to "IPv4" is what you want.
- In the program, enter your IPv4 address, and type in your desired port
  - The default is 9999
- Congrats! You have logged into Wissam OS!

## Two Options
Once you login, you will beee greeted with the ASCII logo, and two options. This part of the README.MD file will help you navigate.
![image](https://user-images.githubusercontent.com/75694885/175171343-2cef94f5-2653-4e66-b2ad-dadfffdcfc4d.png)

### How to open "files."
There are two ways to open "files."
- Type "1"
- Type "files" capitalized or lower case

### How to open "applications."
There are three ways to open "applications."
- Type "1"
- Type "apps" capitalized or lower case
- Type "applications" capitalied or lower case.

## Files Menu
When you open files, it will show a tree of all the files in that directory (I am planning on making a seperate folder for personal files). Anyway, you will see three options:
1. Press "1" to open a file.
2. Press '2' to edit or create a file.
3. Press '3' to exit.

Each option is pretty self explanatory. Once you click an option, you will have to type the name of the file. If the file is in a seperate folder, type the name of the folder, slash, the name of thefile.

An example:
folder/file.filetype

![image](https://user-images.githubusercontent.com/75694885/175176483-b87d1ffa-9671-42a5-a2c3-237467add44b.png)


## Application Menu
When you open the application menu, it will show three options:
1. fileSendServer
2. fileSendClient
3. CPP (File Encryption)

### CPP (File Encryption)
Once you type "CPP" or "cpp" on the application menu, it will open a seperate GUI.

![image](https://user-images.githubusercontent.com/75694885/175177737-4ba8a5d0-7b75-4115-be34-7dc6c4aaedaf.png)

When you select option one (encrypt file), it will ask for the file you wish to encrypt. Like the file menu, you have to type the name of they file. If it is in a another folder, you have to type the name of the folder.

NOTE: THIS WILL NOT WORK UNLESS THE FILE IS IN THE WOS DIRECTORY OR ABOVE!

The second option is to decrypt a file, it works the same way as encryption, but it does the oposite. Option three deletes a file, like all the other options, you have to type the name of the file.

Type "4" to exit. It will exit the program, I am working on a solution.

Now, it is time for what you have been waiting for...

# The Cloud
This section talks about the cloud, how to access it, how to use it, and how it works.

NOTE: IN ORDER TO USE THE CLOUD, YOU MUST TYPE IN YOUR CORRECT IPv4 ADDRESS. TO LEARN HOW, GO TO "HOW TO LOG IN."

## How to Access the SCloud
In order to access the SCloud, you must log in with your correct IPv4 address. Once you have logged in:
1. Go to the applications menu.
2. Type "fileSendClient" (I am going to change the name).
3. Type in your IPv4 address and PORT (default 9999).
4. Once you have opend the SCloud client, type "tree."
5. If a list of file names is printed, you are connected!

### Picture Steps:
![image](https://user-images.githubusercontent.com/75694885/175179766-5c454da2-79d4-4b00-870f-4acaad206f05.png)

![image](https://user-images.githubusercontent.com/75694885/175179816-be571c7a-d109-4060-abb0-f7dc0885c2a6.png)

![image](https://user-images.githubusercontent.com/75694885/175179881-13fd26dd-7d66-40b4-9bdb-df157353de1c.png)

![image](https://user-images.githubusercontent.com/75694885/175179958-2b9b2c42-d061-4207-a1ce-02089e129c89.png)

![image](https://user-images.githubusercontent.com/75694885/175180083-15c6b3b1-b95f-463e-bf63-fae9468ee3e9.png)

![image](https://user-images.githubusercontent.com/75694885/175180148-10fe9e8d-7e60-4c14-a36e-3878436b7913.png)

![image](https://user-images.githubusercontent.com/75694885/175180183-cbe0808b-29bb-4ca4-abab-ba839fac6aba.png)

In the last image when I typed "tree," the reason why nothing showed up was because I did not activate the server.
Also, I accidentally typed "ls."

## How to Use the SCloud
There are a few commands that can be run.
```
upload
download
cmd
tree
```

### Upload
When you type "upload," a window will pop up. Select the file of your choice, and press open. Once the file uploads, it will be in the cloud, and it will show a message.

### Download
When you type download, you also have to type the file name after.

Example download example.txt

This is how you can download files from the cloud

### CMD
When you type cmd, it will run a terminal/console command.

You also have to type the command after you type "cmd."

Example: cmd echo hi

You need to know basic terminal/console commands to be able to use this.

### Tree
This command lists all the files in the cloud. I am working on making it look better (it currently looks ugly).
This command lets you know if you are connected to the SCloud. If nothing shows up after you type the command, you are not connected.

## How SCloud works
SCloud works by using the Python library, socket. It is pretty simple. I have a server at home with code that allows clients to connect to it.

Socket allows the client and server to be able to transfer files, and commands.

The server has about 100 GB of storage.

# fileSendServer
You may have noticed an option in the apps menu labeled fileSendServer. This is because you can have your own personal server. Once you run the file, you have already set up your own cloud for personal use. There are no prompts.

## Personal Use
What do I mean by personal use? Maybe you want somebody to send you a large file. Most services do not allow people to share large files (Gmail, Discord, SMS, MMS, RCS, iMessage). Some might say, why not make a Shared Google Drive, or OneDrive? The reason is simple. In order to make a Shared Google Drive, you need to spend money; and OneDrive only offers 6GB. I don't want to spend money to share files when I could do it for free! This project is benificial and fun.

Wait? How could this project be free if I have 100GB? Wouldn't that cost money? Yes, but no. What I mean is, I had this storage lying around, and I was not the one who payed for it (my parents did 😂).

# Closing Remarks
I am going to add more to this project. If you read to the end, text me, "I read to the end 🧀" I will give you a surprise.
