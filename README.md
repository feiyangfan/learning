## Learning

### General: 
* **Consistency**: make sure when developing, keep everything clean, easy to navigate. Also, easy to understand for later reviews  

### Git related:

* **GENERAL:** 

  * commit small chunks of codes at a time so its easier to read what were doen and what was worked on.
  
* **PULL REQUEST:** request origin/autorized-place to pull my codes to review and possibly merge them

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
    * **My understanding**: create branches when doing new works that might affect main branch or want to work seperately when working with a team
  * **git merge "branch name"**: merge with other branch/changes, accpet/reject changes then use **git add** to add merged files
  * **git remote add "remote/origin" "name"**
  * **git push "remote" "branch":** publish local changes to the central repository

* **OTHERS:**
  * How to upload local repo to remote:
    * **git init** at local repo
    * **git add .** to add all local repo files  
    * **git commit -m**  
  	 * **git remote add "remote name" "url"**  
    * **git push -u "remote name" "remote branch"**  
  		
  * workflow: **modify things** -> **git add "file"** -> **git commit -m** 
  * **.gitconfig** can be used to config repo-specific config
  * **.gitignore** to add files that should be ignored from tracking

### npm related:
**npm install** to install mising dependencies in package.json.  
**npm run "script"** to run script in package.json.  
**npm build** a script that is used to build that we can test out/release

### web development related:
1. Code split: split codes to several files, and only send js that required to display on current screen to users. Use state management. [Link](https://youtu.be/bb6RCrDaxhw)
2. Some general notes: see [my-website readme](https://github.com/feiyangfan/my-website)
3. Frontend: see [my-website frontend readme](https://github.com/feiyangfan/my-website/tree/master/frontend)
4. Backend: see [my-website backend readme](https://github.com/feiyangfan/my-website/tree/master/backend)
5. Database: see [my-website database readme](https://github.com/feiyangfan/my-website/tree/master/database)

### Useful resources:
Git-related:  
[Some youtube videos from Scott Hanselman](https://youtu.be/WBg9mlpzEYU)  
[.gitignore documentation](https://git-scm.com/docs/gitignore)  

Other:  
[Spring boot official documentation](https://spring.io/projects/spring-boot)


## Learning goals:

#### web development
* basic html/css/javascript
* **Frontend**: react
* **Backend**: 
	* **javascript**: node.js and express, 
	* **java**: spring boot
* how to connect frontend to backend
* database(mongoDB or MySQL) and how to connect to it

#### mobile development
* ios: swift


  

