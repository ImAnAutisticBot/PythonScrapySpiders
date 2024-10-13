# CRAWLER RETURNING OSU COE COURSE SYLLABI AND CSE DEPARTMENT FACULTY

This project is based on Python Scrapy and SQLite3. Python Scrapy is for crawling all the data to .csv files, and SQLite3 is to import them to two databases storing all the data crawled from OSU website.

1. Clone the repository and extract the file.
   
2. Open the terminal. Direct into the Folder and start the service.
   
   ```
   $ cd "OSU Course Syllabi and Faculty Crawler\service"
   $ python service.py
   ```
3. Open the service in local terminal, APIs such as Postman, or browser.
    1) Use it in local terminal
      
      ```
      $ curl <link>
      $ curl "http://127.0.0.1:5000/cse"
      $ curl "http://127.0.0.1:5000/prof/Bucci, Paolo"
      ```
    2) Use it in APIs
       ```
       GET <link>
       ```
    4) Use it in browsers
       ```
       <link>
       ```
       It will return the .json data requested.
4. References
   Course Syllabi:
   
   ```
   aeroeng: Aerospace Engineering | aviatn: Aviation | bme: Biomedical Engineering | cbe: Chemical and Biomolecular Engineering
   civilen: Civil, Environmental, and Geodetic Engineering | cse: Computer Science and Engineering | ece: Electical and Computer Engineering
   engr: Engineering Administration | matscen: Materials Science and Engineering | mecheng: Mechanical Engineering
   ```
   
   You can get the data by type in this:
   
   ```
   "http://127.0.0.1:5000/<tablename>" which gives the list of appointed department courses
   "http://127.0.0.1:5000/cse" which gives the list of all CSE courses
   "http://127.0.0.1:5000/<tablename>/<course_number>" which gives the data of appointed course
   "http://127.0.0.1:5000/cse/CSE 2221" or "http://127.0.0.1:5000/cse/CSE%202221" which gives the data of CSE 2221
   ```
   
   CSE Faculty:
   
   You can get the data by type in this:
   
   ```
   "http://127.0.0.1:5000/prof" which gives the list of all CSE faculty
   "http://127.0.0.1:5000/prof/<prof_name>" which gives the data of the faculty
   "http://127.0.0.1:5000/prof/Bucci, Paolo" or "http://127.0.0.1:5000/prof/Bucci,%20Paolo" which gives the data of Professor Paolo Bucci
   ```
   
