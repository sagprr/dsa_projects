import time
from datetime import datetime as dt

ip_localmachine="127.0.0.1"
website_list=["instagram.com","youtube.com"]        # lists of the wesites to block 
hosts_path="/private/etc/hosts" #path of host file on mac to edit the ip address of websites
start_time="09:0:0"  #starting if working hours 
end_time="15:0:0"    # ending of working hours
 
"comment"
    
now=dt.now()
current_time=now.strftime("%H:%M:%S")
print(current_time) # printing the current time of the code execution 

while True:
    current_time=now.strftime("%H:%M:%S")
    if start_time<=current_time and current_time<=end_time:
        print("Working hours")  
        with open(hosts_path,"r+") as file:  #opening the file of hosts and writing on it + reading process
            content=file.read()
            for website in website_list:    
                if website in content:
                    pass
                
                else:
                    file.write(ip_localmachine+" "+website+"\n")
            
    else:
        print("Non working hours")
        with open(hosts_path,"r+") as file:
            file.seek()
            for line in content :
                if not any(website in line for website in website_list):
                    file.write(line)

            file.truncate(0)
            file.close()
            
    
    time.sleep(10)
