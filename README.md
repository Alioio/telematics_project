# telematics_project
 
 ## General Info 
 _________

In this project we implemented a dns server. Our dns server consists of 3 parts :  Stub resolver ,  Recursive resolver and autorative dns server. The main purpose for this implementation is to send a domain name and receive an IP address assigned for this domain name. 

## Technologies 
_________

1. Python3 (programming Language) 
2. Notebook Jupyter (For running the code)
3. Pandas Library (Creating the log file)
4. Json (For creating the zones )

## Setup 
__________ 
Stub Resolver , Recursive Resolver , DNS.

## Zones 
_______ 


![name-of-you-image](https://github.com/Alioio/telematics_project/blob/main/Notebooks/zones_telematik.png)


The process starts with the Dns Resolver which looks in the cache if the information that he seeks is in there, If not he then goes to ask root which reachable in this case with the IP address 127.0.0.11:53053 .If The root doesn't have the answer then he sends the Dns resolver to ask Telematik and FuBerlin (TLD).The process contiunes until the resolver gets an IP adress  If the TLD's don't have the answer the the recrusive resolver proceeds to ask Switch, Router, Homework ,Pcpools. If the resolver doesn't get answer he logs an error with the name rcode=3 which means the domain name doesn't have any information.

## How to run project: 

1. Open the following Jupyter Notebooks in your Browser: 

- `DNS.ipynb`<br>
- `Recursive_resolver.ipynb`<br>
- ` StubResolver.ipynb`<br>

2. Run all cell's in the following Notebooks: 
- `DNS.ipynb`<br>
- `Recursive_resolver.ipynb`<br>
- `StubResolver.ipynb` (Start the stub without sending a message.)

3. In the Notebook `StubResolver.ipynb` we prepared some messages to two different paths in our DNS structure. 

4. After sending some messages check the log files in the project directory. 

5. For restarting the server (stopping all threads running in parallel) press `Kernel restart` in the Notebook.

## Missing features:

- HTTP Server and Proxy.

## Details of our implementation:

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
First of all we load entrys for own zone from out json file.
Here we create load_zone() function in order to load all entries for our zone.Then check if a requested entry is in own zone or not.
(e.g this zonenameis telematik and requested address is for dns name www.switch.telematik means that switch is in our zone and we can send the address for switch.telematik.if it is not ,
 then returns none).We check whetever entry is in our zone with is_in_own_zone() function.In order to create response we have build_response() function.Here we set all the flags with appropriate values.
Let's look at some flags in order to know what do they mean.
dns.flags.response=1 means this is response not query
dns.qry.name is same which we look at domain name 
dns.qry.type=1 because we search IPv4 Address for domain name
dns.flags.rcode=0 when there is no problem , value 3 means that domain name referenced in query doesn't exsist
In order to response to client we create response_to_client() function.We have here send_request() function.We make this function to handle request and response togehter with threads.
At the end all the functions work with start() function.



![name-of-you-image](https://github.com/Alioio/telematics_project/blob/main/Notebooks/screenshots/DNS/21.png)


Photo 3.1 - Our DNS Server is accessible under the IP address:127.0.0.11:53053 . Loading all entrys for own zone from our json file. 
    (e.g. zonename: telematik for zone (telematik, swith, router))


![name-of-you-image](https://github.com/Alioio/telematics_project/blob/main/Notebooks/screenshots/DNS/22.png)



Photo 3.2 - Here we create load_zone() function in order to load all entries for our zone. Checking if a requested entry is in own zone. 
    (e.g. this zonename is telematik and requested address is for dns name www.swith.telematik.
    Means that swith is in our zone and we can send the adress for switch.telematik)
    Returns None if not.


![name-of-you-image](https://github.com/Alioio/telematics_project/blob/main/Notebooks/screenshots/DNS/23.png)


Photo 3.3 -We check whetever entry is in our zone with is_in_own_zone() function.Checks if this dns can send directly the authorative answer? 
 


![name-of-you-image](https://github.com/Alioio/telematics_project/blob/main/Notebooks/screenshots/DNS/24.png)


Photo 3.4 - In order to create response we have build_response() function.Here we set all the flags with appropriate values.

--dns.flags.response=1 means this is response not query
--dns.qry.name is same which we look at domain name 
--dns.qry.type=1 because we search IPv4 Address for domain name
--dns.flags.rcode=0 when there is no problem , value 3 means that domain name referenced in query doesn't exsist


![name-of-you-image](https://github.com/Alioio/telematics_project/blob/main/Notebooks/screenshots/DNS/25.png)


Photo 3.5 - In order to response to client we create response_to_client() function.We have here send_request() function.We make this function to handle request and response togehter with threads.

![name-of-you-image](https://github.com/Alioio/telematics_project/blob/main/Notebooks/screenshots/DNS/26.png)


Photo 3.6 - At the end all the functions work with start() function.

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
