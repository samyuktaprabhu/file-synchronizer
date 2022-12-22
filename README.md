# file-synchronizer

<a name="readme-top"></a>
<h3 align="center" name="readme-top">File Synchronizer</h3>

  <p align="center">
    A Python script to synchronize two folders one-way. 
    <br />
    <a href=""></a>
    <br />
    <br />
    <a href=""></a>
    ·
    <a href=""></a>
    ·
</div>

<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>

## About The Project

This file synchronizer periodically maintains an identical copy of a source folder in a destination folder (replica). 
Any file or folder changes with operations like creation, deletion, modification (eg: rename, content change) are handled by this script.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Built With

* Python

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Getting Started


To get a local copy up and running, follow the steps mentioned below.
(These steps are for MacOS)

### Prerequisites

* VSCode / Terminal
* Git Repo
  ### Installation

1. Clone the repo to your local destination on computer
   ```sh
   git clone https://github.com/samyuktaprabhu/file-synchronizer.git
   ```
2. Create a new Output file (eg. 'output.txt') 
3. In the same root folder, create 2 folders - source and replica. Note down its path.
4. Open Terminal
5. Navigate to the root folder of the cloned project
6. In the terminal, run the command in this format- 
 ```sh
 python3 synctask.py <your_source_file_path> <your_replica_file_path> <your_sync_interval> <your_log_file_path>
   ```
7. Perform any of the operations mentioned in the description aboce to see the synchronization between the files / folders. 
<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- USAGE EXAMPLES -->
## Usage

Python has been used to write this script.

_For information, please refer to the [Documentation](https://docs.python.org/3/)_

Following libraries have been used in the script.
_For information on 'os', please refer to the [Documentation](https://docs.python.org/3/library/os.html)_
_For information on 'shutil', please refer to the [Documentation](https://docs.python.org/3/library/shutil.html)_
_For information on 'threading', please refer to the [Documentation](https://docs.python.org/3/library/threading.html)_
_For information on 'sys', please refer to the [Documentation](https://docs.python.org/3/library/sys.html)_
_For information on 'datetime', please refer to the [Documentation](https://docs.python.org/3/library/datetime.html)_

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- CONTACT -->
## Contact

Email - samyuktaprabhu@gmail.com


<p align="right">(<a href="#readme-top">back to top</a>)</p>