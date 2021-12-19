### git 
+ [about](https://git-scm.com/about)
+ [branch nutshell][gitBranch]

#### vscode clone

step by step guide to clone a CSC repository using vscode using SSH
as transport layer.

| step  | comment                      |
| ----: | ----                         |
|  | ![prereq](./e_scr/git_20200406_clone00.png) |
|  | place ssh keys, private and public into your user home folder |
|  | `.ssh` is required |
|  | ![prereq](./e_scr/git_20200406_clone01.png) |
|  | verify user name and email |
|  | test connection `ssh -T git@code.siemens.com` |
|  | a personal greeting should come back |
|  | ![prereq](./e_scr/git_20200406_clone02.png) |
|  | navigate online to you repository |
|  | copy clone with SSH string|
|  | ![prereq](./e_scr/git_20200406_clone03.png) |
|  | start vscode |
|  | open command palette |
|  | ![prereq](./e_scr/git_20200406_clone04.png) |
|  | pick `Git Clone` command|
|  | ![prereq](./e_scr/git_20200406_clone05.png) |
|  | paste clone with SSH string in|
|  | press `Enter` |
|  | ![prereq](./e_scr/git_20200406_clone06.png) |
|  | pick a folder to clone your repo in|
|  | ![prereq](./e_scr/git_20200406_clone07.png) |
|  | cloning in progress |
|  | ![prereq](./e_scr/git_20200406_clone08.png) |
|  | cloning done, wanna open repo now? |
|  | ![prereq](./e_scr/git_20200406_clone09.png) |
|  | note status bar color change |
|  | always be aware of active branch , bottom left , here master|
|  | ![prereq](./e_scr/git_20200406_clone10.png) |
|  | click on master to change branch |
|  | prefix `origin/` point to remote repo branch |

#### vscode branch

| step  | comment              |
| ----: | ----                 |
|  | ![git-bash branch](./e_scr/git_branch_20190925_061945.png)
|  | look line above current input right inside parentheses |
|  | ![vscode branch](./e_scr/git_branch_20190925_062031.png)
|  | look bottom left to identify active branch |
|  | ![vscode branch](./e_scr/git_merge_20190927_083944.png)
|  | verify merge request before commit |
|  | ![vscode branch](./e_scr/vscode_branch_20190925_062117.png)
| 1| active branch |
| 2| change branch |
|  | ![vscode branch](./e_scr/vscode_launch_20190925_062619.png)
|  | git=bash branch |
|  | ![vscode branch](./e_scr/vscode_push_20190925_062936.png)
| 1| navigate to changes |
| 2| stage changes |
|  | ![vscode branch](./e_scr/vscode_push_20190925_063035.png)
| 1| navigate to SCM via menu |
|  | ![vscode branch](./e_scr/vscode_push_20190925_063317.png)
| 1| stage changes |
| 2| staged changes |
| 3| provide commit message, shows up in repo |
|  | ![vscode branch](./e_scr/vscode_push_20190925_063539.png)
| 1| finalize staging by pressing `<Ctrl>+<Enter>` |
| 2| push staged changes into remote repo |
| :bulb: | can happen at a later time |
|  | ![vscode branch](./e_scr/vscode_push_20190925_063745.png)
|  | using ssh as transport layer, key phrase is required  |
|  | ![vscode branch](./e_scr/vscode_push_20190925_063807.png)
|  | working for a time|
|  | ![vscode branch](./e_scr/vscode_push_20190925_063947.png)
|  | check remote repo |
|  | ![vscode branch](./e_scr/vscode_push_20190925_064012.png)
|  | see your commit is visible in remote repo |

#### vscode check out

| step  | comment                      |
| ----: | ----                         |
|  | ![CMT ](./e_scr/msvsc_branch_20181217_00.png)
|  | open command palette by pressing `<Ctrl>+<Shift>+P`
| 1| enter *git*
| 2| select *Git checkout to ..*
|  | ![CMT ](./e_scr/msvsc_branch_20181217_01.png)
|  | select branch
|  | ![CMT ](./e_scr/msvsc_branch_20181217_02.png)
|  | see even git shell has changed upstream branch :+1:

### git lfs

storing large binary files in your repository
will slow down performance considerable.
use git lfs extension to circumvent this problem.
it is very simple and transparent to use.

navigate to [git lfs](https://git-lfs.github.com/)
download and install, [mirgrate](./git_lfs_mirgate.md)

on linux it's even more simple

```shell
sudo dnf install git-lfs
```

inside your repo, you need to add extension, which
are to be tracked by lfs.

```shell
git lfs install
git lfs track "*.png"
git lfs track "*.jpg"
git lfs track "*.jpeg"
git lfs track "*.tiff"
git lfs track "*.pdf"
git lfs track "*.7z"
git lfs track "*.tar"
git lfs track "*.gz"
git lfs track "*.xls"
git lfs track "*.xlsm"
git lfs track "*.xlsx"
git lfs track "*.doc"
git lfs track "*.docx"
git lfs track "*.vsd"
git lfs track "*.vsdx"
git lfs track "*.vss"
git lfs track "*.vssx"
git lfs track "*.ppt"
git lfs track "*.pptx"
git lfs track "*.ipynb"
git lfs track "largefiles/*.xml"
git lfs track "largefiles/*.csv"
```

in case you cloned repository before having git lfs installed, files tracked by lfs will not be present
in your repo, only a link will be there.
just enter 2 commands to fix it.

```shell
git lfs fetch
git lfs checkout
```


#### vscode branch
| step  | comment                                                       
| ----: | ----                                                          
|		| ![CMT ](./e_scr/msvsc_branch_20181217_00.png)
|		| open command palette by pressing `<Ctrl>+<Shift>+P`
|1      | enter *git*
|2      | select *Git checkout to ..*
|		| ![CMT ](./e_scr/msvsc_branch_20181217_01.png)
|		| select branch
|		| ![CMT ](./e_scr/msvsc_branch_20181217_02.png)
|		| see even git shell has changed upstream branch :+1:

[gitBranch]: https://git-scm.com/book/en/v2/Git-Branching-Branches-in-a-Nutshell


#### config

get configuration data

| step  | comment                      |
| ----: | ----                         |
| version      |`git --version` |
| get user name |`git config --global user.name`
| get email      |`git config --global user.email`

set configuration data

| step  | comment                      |
| ----: | ----                         |
| user name      |`git config --global user.name "<your name>"`|
| email      |`git config --global user.email "<your email>"` |

#### ssh

| step  | comment                      |
| ----: | ----                         |
|chk fn |`type %userprofile%\.ssh\id_rsa.pub`|
| gen   | `ssh-keygen -t rsa -C "<your email>" -b 4096`|
|test   |`ssh -T git@gitlab.com`|

[gitBranch]: https://git-scm.com/book/en/v2/Git-Branching-Branches-in-a-Nutshell

enter password phrase just once at git-bash launch,
edit line :arrow_down: to `~/.bashrc`

```bash
SSH_ENV=$HOME/.ssh/environment

# start the ssh-agent
function start_agent {
    echo "Initializing new SSH agent..."
    # spawn ssh-agent
    /usr/bin/ssh-agent | sed 's/^echo/#echo/' > ${SSH_ENV}
    echo succeeded
    chmod 600 ${SSH_ENV}
    . ${SSH_ENV} > /dev/null
    /usr/bin/ssh-add
}

if [ -f "${SSH_ENV}" ]; then
     . ${SSH_ENV} > /dev/null
     ps -ef | grep ${SSH_AGENT_PID} | grep ssh-agent$ > /dev/null || {
        start_agent;
    }
else
    start_agent;
fi
```

