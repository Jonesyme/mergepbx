
# MergePBX - Jonesy's Fork

### **What is it?** 
A tool to help git properly merge and rebase Xcode generated PBX files (i.e ".pbxproj") 
### **Does it really work?** 
Yes, it really works.  You will never again have to manually resolve needless conflicts simply because more than one developer modified the PBX file
### **Why the fork?** 
The original repo hasn't been updated in 5 years and some newer Xcode features now break the original script
### **What's in the fork?**
* Added support for Swift Package Manager (ALL CREDIT for this feature goes to [Daniel Larsen|https://github.com/GrandLarseny] and his [mergepbx fork|https://github.com/GrandLarseny/mergepbx])
* Added ability to post a message to the console/stdout whenever git invokes MergePBX during an operation. There's two reasons I added this:
* 1) to confirm whether MergePBX is properly configured and being called in the first place
* 2) to inform the user which commit, branch, merge, etc. resulted in a PBX conflict 

### **Original Project Links**
* Original MergePBX Version: 0.6 - 2nd Oct 2014
* Original Author's Website (Simon Wagner): http://simonwagner.github.io/mergepbx/
* Buy Simon a cup of tea: [![Donate to mergepbx](https://www.paypalobjects.com/en_US/i/btn/btn_donate_SM.gif)](https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=UX3YTWH8DRYVN)

## Why mergepbx?

Umm, why sliced bread? 
Have you ever wasted hours of your day manually resolving merge conflicts in a "pbxproj" file?
If yes, then MergePBX will change your life.

.

# How to configure as a GIT driver

While MergePBX can be used standalone via the command line, we recommend using MergePBX as a merge driver for git.  To do so, follow these steps below:

## Compile python source into executable

Checkout repo and execute the following command inside the root directory of the project: (note: its a python script, I promise it does nothing nefarious which you're welcome to verify for yourself):

```
./build.py
```

Assuming all goes well, an executable file named: `mergepbx` will be generated in same directory. This executable is the actual MergePBX script that performs all the magic.  
Why didn't we just provide you with that file to begin with?  No idea. Ask Simon, he created this process...

## Configure git to use driver

Note: this will configure git to only use `mergepbx` when it encounters a conflict in a PBX file.  This will NOT alter the way git merges any other file types other than "pbxproj" files. 
It can be disabled at anytime by commenting out or removing the gitconfig lines below or commenting out and/or deleting the lines from the .gitattributes file in the final step below.

Open `~/.gitconfig` (create if it does not exist) and add the following lines:

```
# use the MergePBX algorithm only on pbxproj files
[merge "mergepbx"]
        name = Xcode project files merger
        driver = /Users/yourusername/path/to/mergepbx %O %A %B
```

Replace the path in the last line above with the correct path to the `mergepbx` executable file you generated using the `build.py` command above.

## Configure your repo to use the driver ##

In the root directory of any and all local git repos you wish to use MergePBX on, open the file `.gitattributes` (create if it does not exist) and add the following line:

```
*.pbxproj merge=mergepbx
```
This allows you to enable or disable MergePBX on a project by project basis.

.

# Testing whether MergePBX is working

If you merge/rebase any branches with git, git will automatically invoke mergepbx for all .pbxproj files. You don't have to do anything special, simply merge/rebase your branches as you did before. 
The results should speak for themselves....

**Note:** MergePBX can be quite slow.  It is not optimized for speed.  We leave that as an exercise for the reader.... 

.

# Disclaimer

**Use at your own risk**
This code published here and any programs that are created from it are not claimed to be fit for any purpose.
Running them might lead to your project being eliminated, kittens killed and the end of the world.
Be careful, you have been warned!

**Reality has limits** 
MergePBX can only add context to git's merge algorithm, it cannot resolve _genuine_ code conflicts.  For example: if you rename a file and your co-worker deletes that same file, the resulting merged file 
is not going to make logical sense even with MergePBX properly configured.    There's no magic wand for everthing...


## Contributers ##

* Simon Wagner
* Daniel Larson
* Mike Jones
