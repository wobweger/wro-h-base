### migrate existing repos

```shell
git clone --mirror git@gitlab.com:grp/repo.git
cd repo.git
git lfs migrate import --everything --include "*.png"
git lfs migrate import --everything --include "*.pdf"
git lfs migrate import --everything --include "*.zip"
git lfs migrate import --everything --include "*.7z"
git lfs migrate import --everything --include "*.tar"
git lfs migrate import --everything --include "*.gz"
git lfs migrate import --everything --include "*.exe"
git lfs migrate import --everything --include "*.ppt"
git lfs migrate import --everything --include "*.pptx"
git lfs migrate import --everything --include "*.vsd"
git lfs migrate import --everything --include "*.vsdx"
git lfs migrate import --everything --include "*.doc"
git lfs migrate import --everything --include "*.docx"
git lfs migrate import --everything --include "*.xlsm"
git lfs migrate import --everything --include "*.xlsx"
git lfs migrate import --everything --include "*.xls"
git lfs migrate import --everything --include "*.vss"
git lfs migrate import --everything --include "*.vssx"
git lfs migrate import --everything --include "largefiles/*.xml"
git lfs migrate import --everything --include "largefiles/*.csv"
git reflog expire --expire-unreachable=now --all
git gc --prune=now
git push --force
```

+ [git lfs tutorial](https://github.com/git-lfs/git-lfs/wiki/Tutorial#migrating-existing-repository-data-to-lfs)
