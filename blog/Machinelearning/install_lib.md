#Machine Learning(1)-Preparations

Today I started to learn a book named: The Practice of Machine Learning.
This book provides some cases on machine learning with lots of good libs. And I'll record what I've learned from this book since today. And this passage we'll do some preparations.
##1.Install OpenCv
As it listed on official website, you need to insatll some basic software pakages.
```sh
[compiler] sudo apt-get install build-essential
[required] sudo apt-get install cmake git libgtk2.0-dev pkg-config libavcodec-dev libavformat-dev libswscale-dev
[optional] sudo apt-get install python-dev python-numpy libtbb2 libtbb-dev libjpeg-dev libpng-dev libtiff-dev libjasper-dev libdc1394-22-dev
```
Then download pakages of opencd from [here](http://opencv.org/downloads.html)

Extract source code, and install that pacage.
```sh
cd ~/opencv
mkdir release
cd release
cmake -D CMAKE_BUILD_TYPE=RELEASE -D CMAKE_INSTALL_PREFIX=/usr/local ..
make
sudo make install
```
This way is provided on the official website, but It doesn't work on my Ubuntu 14.10, And I try a lot of methods which still doesn't work. If you occured the same problem as me, strongly recommend you to install opencv repo
```sh
sudo apt-get install libopencv-dev
```
Here  is another solution.
>Installing OpenCV from the Ubuntu repositories is a good choice for the most cases, but sometimes you need build OpenCV from sources yourself.
For example, if you need OpenCV's non-free functionality, or want to contribute to this project (you should use the latest version to create pull request), or want to change something (yes, OpenCV can also contain bugs).
Possible solution is building ffmpeg (it's rather simple) - I really don't understand why Debian/Ubuntu prefers libav without alternative.
For installing ffmpeg you should download its sources from official site or clone GIT repository (git://source.ffmpeg.org/ffmpeg.git), then enter source directory and run
```sh
    ./configure --enable-shared --disable-static
    make
    sudo make install
```
>you can also add other parameters to configure. You can build static libraries too, but OpenCV can't be built with static ffmpeg libraries (now I don't know why).
After this you can download OpenCV sources from OpenCV site or clone GitHub repository (OpenCV repository), create build folder and run from it the following:
```
    cmake PATH_TO_SOURCES -DCMAKE_BUILD_TYPE=Release
    make
    sudo make install
```
>Of course, PATH_TO_SOURCES must be actual path to your OpenCV sources.
After these steps you have working latest OpenCV build in your system.

##2. Install R
Installing R is very simple
```sh
sudo apt-get update
sudo apt-get install r-base
sudo apt-get install r-base-dev
```

##3. Install BeautifulSoup
BeautifulSoup is a very important Html/xml parser writen in python. We can handle some tasks on parsing webpages easily.
```sh
sudo apt-get install python-bs4
```
##4. Install mlpy
Before install mlpy, you need to install GSL from [here](http://ftp.club.cc.cmu.edu/pub/gnu/gsl/)
```sh
./configure
make
make install
```
Then download package from [here](http://sourceforge.net/projects/mlpy/files/)
extract and cd to that directory.

```sh
sudo python setup.py install
```
If your GSL is not installed at standard dir, you may use this command
```
python setup.py build_exe --include-dirs=/path/to/header --rpath=/path/to/lib
```
##5. Install Neurolab 
Neurolab is a very strong but simple lib implmented in python on NN, with basic NN. training algorithm and very flexible framework.
You should download from [here](http://code.google.com/p/neurolab/downloads/list) (in china, you may get it from [here](https://pypi.python.org/pypi/neurolab))
```sh
python setup.py install
```
##
