# telematics_project
 
 General Info _________

In this project we implemented a dns server. Our dns server consists of 3 parts :  Stub resolver ,  Recursive resolver and autorative dns server. The main purpose for this implementation is to send a domain name and receive an IP address assigned for this domain name. 

Technologies _________

1. Python3 (programming Language) 
2. Notebook Jupyter (For running the code)
3. Pandas Library (Creating the log file)
4. Json (For creating the zones )

Setup __________ Stub Resolver , Recursive Resolver , DNS.

Zones _______ Explaining the zones


![name-of-you-image](https://github.com/Alioio/telematics_project/blob/main/Notebooks/zones_telematik.png)

Photo 4.1 Zones---- 
The process starts with the Dns Resolver which looks in the cache if the information that he seeks is in there, If not he then goes to ask root which reachable in this case with the IP address 127.0.0.11:53053 .If The root doesn't have the answer then he sends the Dns resolver to ask Telematik and FuBerlin (TLD).The process contiunes until the resolver gets an IP adress  If the TLD's don't have the answer the the recrusive resolver proceeds to ask Switch, Router, Homework ,Pcpools. If the resolver doesn't get answer he logs an error with the name rcode=3 which means the domain name doesn't have any information.


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

2.  Recursive Resolver


![name-of-you-image](https://github.com/Alioio/telematics_project/blob/main/Notebooks/screenshots/recursiveresolver/11.PNG)

 

Photo 2.1 -  Our Recursive Resolver has cache .when client sends request,first recursive resolver checks whetever cache has response for request or not.When it has, returns entry from cache, if not , then our cache entry is none.We check here all the entry of cache.Our recutsive resolver accessible under the IP address:127.0.0.10:53053. In cache we have many functions that perform for cache's functions.When we find the response ,then cache adds entry with add_entry_cache functions.Our cache has also TTL(Time to leave),with this TTL consider we that how much time the entry remains in 
the cache.



![name-of-you-image](https://github.com/Alioio/telematics_project/blob/main/Notebooks/screenshots/recursiveresolver/12.png)


Photo 2.2 -  We create connection among servers and also between clients and servers with socket libraries.First recursive resolver begins to listen requests and check if it is a request from a stub resolver or not.

![name-of-you-image](https://github.com/Alioio/telematics_project/blob/main/Notebooks/screenshots/recursiveresolver/13.png)


Photo 2.3 -  .We use here thread in order to perform many functions at the same time.We start all the process with start() function. Then check if requested entry is in the cache or not. When it is , then he responds to the client with "I HAVE THE ANSWER NO NEED TO ASK" message.


![name-of-you-image](https://github.com/Alioio/telematics_project/blob/main/Notebooks/screenshots/recursiveresolver/14.png)


Photo 2.4 - : Here we implement a code to send a response from the cache to the stubresolver which the forwards that to DNS.

![name-of-you-image](https://github.com/Alioio/telematics_project/blob/main/Notebooks/screenshots/recursiveresolver/15%20threading.png)


Photo 2.5 -  After that send response from cache to stub resolver.In other cases that cache has no entry for the request,the  recursive resolver 
forwards it to dns server.We implement the request to the dns server also with the thread.

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

3.DNS


![name-of-you-image](https://github.com/Alioio/telematics_project/blob/main/Notebooks/screenshots/DNS/21.png)


Photo 3.1 DNS


![name-of-you-image](https://github.com/Alioio/telematics_project/blob/main/Notebooks/screenshots/DNS/22.png)



Photo 3.2 DNS


![name-of-you-image](https://github.com/Alioio/telematics_project/blob/main/Notebooks/screenshots/DNS/23.png)


Photo 3.3 DNS


![name-of-you-image](https://github.com/Alioio/telematics_project/blob/main/Notebooks/screenshots/DNS/24.png)


Photo 3.4 DNS


![name-of-you-image](https://github.com/Alioio/telematics_project/blob/main/Notebooks/screenshots/DNS/25.png)


Photo 3.5 DNS


![name-of-you-image](https://github.com/Alioio/telematics_project/blob/main/Notebooks/screenshots/DNS/26.png)


Photo 3.6 DNS

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


