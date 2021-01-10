import os
import datetime


# Git directory's name
MY_GIT_REPO_NAME = "MyPainter"

# .txt directory's name (in git directory)
MY_GIT_COMMIT_DIR_NAME = "Rubbish"

# Commit message
MY_GIT_COMMIT_MESSAGE = "Update Text Files"

# Whether commit into future days in this Week
FURNISH_INTO_THE_FUTURE = False

# Size of the Git Wall
ROWS_MAGIC_NUMBER = 7
COLOUMS_MAGIC_NUMBER = 53

# Expected Git Wall
MyExpectedWall = [
[ 1, 1,10, 1,10, 1, 1, 1,10, 1,10,10,10,10, 1,10, 1, 1, 1,10, 1,10,10, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,10],
[ 1,10, 1, 1, 1,10, 1,10, 1, 1,10, 1, 1, 1, 1,10,10, 1, 1,10, 1,10, 1,10, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,10],
[10, 1, 1, 1, 1,10, 1,10, 1, 1,10, 1, 1, 1, 1,10, 1,10, 1,10, 1,10, 1,10, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,10],
[10, 1, 1, 1, 1, 1,10, 1, 1, 1,10,10,10,10, 1,10, 1,10, 1,10, 1,10,10, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,10],
[10, 1, 1, 1, 1,10, 1,10, 1, 1,10, 1, 1, 1, 1,10, 1,10, 1,10, 1,10, 1,10, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,10],
[ 1,10, 1, 1, 1,10, 1,10, 1, 1,10, 1, 1, 1, 1,10, 1, 1,10,10, 1,10, 1,10, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,10],
[ 1, 1,10, 1,10, 1, 1, 1,10, 1,10, 1, 1, 1, 1,10, 1, 1, 1,10, 1,10,10, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,10],
]


def gitInit(name, dirName):
    os.mkdir(name)
    os.chdir(name)
    os.system("git init")
    os.mkdir(dirName)
    os.chdir(dirName)


def gitCommit(name, message, dateFormat, date):
    with open(f"{name}.txt", "w") as commitFile:
        print("This File is MEANINGLESS", file=commitFile)
    os.system("git add .")
    os.system(f'git commit -m "{message}" --date=format:{dateFormat}:{date}')


if __name__ == '__main__':
    gitInit(MY_GIT_REPO_NAME, MY_GIT_COMMIT_DIR_NAME)
    # 1 → Sunday, 2 → Monday, etc.
    dayOfWeek = (datetime.datetime.now().isoweekday() % 7) + 1
    fileCounter = 0
    # Past Weeks
    for i in range(0, COLOUMS_MAGIC_NUMBER-1):
        for j in range(0, ROWS_MAGIC_NUMBER):
            commitTimes = MyExpectedWall[j][i]
            myDelta = ((COLOUMS_MAGIC_NUMBER - 1 - i) *
                       ROWS_MAGIC_NUMBER) - j + dayOfWeek - 1
            thisDay = datetime.date.today() - datetime.timedelta(days=myDelta)
            for k in range(0, commitTimes):
                gitCommit(str(fileCounter), MY_GIT_COMMIT_MESSAGE,
                          "short", str(thisDay))
                fileCounter += 1
    # This Week
    for i in range(0, dayOfWeek):
        commitTimes = MyExpectedWall[i][COLOUMS_MAGIC_NUMBER-1]
        myDelta = dayOfWeek - i - 1
        thisDay = datetime.date.today() - datetime.timedelta(days=myDelta)
        for k in range(0, commitTimes):
            gitCommit(str(fileCounter), MY_GIT_COMMIT_MESSAGE,
                      "short", str(thisDay))
            fileCounter += 1

    if FURNISH_INTO_THE_FUTURE:
        for i in range(dayOfWeek, ROWS_MAGIC_NUMBER):
            commitTimes = MyExpectedWall[i][COLOUMS_MAGIC_NUMBER-1]
            myDelta = ROWS_MAGIC_NUMBER - i
            thisDay = datetime.date.today() + datetime.timedelta(days=myDelta)
            for k in range(0, commitTimes):
                gitCommit(str(fileCounter), MY_GIT_COMMIT_MESSAGE,
                          "short", str(thisDay))
                fileCounter += 1
