## learning

### Git related:

* **GENERAL:** 

  * workflow: **modify things** -> **git add "file"** -> **git commit -m** 
  * commit often since I can always go back to a previous change

* **COMMAND:**

  * **head points to current branch**
  * **git clone "url"** to clone a repo from remote to local
  * **git revert "a commit hash"** to revert this commit

  * **git log** to find who did which commit, then use **git checkout "hash"** to go back to that commit

  * **git restore** to restore deleted but not commited files

  * create new branch and work on different branches:
    * **git branch** to check branches
    * **git checkout -b "branch name"** to create a new branch
    * **git checkout "branch name"** to change to another branch
    * my understanding: create branches when doing new works that might affect main branch or want to work seperately when working with a team
  
  * **git merge "branch name"**: merge with other branch/changes, accpet/reject changes then use **git add*
  
  * **git remote add "remote/origin" "name"**
  
  * **git push "remote" "branch":** publish local changes to the central repository
  
* **PULL REQUEST:** request origin/autorized-place to pull my codes to review and possibly merge them

* **OTHERS:** 

  * **.gitconfig** can be used to config repo-specific config

  * **.gitignore** to add files that should be ignored from tracking

### npm related:

**npm install** to install mising dependencies in package.json

**npm run "script"** to run script in package.json
  
### resources:

## Ideas and learning goals:

#### QoL:
* todolist app
* timetable app
* reminder app
* go train schedule and estimate how long user will take to get to the train station from current position
* break reminder
* <s>an app where i record stuff i learned everyday(to force me to be productive)?</s>
 * It so painful to upload my desgin images to github and use them in development log, maybe develop an app that make this less painful?
* combine all features into one app
* use github.io to deploy website?

#### Dev:
* find how to securely use API key in backend
* Express framwork with node.js?

#### learning goal:
* website
* cross-platform app
* flask?
* learn npm
* learn react
  

