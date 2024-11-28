<H1>Python-Nmap-Scanner</H1>

<h2>Objective:</h2>
<br>This project was conducted to demostrate how to automate network mapping by intergrating <i>python-nmap</i> library, which is a Python wrapper for the popular Nmap tool commonly found in network engineering and cybersecurity environments. We will create the script in a Kali Linux virtual machine and scan a the vulnerable Metasploitable2 machine which will be in our network. 


<h4>Requirements:</h4>
</br>Oracle VM Virtual Box
</br>Kali Linux
</br>Metasploitable2
</br>python-namp 
</br>Visual Studio Code


<h2>Create virtual machine</h2>
</br> Even though this is out of the scope of the project and not our main focus point. I will provide links to installing and configuring the Oracle Vm Virtual Box, Kalli Linux machine, Visual Studio Code(on Kali Linux machine) and Metasploitable2 machine below:

</br>
</br>
</br>
</br>

<hr>

<h2>Subnetting</h2>
</br>We want to ensure that both our Kali Linux machine and our Metasploitable2 machine are on the same network. We after following the videos to set up the machines, go into the "Setting" of each individual virtual machine. Then you will need to navigate to the "Network" tab and change "Attached to" to a "NAT Network" and assign each machine to the same NAT network for connection purposes. 

</br>
</br>

</br>Using the default credentials (msfadmin:msfadmin) to log into the Metasploitable2 machine and use the command <i>ip a</i> to find the IP address for the vulnerable machine.
</br>We will now go into the Kali machine to check if the Metasploitable2 machine is on our same network by using the command <i>sudo netdiscover -r 10.0.2.0/24</i>

</br>
</br>

<h2>Create a directory for our src code</h2>
</br> Go into Visual Studio Code, here you will need create a folder and file to the python script where the code will run. We will write our code here. example path for code <i> /testcode/src/scanner.py </i>

</br>This section of the code 
</br>

</br>This section of the code
</br>

</br>This section of the code returns to the console responses based on the users input between 1-3. 
</br>


<h2>Test scanner</h2>
</br>We will now change to root privilege using the <i>sudo su</i> command. We will then navigate to the directory that our scanner.py code is found. In this "src" directory we will then use the command to run scanner using the <i>python3 scanner.py</i> command.

