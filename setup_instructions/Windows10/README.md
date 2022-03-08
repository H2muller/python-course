# Setup instructions - Windows 10 / Windows 11

## **Overview**
This course will utilize Visual Studio Code to develop Python code. In this section, we will learn how to install and configure Visual Studio Code and its dependencies and plugins, as well as how to install and configure Python and the Python libraries.

**Since this course is intended for a UNIX environment, it will be necessary to setup a UNIX environment within Windows to run the course. This will be achieved using the Windows Subsystems for Linux (WSL, version 2) and an Ubuntu Linux instance. If you already have these installed, you can skip this section.**

If you don't have these configured, or if you are not sure, detailed instructions on how to properly set up the course environment are provided below.

---
## Table of Contents
<details>
 <summary> Click to expand </summary>

 [Prerequisites](#prerequisites)

 [Installing and configuring the Virtual Linux Environment](Installing-and-configuring-the-Virtual-Linux-Environment)
 - [Installing Windows Subsystem for Linux](Installing-Windows-Subsystem-for-Linux)
 - [Configuring a virtual Ubuntu environment](Configuring-a-virtual-Ubuntu-environment)

 [Installing Visual Studio Code](Installing-Visual-Studio-Code)
 - [Installing VS Code plugins](Installing-VS-Code-plugins)
   - [Required plugins](Required-plugins)
   - [Recommended plugins](Recommended-plugins)

 [Running VS Code from the WSL environment](Running-VS-Code-from-the-WSL-environment)


</details>

---
## **Prerequisites**
You must be running Windows 10 version 2004 and higher (Build 19041 and higher) or Windows 11

>To check your Windows version and build number, select **Windows logo key + R**, type **winver**, select **OK**. You can update to the latest Windows version by selecting **Start > Settings > Windows Update > Check for updates**.

## **Installing and configuring the Virtual Linux Environment**

### **Enabling required Windows features**
This course requires the utilization of WSL2. To enable WSL2, you must first enable the **Virtualization** feature on your operating system.

To enable the **Virtualization** feature, open the **control panel** by pressing **Windows logo key + R**, typi **control**, and hitting **Enter**.

Next, click on **Programs**, then **Programs and Features**, and finally **Turn Windows features on or off**.

Enable the following features (if they are not already enabled):
- **Hyper-V** (if this option is grayed out, you may need to enable it from the BIOS: the setting may be called *VT-x*, *AMD-V*, *SVM*, or *Vanderpool*. Enable **Intel VT-d** or **AMD IOMMU** if the options are available)

- **Virtual Machine Platform**

Save your changes and reboot.

### **Installing Windows Subsystem for Linux**
You can now install everything you need to run **Windows Subsystem for Linux (WSL)** by entering this command in Windows PowerShell or Windows Command Prompt **as an administrator**, and then restarting your machine.

```powershell
wsl --install
```

This command will enable the required optional components, download the latest Linux kernel, set WSL 2 as your default, and install a Linux distribution for you (Ubuntu by default).


### **Configuring a virtual Ubuntu environment**
The first time you launch a newly installed Linux distribution, a console window will open and you'll be asked to wait for files to de-compress and be stored on your machine. All future launches should take less than a second. You will then be required to create a username and password for your new Linux account. **These should not be the same as your Windows username and password**. Make sure you chose a password you will remember, as you will be asked to enter it every time you install or update any software in your Linux distribution.

You can verify that your Linux distribution is set up correctly by typing **lsb_release -a** in your Linux console, as shown below.
```bash
$ lsb_release -a
```
You should see the following output:
```bash
No LSB modules are available.
Distributor ID: Ubuntu
Description:    Ubuntu 20.04.4 LTS
Release:        20.04
Codename:       focal
```

To ensure that you have the latest version of the Ubuntu package libraries, you can update your system by entering the following command in your Linux console
```bash	
$ sudo apt update
```
You will be prompted to enter the password you set when you installed the Ubuntu distribution, then hit **Enter**. This should take a few minutes.

Once the update is complete, you may be notified that there are packages that can be upgraded. If that is the case, you can upgrade the packages by entering the following command in your Linux console:
```bash
$ sudo apt upgrade
```
You won't be asked to enter your password this time, because the session is stil validated. You will be asked if you would like to continue with the upgrade. Press **Y** to continue. This should take a bit longer than the previous stage.

Ubuntu 20.04 already comes with Python 3.8 installed, so you won't need to install it. You can verify that Python 3.8.2 is installed by typing **python3 --version** in your Linux console, as shown below.
```bash
$ python3 --version

Python 3.8.10
```


## Installing Visual Studio Code
Visual Studio Code is an open-source software provided by Microsoft. It is a powerful, cross-platform, and easy-to-use text editor with code completion, syntax highlighting, and debugging features.

More importantly, it provides access to a large number of plugins that allow you to develop and debug code in a variety of languages, and a fully functional terminal.

The software installer is available as a free download from [https://code.visualstudio.com/download](https://code.visualstudio.com/download).

Once you have downloaded the .exe file, you can install it by following the instructions from the Installation Wizard.

### Installing VS Code plugins

#### Required plugins
abc



#### Recommended plugins
abc


## Running VS Code from the WSL environment
abc