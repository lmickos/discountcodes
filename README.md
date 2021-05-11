Discountcode microservice - The Programming Task
================================================

The following text defined the programming part of the task:

You don’t hire a chef without tasting their food, and similarly we’d like to have a look at
your code. We’re interested in your structure, practices and design. So we would like you
to:

* Set the structure for the microservice that handles the discount codes.
* Implement two of its endpoints:
  - Generate a discount code
    + The brand wants to create X number of discount codes
  - Fetch a discount code
    + A user of the system gets a discount code
* Document your endpoints.
* Document how to set up and start the application.

The storage for discount codes in the service can be a real database, something in
memory or just hard coded mock data as you like and have time for.

Feel free to use any web framework or 3rd party modules that you’d like.

Please send us a link to a github repo with your implementation.

Don’t let the above limit you; if you can derive inspiration from your thought process in
the previous feature design task, please feel free to do so. We are interested in seeing
how you structure your code, what you choose to implement given the time and how you
do it. In the following meeting you’ll have time to reason about and elaborate on your
choices, what you would have done if you had more time, obstacles you encountered
and any other points you’d like to bring up.

The solution
============

Worth looking at
----------------
* The API documentation in HTML (https://lmickos.github.io/discountcodes/api.html)
* The Swagger (OAS 3.0) file in swagger_server/swagger/swagger.yaml
* All code in the swagger_server/storage_layer (implementes the 'Data Mapper' pattern).
  - Yes, it could be neater implemented, but it works for mockup...
* Logic of the implemented endpoints in swagger_server/controllers/default_controller

Considered architectures
------------------------
1. A simple Flask implementation
    * Benefits
        - Simple
    * Drawbacks
        - Nothing comes for free out of the box. 
          Security, error handling etc needs to be implemented by hand. 
        - Hard to scale

2. A code first framework
    * Benefits
    	- I get a lot of functionality for free
    * Drawbacks
        - Hard to keep a high level view of the implementation and hard to make docs for external users of the API
        - Will eventually become a mess of things
        - Depending on complex frameworks with a steep learning code

3. A spec first framework
  * Benefits
    - Can define the interface first and make sure the customer needs are met even before the coding starts
    - Can create automated mockups earli helping with test first approaches and developing in parallell on the API user side
    - Automated docs creation (e.g. usable in build pipe) that looks nice and can be given to 
    - Can create a skeleton setup for the code automatically
    - I get a lot of functionality for free, but maybe not as much as a code first approach
    - Automated testing and execution of compliance with the API spec
    - Possible to export Client support packages
  * Drawbacks
    - Hard to handle changes in the api. Requires a good separation between generated code and written code.
    - Depending on complex frameworks with a learning code that increases with the complexity of the api.
    - Tends to become complex and problems may be hard to troubleshoot and solve/workaround
        
Chosen architecture
-------------------

I chose the third version - Some of the reasoning behind:
* I focused on creating the spec first since I at first intended to focus on the architecture part
* I like to the API first approach
* I also like the many possible export opportunities given. 
* I was also curious to try out the latest version of Swagger/SwaggerHub (with OAS 3.0 support).
  Task assignments are a good time to test new things.

The API
-------
The API was designed using OAS (formerly Swagger) format on the Swaggerhub cloud implementation and exported using 
the Flask/Connexion extension. The API spec uses OAS version 3.0. Likewise the API docs were exported using a HTML export extension.

It may sometimes be hard to see the difference between what I created and what was automatically generated code.
I primarily wrote:
* All code in the swagger_server/storage_layer (implementes the 'Data Mapper' pattern).
* Logic of all the implemented functions in swagger_server/controllers/default_controller

Some of the code may not be optimally structured, but I prioritized hard and tried to keep close to the 
generated code for the times I needed to rerun API -> generation.


How to setup
------------
* ```pip3 install -r requirements.txt``` or ```pip install -r requirements.txt``` depending on OS/Python flavor
* You may have to run ```pip install 'connexion[swagger-ui]'``` (not documented, but it solved some problems I had)
* I installed PEP8 support (google it...) but that is just for checking the code style

How to run the implementation
-----------------------------

* cd into the root directory of the project
* Run ```python -m swagger_server``` to start the web server (or equivalent depending on os, python interpreter etc)
* Test the API
  - Browse to the root of the application as specified in the consol when starting up.
  - Look at a list of the endpoints exposed (but not necessarily implemented)
  - Use an HTTP tool 

Tools and technologies used
---------------------------
The following tools used where used to create and publish this solution:
* Python 3.9 (Latest at the current time)
* Python Idle - As IDE and text editor
* (UltraEdit as secondary text editor)
* PEP8 - For code style verification
* Postman for manual HTTP testing

* Git & SourceTree for code mgmt on local machine
* Github for cloud storage and publish of code


Whats next?
-----------
The following things would be the logical continuation on the implementation and pinpoints things that have not been done in this implementation (yet)
* Implement the remaining API endpoints
* Write unit tests for the storage layer
* Expand the automatically generated integration Test package 
or setup in an external tool like Postman.
* Debug the system more
* Import the OAS/Swagger file into Postman (using the OAS import support)
* Implement a real DB integration in the storage_layer


