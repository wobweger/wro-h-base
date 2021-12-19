### cvs

+ [home](http://www.nongnu.org/cvs/)
+ [quick](https://www.cs.umb.edu/~srevilak/cvs.html)
+ [branch](http://ximbiot.com/cvs/manual/feature/cvs_5.html#SEC60)

|action|command|comment|
|---    |---    |---    |
|env|setenv CVSROOT /path/to/repo/|C-shell|
|env|CVSROOT=/path/to/repo/;export CVSROOT |bash|
|pserver|cvs -d :pserver:usr@host/path/to/repo login|
|login|cvs  login|
|checkout|cvs checkout module|
|update|cvs update|
|   |cvs update -d|include new directories|
|   |cvs update -P|prunes empty directories|
|status|cvs status||
|commit|cvs commit FN|commit changes|
|add file|cvs add DN|directory |
|   |cvs add FN| source/text file|
|   |cvs add -kb FN|binary file|
|merge|cvs update -j 1.7 -j 1.10 FN| |