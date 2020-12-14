# telematics_project
 General Info _________

In this project we implemented a dns server. Our dns server consists of 3 parts :  Stub resolver ,  Recursive resolver and autorative dns server. The main purpose for this implementation is to send a domain name and receive an IP address assigned for this domain name. 

Technologies _________

1. Python3 (programming Language) 
2. Notebook Jupyter (For running the code)
3. Pandas Library (Creating the log file)
4. Json (For creating the zones )

Setup __________
1.Stub Resolver



![name-of-you-image](https://github.com/Alioio/telematics_project/blob/main/Notebooks/screenshots/stubresolver/1.png)


![name-of-you-image](https://github.com/Alioio/telematics_project/blob/main/Notebooks/screenshots/stubresolver/2.png)


![name-of-you-image](https://github.com/Alioio/telematics_project/blob/main/Notebooks/screenshots/stubresolver/3.png)


![name-of-you-image](https://github.com/Alioio/telematics_project/blob/main/Notebooks/screenshots/stubresolver/4start%20define.png)


![name-of-you-image](https://github.com/Alioio/telematics_project/blob/main/Notebooks/screenshots/stubresolver/defining%20stub%20resolver.png)

2.Recursive Resolver
3.DNS
Features _______
Status_________

![name-of-you-image](https://github.com/Alioio/telematics_project/blob/main/Notebooks/zones_telematik.png)
photo 1.Zones---- 
The process starts with the Dns Resolver which looks in the cache if the information that he seeks is in there, If not he then goes to ask root which reachable in this case with the IP address 127.0.0.11:53053 .If The root doesn't have the answer then he sends the Dns resolver to ask Telematik and FuBerlin (TLD).The process contiunes until the resolver gets an IP adress  If the TLD's don't have the answer the the recrusive resolver proceeds to ask Switch, Router, Homework ,Pcpools. If the resolver doesn't get answer he logs an error with the name rcode=3 which means the domain name doesn't have any information.

