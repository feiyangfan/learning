# Java Learning Notes

## Basic Ideas

### The Java programming language
* general-purpose, high-level
* In Java, all source code is first written in plain text files with **.java** extension. Those source files are then compiled into **.class** files by the **javac** compiler. A **.class** file does not contain code that is native to your processor; it instead contains bytecodes — the machine language of the Java Virtual Machine1 (Java VM). The java launcher tool then runs your application with an instance of the Java VM.
<img src="./images/java-images/basic-java-class-jvm.gif" alt="image from Oracle java tutorial website" width="500"/>
<p align="center">*Ilustration(image from Oracle)*</p>

* Because the Java VM is available on many different operating systems, the same .class files can be run in different OS'.

### The Java Platform
* A platform is the hardware or software environment in which a program runs, can be described as a combination of the operating system and underlying hardware
* Java platform **differs** from most other platforms in that it's a **software-only** platform that runs on top of other hardware-based platforms.
* The Java platform has two components:
	* The Java Virtual Machine
	* The Java Application Programming Interface (API) 
		* The API is a large collection of ready-made software components that provide many useful capabilities. It is grouped into libraries of related classes and interfaces; these libraries are known as **packages**.
* As a **platform-independent** environment, the Java platform is **slower than native code**.
	<img src="./images/java-images/java-platform.gif" alt="image from Oracle java tutorial website" width="300"/>
	<p align="center">*Ilustration(image from Oracle)*</p>



## Resources
* https://docs.oracle.com/javase/tutorial/
	* This is the first website I used to learn basic Java knowledges

# Credits