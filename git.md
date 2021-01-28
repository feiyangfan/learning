# Git notes

## Table of Contents
- [Git notes](#git-notes)
    + [Workflow](#workflow)
    + [HEAD](#head)
    + [Relative refs](#relative-refs)
    + [Move around in git](#move-around-in-git)
    + [Multiple parents: Specifying Parents](#multiple-parents--specifying-parents)
    + [Branch and checkout](#branch-and-checkout)
    + [Merge](#merge)
    + [Rebase](#rebase)
    + [Merge vs rebase](#merge-vs-rebase)
    + [Reversing Changes in git](#reversing-changes-in-git)
    + [Cherry-pick](#cherry-pick)
    + [Interactive rebase](#interactive-rebase)
    + [Locally stacked commits](#locally-stacked-commits)
    + [Juggling Commits](#juggling-commits)
    + [Git tags](#git-tags)
    + [Git Describe](#git-describe)
    + [Remote Repo](#remote-repo)
      - [Pros](#pros)
      - [Special property](#special-property)
      - [Commands](#commands)
        * [Git Clone \<remote url>](#git-clone---remote-url-)
        * [git fetch](#git-fetch)
        * [git fetch with arguments](#git-fetch-with-arguments)
        * [git pull](#git-pull)
        * [git pull with arguments](#git-pull-with-arguments)
        * [git push](#git-push)
        * [git push with arguments](#git-push-with-arguments)
      - [Use nothing as fetch/push source arguments](#use-nothing-as-fetch-push-source-arguments)
      - [Diverged Work](#diverged-work)
      - [stuck on rejected push](#stuck-on-rejected-push)
      - [Remote tracking](#remote-tracking)
    + [Misc](#misc)
    + [Resources](#resources)
- [Credit](#credit)

### Workflow
* git add -> git commit -> git push

### HEAD
1. HEAD is the symbolic name for the currently checked out commit -- it's essentially what commit you're working on top of
2. HEAD always points to the most recent commit which is reflected in the working tree. Most git commands which make changes to the working tree will start by changing HEAD.
3. Normally HEAD points to a branch name (like newFeature). When you commit, the status of newFeature is altered and this change is visible through HEAD.
4. We can use **git checkout** to move HEAD to another branch/commit

### Relative refs
1. \<branch/commit>**^**: ^ Moving upwards one commit at a time.
3. \<branch/commit>**~**\<nums>: Moving upwards a number of times.
4. Above command can be chained together
	* **git checkout HEAD~^2~2**
4. One of the most common ways to use relative refs is to move branches around. You can directly reassign a branch to a commit with the -f option. 
	*  **git branch -f \<branch to move> \<some place>**
	* Example: git branch -f main newFeature~4

### Move around in git
1. using **git branch -f \<branch to move> \<some place>**

### Multiple parents: Specifying Parents
Like the ~ modifier, the ^ modifier also accepts an optional number after it.

Rather than specifying the number of generations to go back (what ~ takes), the modifier on ^ specifies which parent reference to follow from a merge commit. Remember that merge commits have multiple parents, so the path to choose is ambiguous.

Git will normally follow the "first" parent upwards from a merge commit, but specifying a number with ^ changes this default behavior.

### Branch and checkout

1. Git branch: Because there is no storage / memory overhead with making many branches, it's easier to logically divide up your work than have big beefy branches. a branch essentially says "I want to include the work of this commit and all parent commits."
2. **git branch \<branch name>**: to create a new branch that is on this current commit
3. **git checkout \<new branch name>**: switch to this branch, any commit made after will be counted as this branch
4. **git switch \<branch name>**: new version of git checkout,
5. shortcut: **git checkout -b \<new branch name> \<at commit(optional)>**: create a new branch, and switch to it

### Merge

1. Merging in Git creates a special commit that has two unique parents. A commit with two parents essentially means "I want to include all the work from this parent over here and this one over here, and the set of all their parents."
2. **git merge \<another branch name>**: merge the current* branch with another branch


### Rebase

1. Rebasing essentially takes a set of commits, "copies" them, and plops them down somewhere else
2. These commits are the commits that differ from another branch
2. the advantage of rebasing is that it can be used to make a nice linear sequence of commits. The commit log / history of the repository will be a lot cleaner if only rebasing is allowed.
3. **git rebase \<another branch>**: rebase the current branch onto ‘another branch’.
4. **git rebaes \<current branch> \<another branch>**: rebase another branch onto current branch
 
### Merge vs rebase
* rebase
	* Pros:
	Rebasing makes your commit tree look very clean since everything is in a straight line
	* Cons:
Rebasing modifies the (apparent) history of the commit tree.
	* For example, commit C1 can be rebased past C3. It then appears that the work for C1' came after C3 when in reality it was completed beforehand.

### Reversing Changes in git
1. Using **git reset \<branch>^/~/-**
	* reverts changes by moving a branch reference backwards in time to an older commit
	* move a branch backwards as if the commit had never been made in the first place
	* **HOWEVER** doesn't work for remote branches that others are using
	

2. Using **git revert \<branch>^/~/-**
	* work for remote branches that others are using
	* reverse changes and share those reversed changes with others


### Cherry-pick
1. **git cherry-pick \<commit1> \<commit 2> ... \<commit n>**
2. commit order from left to right
3. great when you know which commits you want (and you know their corresponding hashes)
4. copy a series of commits below your current location (HEAD)

### Interactive rebase
1. **git rebase -i \<commit>~\<nums>**, using the **-i** flag
1. you don't know what commits you want
2. review a series of commits you're about to rebase
3. git will open up a UI to show you which commits are about to be copied below the target of the rebase. It also shows their commit hashes and messages, which is great for getting a bearing on what's what
4. There are many possible operations you can do with git rebase


### Locally stacked commits
1. Happens when you have some local commits that you do not want to be pushed to the main branch
2. We can use **git cherry-pick** or **git rebase -i**


### Juggling Commits
1. Want to make changes to a previous commit
2. Using **git rebase -i**:
	* We will re-order the commits so the one we want to change is on top with git rebase -i
	* We will git commit --amend to make the slight modification
	* Then we will re-order the commits back to how they were previously with git rebase -i
	* Finally, we will move main to this updated part of the tree to finish the level (via the method of your choosing)
3. The above method can introduce rebase conflicts
4. Using **git cherry-pick**
	* cherry pick the commit to fix
	* cherry pick the commits after the previous commit
	* done

### Git tags
1. **git tag \<tag name> \<commit>** to tag a specific commit
2. **git tag \<tag name>** to tag HEAD's commit
1. permanently mark historical points in your project's history. For things like major releases and big merges, mark these commits with something more permanent than a branch.
2. **git tags** never move as more commits are created. You can't "check out" a tag and then complete work on that tag -- tags exist as anchors in the commit tree that designate certain spots

### Git Describe
1. **git describe \<ref>**: \<ref> is anything git can resolve into a commit. If you don't specify a ref, git just uses where you're checked out right now (HEAD).
1. a command to describe where you are relative to the closest "anchor" (aka tag).
2. Git describe can help you get your bearings after you've moved many commits backwards or forwards in history; this can happen after you've completed a git bisect (a debugging search) or when sitting down at a coworkers computer who just got back from vacation.
3. Output: 
	* \<tag>_\<numCommits>\_g\<hash>
	* Where tag is the closest ancestor tag in history, numCommits is how many commits away that tag is, and \<hash> is the hash of the commit being described.

### Remote Repo
#### Pros
1. First and foremost, remotes serve as a great backup! Local git repositories have the ability to restore files to a previous state (as you know), but all that information is stored locally. By having copies of your git repository on other computers, you can lose all your local data and still pick up where you left off.

2. More importantly, remotes make coding social! Now that a copy of your project is hosted elsewhere, your friends can contribute to your project (or pull in your latest changes) very easily.

#### Special property
* Remote branches have the special property that when you check them out, you are put into detached HEAD mode. Git does this on purpose because you can't work on these branches directly; you have to work elsewhere and then share your work with the remote (after which your remote branches will be updated).
* **origin/main**: orgin refers to the remote, this is where the remote is at

#### Commands
##### Git Clone \<remote url>
* create local copies of remote repositories

##### git fetch
* fetch data from a remote repository
* performs two main steps, and two main steps only. It:
	* downloads the commits that the remote has but are missing from our local repository, and...
	* updates where our remote branches point (for instance, origin/main, origin/feature)
* essentially brings our local representation of the remote repository into synchronization with what the actual remote repository looks like (right now)
* Using internet
* **HOWEVER**, does not change anything about your local state. It will not update your main branch or change anything about how your file system looks right now.
* Like a **DOWNLOAD** step

##### git fetch with arguments
* **git fetch origin foo**
	* Git will go to the foo branch on the remote, grab all the commits that aren't present locally, and then plop them down onto the o/foo branch locally.
* *git fetch origin \<source>:\<destination>*
* \<source> is now a place on the remote and \<destination> is a local place to put those commits

##### git pull
* fetching remote changes and then merging it with the current branch
	* git fetch -> git merge ~= git pull
* after git pull, 

##### git pull with arguments
* just git fetch origin \<source>:\<destination> with git merge called after it.
* git pull origin foo = git fetch origin foo + git merge o/foo
* git pull origin \<source>:\<destination>

##### git push
* **git push \<remote(optional)> \<place(optional)>**
* upload shared work
* the behavior of git push with no arguments varies depending on one of git's settings called push.default.
* if not given optional arguments, push will fail if HEAD not currently on a remote tracking branch 

##### git push with arguments

* *git push origin main*
	* translates to this in English:
	* Go to the branch named "main" in my repository, grab all the commits, and then go to the branch "main" on the remote named "origin". Place whatever commits are missing on that branch and then tell me when you're done.
	* This way, it **does not** need to know where we are checked out currently
* colon refspec
	* Refspec is just a fancy name for a location that git can figure out (like the branch foo or even just HEAD~1)
	* **git push origin \<source>:\<destination>**
	* \<source> is a place on the local and \<destination> is a remote place to push these commits
	* if destination does not exist, git will create it for you

#### Use nothing as fetch/push source arguments
* **git push origin :foo** deletes the foo branch both locally and remotely
* **git fetch origin :foo** create a foo branch locally



#### Diverged Work
* Imagine you clone a repository on Monday and start dabbling on a side feature. By Friday you are ready to publish your feature -- but oh no! Your coworkers have written a bunch of code during the week that's made your feature out of date (and obsolete). They've also published these commits to the shared remote repository, so now your work is based on an old version of the project that's no longer relevant
* Two ways to fix this problem
	* **rebase**
		* **git pull --rebase**
	* **merge**
		* **git pull**

#### stuck on rejected push
* Imagin your push is rejected because pushing to main is not permitted and you need to do a pull request, now you are stuck on main.
	* create a new branch called feature
	* git reset main back to the previous origin/main commit
	* git push origin feature	

#### Remote tracking
* Connection between **main** and **origin/main** is explained simply by the "remote tracking" property of branches. The **main** branch is set to track **origin/main** -- this means there is an implied merge target and implied push destination for the **main** branch.
* when you clone a repository with git, this property is actually set for you automatically.

* During a clone, git creates a remote branch for every branch on the remote (aka branches like o/main). It then creates a local branch that tracks the currently active branch on the remote, which is main in most cases.
* Once git clone is complete, you only have one local branch (so you aren't overwhelmed) but you can see all the different branches on the remote (if you happen to be very curious). It's the best of both worlds!

* This also explains why you may see the following command output when cloning:
	``` local branch "main" set to track remote branch "origin/main" ```
	
* Creating own tracking branch
	* Method 1: **git checkout -b totallyNotMain origin/main**
	* Method 2: **git branch -u o/main totallyNotMain**

### Misc
* .gitignore: used to add stuff that should be ignored by git
* .gitconfig: config git at this current repo or globally
* commit a small chunk of codes at a time so its easier to understand what was worked on and easy to go back to a previous commit if something goes wrong.
* branch early, and branch often
* PULL REQUEST: request origin/autorized-place to pull my codes to review and possibly merge them
	* When submitting pulling requests, whenever possible, make sure to split codes and only submit a small chunk at a time (couple hundreds maxmium) instead of thousands of lines of code, because it is easier for reviewer to review and easy for myself to keep track of what have been submitted.

### Resources
* https://learngitbranching.js.org/ 
	* The website I used to learn git interactively. The reason why I recommand this website is that it offers interactive ways of learning git:
		* It has graphs showing how commands work
		* It has a good flow of learning, starts from the basic than dig deeply into git.
* https://youtu.be/WBg9mlpzEYU
	* A youtube video from Scott Hanselman talking about some insight of git related knowledge

# Credit
* Some of the examples and conclusions come from https://learngitbranching.js.org/, which is a great website worth checking out if people wants to learn git
