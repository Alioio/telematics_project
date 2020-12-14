# telematics_project
 
 General Info _________

In this project we implemented a dns server. Our dns server consists of 3 parts :  Stub resolver ,  Recursive resolver and autorative dns server. The main purpose for this implementation is to send a domain name and receive an IP address assigned for this domain name. 

Technologies _________

1. Python3 (programming Language) 
2. Notebook Jupyter (For running the code)
3. Pandas Library (Creating the log file)
4. Json (For creating the zones )

Setup __________ Stub Resolver , Recursive Resolver , DNS.


1.Stub Resolver



![name-of-you-image](https://github.com/Alioio/telematics_project/blob/main/Notebooks/screenshots/stubresolver/1.png)
                            
Photo 1.1 Stubresolver

![name-of-you-image](https://github.com/Alioio/telematics_project/blob/main/Notebooks/screenshots/stubresolver/2.png)

Photo 1.2 Stubresolver

![name-of-you-image](https://github.com/Alioio/telematics_project/blob/main/Notebooks/screenshots/stubresolver/3.png)

Photo 1.3 Stubresolver

![name-of-you-image](https://github.com/Alioio/telematics_project/blob/main/Notebooks/screenshots/stubresolver/4start%20define.png)

Photo 1.4 Stubresolver

![name-of-you-image](https://github.com/Alioio/telematics_project/blob/main/Notebooks/screenshots/stubresolver/defining%20stub%20resolver.png)


Photo 1.5 Stubresolver

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

2.Recursive Resolver


![name-of-you-image](https://github.com/Alioio/telematics_project/blob/main/Notebooks/screenshots/recursiveresolver/11.PNG)

Photo 2.1 Recursive Resolver

![name-of-you-image](https://github.com/Alioio/telematics_project/blob/main/Notebooks/screenshots/recursiveresolver/12.PNG)

Photo 2.2 Recursive Resolver

![name-of-you-image](https://github.com/Alioio/telematics_project/blob/main/Notebooks/screenshots/recursiveresolver/13.PNG)

Photo 2.3 Recursive Resolver

![name-of-you-image](https://github.com/Alioio/telematics_project/blob/main/Notebooks/screenshots/recursiveresolver/14.PNG)

Photo 2.4 Recursive Resolver

![name-of-you-image](https://github.com/Alioio/telematics_project/blob/main/Notebooks/screenshots/recursiveresolver/15%20threading.png)

Photo 2.5 Recursive Resolver

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

3.DNS


https://github.com/Alioio/telematics_project/blob/main/Notebooks/screenshots/DNS/21.png

Photo 3.1 DNS

https://github.com/Alioio/telematics_project/blob/main/Notebooks/screenshots/DNS/22.png

Photo 3.2 DNS

https://github.com/Alioio/telematics_project/blob/main/Notebooks/screenshots/DNS/23.png

Photo 3.3 DNS

https://github.com/Alioio/telematics_project/blob/main/Notebooks/screenshots/DNS/24.png

Photo 3.4 DNS

https://github.com/Alioio/telematics_project/blob/main/Notebooks/screenshots/DNS/25.png

Photo 3.5 DNS

https://github.com/Alioio/telematics_project/blob/main/Notebooks/screenshots/DNS/26.png

Photo 3.6 DNS

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Zones _______ Explaining the zones


![name-of-you-image](https://github.com/Alioio/telematics_project/blob/main/Notebooks/zones_telematik.png)

Photo 4.1 Zones---- 
The process starts with the Dns Resolver which looks in the cache if the information that he seeks is in there, If not he then goes to ask root which reachable in this case with the IP address 127.0.0.11:53053 .If The root doesn't have the answer then he sends the Dns resolver to ask Telematik and FuBerlin (TLD).The process contiunes until the resolver gets an IP adress  If the TLD's don't have the answer the the recrusive resolver proceeds to ask Switch, Router, Homework ,Pcpools. If the resolver doesn't get answer he logs an error with the name rcode=3 which means the domain name doesn't have any information.
